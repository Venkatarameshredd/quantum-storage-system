with open('updated_main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re
body = text[:text.find(r'\begin{thebibliography}')]
for m in re.finditer(r'avanzi2021crystals', body):
    start = max(0, m.start() - 50)
    end = min(len(body), m.end() + 50)
    print("Match avanzi:", body[start:end].replace('\n', ' '))

for m in re.finditer(r'krawczyk2010hmac', body):
    start = max(0, m.start() - 50)
    end = min(len(body), m.end() + 50)
    print("Match krawczyk:", body[start:end].replace('\n', ' '))
