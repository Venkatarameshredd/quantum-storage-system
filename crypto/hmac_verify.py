import hmac
import hashlib

class HMACManager:
    def generate_mac(self, key, message):
        return hmac.new(key, message, hashlib.sha256).digest()

    def verify_mac(self, key, message, signature):
        expected_mac = self.generate_mac(key, message)
        return hmac.compare_digest(expected_mac, signature)

hmac_manager = HMACManager()
