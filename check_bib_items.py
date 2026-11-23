with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check the bib items in main.tex
import re
bib_items = re.findall(r'\\bibitem(?:\[.*?\])?\{([^}]+)\}', text)
print("Bib items count:", len(bib_items))
for idx, b in enumerate(bib_items):
    print(f"  {idx+1}: {b}")
