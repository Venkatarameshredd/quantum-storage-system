import re

with open('updated_main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Verify Title & Authors
print("Title check:", "Adaptive Quantum-Resistant Hybrid Cloud Storage With Zero-Trust Key Distribution" in text)
print("Madhira author 1:", text.find("Madhira Venkata Ramesh Reddy") < text.find("Varsha Sambhaje"))
print("Varsha affiliation check:", "Quantum Technology \\& Institute" in text and "522240" in text)

# 2. Check all \cite in text before \begin{thebibliography}
body = text[:text.find(r'\begin{thebibliography}')]
cites = re.findall(r'\\cite\{([^}]+)\}', body)
print("\nAll citations in body (in order of appearance):")
all_keys_in_order = []
for c in cites:
    keys = [k.strip() for k in c.split(',')]
    print(f"  cite: {keys}")
    all_keys_in_order.extend(keys)

print("\nTotal individual citations in body:", len(all_keys_in_order))
print("Unique individual citations in body:", len(set(all_keys_in_order)))

# 3. Check bibitem order
bib_text = text[text.find(r'\begin{thebibliography}'):text.find(r'\end{thebibliography}')]
# Split by \bibitem
parts = re.split(r'\\bibitem\b', bib_text)
bib_keys = []
for p in parts[1:]:
    m = re.search(r'\{([a-zA-Z0-9_-]+)\}', p)
    if m:
        bib_keys.append(m.group(1))

print("\nBib items in order:")
for i, k in enumerate(bib_keys):
    print(f"  [{i+1}] {k}")

# 4. Check if body citations match 1, 2, ..., 15 in exact sequence
key_to_num = {k: i+1 for i, k in enumerate(bib_keys)}
rendered_nums = [key_to_num[k] for k in all_keys_in_order]
print("\nRendered citation numbers in body:")
print(rendered_nums)

is_sequential = (rendered_nums == list(range(1, 16)))
print("Is strictly sequential [1..15] with NO repetitions?", is_sequential)
