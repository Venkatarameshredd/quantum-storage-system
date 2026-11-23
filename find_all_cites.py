with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'(\\cite\{[^\}]*\})', text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 40)
    print("MATCH:", text[start:end].replace('\n', ' '))
