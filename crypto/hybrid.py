from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from crypto.ecc import ecc_manager
from crypto.kyber import kyber_manager
import os

class HybridManager:
    def generate_hybrid_keypair(self):
        ecc_priv, ecc_pub = ecc_manager.generate_keypair()
        kyber_priv, kyber_pub = kyber_manager.generate_keypair()
        return {
            'ecc_private': ecc_priv,
            'ecc_public': ecc_pub,
            'kyber_private': kyber_priv,
            'kyber_public': kyber_pub
        }

    def derive_combined_secret(self, ecc_secret, kyber_secret):
        return ecc_secret + kyber_secret

    def expand_keys(self, combined_secret, salt=None):
        if not salt:
            salt = os.urandom(16)
        
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=64,
            salt=salt,
            info=b'quantum_hybrid_kdf'
        )
        derived = hkdf.derive(combined_secret)
        return {
            'k_enc': derived[:32],
            'k_auth': derived[32:],
            'salt': salt
        }

hybrid_manager = HybridManager()
