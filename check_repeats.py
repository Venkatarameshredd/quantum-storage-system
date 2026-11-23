import re

with open('extracted_paper_from_pdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check phrases that appear multiple times
phrases_to_check = [
    'Key Encapsulation Mechanism',
    'Adaptive Encryption Decision Engine',
    'Harvest Now, Decrypt Later',
    'Harvest Now Decrypt Later',
    'Denial-of-Service',
    'Denial-of-service',
    'Galois Field',
    'Galois field',
    'Hardware Security Module',
    'key management services',
    'key management service',
    'integer factorization',
    'elliptic curve discrete logarithm',
    'elliptic curve',
    'Maximum Transmission Unit',
    'Wide Area Network',
    'Service-Level Agreement',
    'Service Level Agreement',
    'applied pi-calculus',
    'ProVerif',
    'Shor’s algorithm',
    'Shamir secret sharing',
    'early-drop',
    'Early-Drop',
]

for p in phrases_to_check:
    matches = list(re.finditer(re.escape(p), text, re.IGNORECASE))
    print(f'{p}: {len(matches)} occurrences')
    for m in matches:
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        snippet = text[start:end].replace('\n', ' ')
        print(f'   -> "...{snippet}..."')
