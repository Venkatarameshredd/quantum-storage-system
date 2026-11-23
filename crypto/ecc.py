from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

class ECCManager:
    def generate_keypair(self):
        priv_key = ec.generate_private_key(ec.SECP256R1())
        pub_key = priv_key.public_key()
        return priv_key, pub_key

    def derive_shared_secret(self, my_priv, peer_pub):
        shared_key = my_priv.exchange(ec.ECDH(), peer_pub)
        return shared_key

ecc_manager = ECCManager()
