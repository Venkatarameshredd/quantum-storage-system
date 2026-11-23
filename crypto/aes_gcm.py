from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AESGCMManager:
    def encrypt(self, key, plaintext, associated_data=None):
        nonce = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
        encryptor = cipher.encryptor()
        
        if associated_data:
            encryptor.authenticate_additional_data(associated_data)
            
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return nonce, ciphertext + encryptor.tag

    def decrypt(self, key, nonce, ciphertext, associated_data=None):
        tag = ciphertext[-16:]
        actual_ciphertext = ciphertext[:-16]
        
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
        decryptor = cipher.decryptor()
        
        if associated_data:
            decryptor.authenticate_additional_data(associated_data)
            
        plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
        return plaintext

aes_gcm_manager = AESGCMManager()
