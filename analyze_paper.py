import re

with open('extracted_paper_from_pdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pairs = [
    ('HNDL', 'Harvest Now, Decrypt Later'),
    ('HNDL', 'Harvest Now Decrypt Later'),
    ('AEDE', 'Adaptive Encryption Decision Engine'),
    ('KEM', 'Key Encapsulation Mechanism'),
    ('DoS', 'Denial-of-Service'),
    ('DoS', 'Denial of Service'),
    ('DoS', 'Denial-of-service'),
    ('IFP', 'integer factorization'),
    ('ECDLP', 'elliptic curve discrete logarithm'),
    ('ECC', 'Elliptic Curve Cryptography'),
    ('ECC', 'elliptic curve'),
    ('WAN', 'Wide Area Network'),
    ('MTU', 'Maximum Transmission Unit'),
    ('KMS', 'Key Management Service'),
    ('KMS', 'key management service'),
    ('GF', 'Galois Field'),
    ('GF', 'Galois field'),
    ('HSM', 'Hardware Security Module'),
    ('SLA', 'Service Level Agreement'),
    ('SLA', 'Service-Level Agreement'),
    ('SLA', 'Security-SLA'),
    ('PRF', 'Pseudorandom Function'),
    ('CDH', 'Computational Diffie-Hellman'),
    ('LWE', 'Learning With Errors'),
    ('MLWE', 'Module Learning With Errors'),
    ('MLWE', 'Module-LWE'),
    ('PQC', 'Post-Quantum Cryptography'),
    ('PQC', 'Post-Quantum'),
    ('ECDH', 'Elliptic Curve Diffie-Hellman'),
    ('HKDF', 'HMAC-based Extract-and-Expand Key Derivation Function'),
    ('HKDF', 'HMAC-based Key Derivation Function'),
    ('HMAC', 'Hash-based Message Authentication Code'),
    ('AES', 'Advanced Encryption Standard'),
    ('GCM', 'Galois/Counter Mode'),
    ('IV', 'Initialization Vector')
]

for acr, phrase in pairs:
    occurrences = [m.start() for m in re.finditer(re.escape(phrase), text, re.IGNORECASE)]
    if occurrences:
        print(f'{acr} <-> "{phrase}": found {len(occurrences)} times')
