with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

import re

bib_start = content.find(r'\begin{thebibliography}')
bib_end = content.find(r'\end{thebibliography}')
bib_text = content[bib_start:bib_end]

# Split by \bibitem
parts = re.split(r'\\bibitem\b', bib_text)
print("Parts found:", len(parts))

entries = {}
for p in parts[1:]:
    # Find {key}
    m = re.search(r'\{([a-zA-Z0-9_-]+)\}', p)
    if m:
        key = m.group(1)
        entries[key] = r'\bibitem' + p
        print("Parsed key:", key)

print("Parsed entries:", len(entries))
