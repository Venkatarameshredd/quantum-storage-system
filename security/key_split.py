import os
import random
from crypto.aes_gcm import aes_gcm_manager

class KeySplitter:
    # Basic Shamir Secret Sharing implementation over GF(256)
    def __init__(self):
        self.PRIME = 257 # Using simplified math for demo

    def _eval_poly(self, poly, x):
        result = 0
        for i in range(len(poly) - 1, -1, -1):
            result = (result * x + poly[i]) % self.PRIME
        return result

    def split_key(self, secret_key, threshold, shares):
        fragments = []
        for byte in secret_key:
            # Rejection sampling guard over GF(257):
            # Resample random polynomial slope if any share coordinate evaluates to 256.
            # This ensures each share coordinate strictly fits into an 8-bit unsigned byte [0, 255]
            # with probability 98.83% and expected 1.016 trials per byte.
            while True:
                poly = [byte] + [random.randint(1, self.PRIME - 1) for _ in range(threshold - 1)]
                byte_shares = [(i, self._eval_poly(poly, i)) for i in range(1, shares + 1)]
                if all(y < 256 for _, y in byte_shares):
                    break
            fragments.append(byte_shares)
        
        # Transpose fragments
        final_shares = [[] for _ in range(shares)]
        for byte_shares in fragments:
            for i, (x, y) in enumerate(byte_shares):
                final_shares[i].append((x, y))
        return final_shares

    def _lagrange_interpolate(self, x, x_s, y_s):
        k = len(x_s)
        secret = 0
        for i in range(k):
            num = 1
            den = 1
            for j in range(k):
                if i != j:
                    num = (num * (x - x_s[j])) % self.PRIME
                    den = (den * (x_s[i] - x_s[j])) % self.PRIME
            term = (y_s[i] * num * pow(den, self.PRIME - 2, self.PRIME)) % self.PRIME
            secret = (secret + term) % self.PRIME
        return secret

    def reconstruct_key(self, shares, threshold):
        k = len(shares[0])
        secret_bytes = []
        for i in range(k):
            x_s = [share[i][0] for share in shares[:threshold]]
            y_s = [share[i][1] for share in shares[:threshold]]
            secret_byte = self._lagrange_interpolate(0, x_s, y_s)
            secret_bytes.append(secret_byte)
        return bytes(secret_bytes)

    def encrypt_fragment(self, fragment, fragment_id):
        master_key = b"master_fragment_key_32_bytes_len"
        frag_bytes = bytes([y for x, y in fragment])
        nonce, ct = aes_gcm_manager.encrypt(master_key, frag_bytes)
        return nonce + ct

    def decrypt_fragment(self, encrypted_fragment, fragment_id):
        master_key = b"master_fragment_key_32_bytes_len"
        nonce = encrypted_fragment[:12]
        ct = encrypted_fragment[12:]
        pt = aes_gcm_manager.decrypt(master_key, nonce, ct)
        return [(fragment_id, b) for b in pt]

    def rotate_shares(self, existing_shares, threshold=2, shares=3):
        """
        Algorithm 5: Zero-Trust Key Rotation & Multi-Domain Re-encryption.
        Reconstructs symmetric payload key K_payload from existing shares,
        then instantiates fresh random degree-1 polynomials over GF(257) with
        rejection sampling to produce fresh independent shares without re-encrypting ciphertext.
        """
        k_payload = self.reconstruct_key(existing_shares, threshold=threshold)
        new_shares = self.split_key(k_payload, threshold=threshold, shares=shares)
        return k_payload, new_shares

key_splitter = KeySplitter()
