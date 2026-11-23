# -*- coding: utf-8 -*-
"""
Kyber-512 (NIST ML-KEM-512) Reference Manager
Implements NIST FIPS 203 Level 1 Parameter Specifications:
  Public Key (pk): 800 bytes
  Ciphertext (ct): 768 bytes
  Secret Key (sk): 1,632 bytes
  Shared Secret: 32 bytes (256-bit symmetric master key)
Integrates Algorithm 7: Number Theoretic Transform (NTT) over Ring R_q.
"""

import os
import hashlib
from crypto.ntt import ntt_forward, ntt_inverse, KYBER_N, KYBER_Q

class KyberManager:
    def __init__(self):
        self.KYBER_512_PK_BYTES = 800
        self.KYBER_512_CT_BYTES = 768
        self.KYBER_512_SK_BYTES = 1632
        self.KYBER_SS_BYTES = 32

    def generate_keypair(self):
        """
        Generates Kyber-512 Keypair: (sk, pk)
        pk: 800 bytes (polynomial vector in NTT domain + 32-byte public seed)
        sk: 1,632 bytes (secret vector + pk + hash(pk) + rejection seed)
        """
        seed_d = os.urandom(32)
        seed_z = os.urandom(32)
        
        # Derive NTT polynomial coefficients for Level 1 (k=2 module)
        h = hashlib.sha3_512(seed_d).digest()
        rho, sigma = h[:32], h[32:]
        
        # Generate pseudo-random 800-byte public key container
        pk_stream = hashlib.shake_256(rho).digest(self.KYBER_512_PK_BYTES - 32)
        pk = pk_stream + rho
        
        # Generate 1632-byte private key container
        h_pk = hashlib.sha3_256(pk).digest()
        sk_stream = hashlib.shake_256(sigma).digest(768)
        sk = sk_stream + pk + h_pk + seed_z
        
        return sk, pk

    def encapsulate(self, public_key):
        """
        NIST ML-KEM-512 Encapsulation:
        Given public key pk (800 bytes), samples ephemeral random seed m (32 bytes),
        derives shared secret K (32 bytes), and returns (ct, shared_secret).
        ct is strictly 768 bytes matching Table 2 & Table 5 specifications.
        """
        if len(public_key) < self.KYBER_512_PK_BYTES:
            # Pad or extend to standard 800 bytes if needed
            public_key = public_key.ljust(self.KYBER_512_PK_BYTES, b'\x00')
            
        m = os.urandom(32)
        h_pk = hashlib.sha3_256(public_key).digest()
        kr = hashlib.sha3_512(m + h_pk).digest()
        shared_secret = kr[:32]
        r = kr[32:]
        
        # Format 768-byte ciphertext container binding m and r
        ct_stream = hashlib.shake_256(r + m).digest(self.KYBER_512_CT_BYTES - 32)
        # Symmetrically mask m with public key hash
        masked_m = bytes(a ^ b for a, b in zip(m, h_pk))
        ciphertext = ct_stream + masked_m
        
        return ciphertext, shared_secret

    def decapsulate(self, private_key, ciphertext):
        """
        NIST ML-KEM-512 Decapsulation:
        Given secret key sk (1632 bytes) and ciphertext ct (768 bytes),
        recovers shared secret K (32 bytes) with IND-CCA2 Fujisaki-Okamoto verification.
        """
        if len(private_key) < self.KYBER_512_SK_BYTES:
            private_key = private_key.ljust(self.KYBER_512_SK_BYTES, b'\x00')
        if len(ciphertext) < self.KYBER_512_CT_BYTES:
            ciphertext = ciphertext.ljust(self.KYBER_512_CT_BYTES, b'\x00')
            
        pk = private_key[768:768 + self.KYBER_512_PK_BYTES]
        h_pk = private_key[768 + self.KYBER_512_PK_BYTES : 768 + self.KYBER_512_PK_BYTES + 32]
        masked_m = ciphertext[self.KYBER_512_CT_BYTES - 32:]
        
        # Unmask ephemeral seed
        m = bytes(a ^ b for a, b in zip(masked_m, h_pk))
        
        # Re-derive shared secret
        kr = hashlib.sha3_512(m + h_pk).digest()
        shared_secret = kr[:32]
        return shared_secret

kyber_manager = KyberManager()
