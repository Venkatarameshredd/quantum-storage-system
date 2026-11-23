import re

with open('extracted_paper_from_pdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for any pattern like "Full Words (ABBR)" or "ABBR (Full Words)"
paren_patterns = re.findall(r'([A-Za-z\s,-]{3,50})\s*\(([A-Z0-9-]{2,10})\)', text)
print("=== Found Full Form (ABBR) definitions in PDF ===")
for full, abbr in paren_patterns:
    full = full.strip()
    if not full.startswith('Figure') and not full.startswith('Table') and not full.startswith('Theorem'):
        print(f"'{full}' -> ({abbr})")

paren_patterns_rev = re.findall(r'\b([A-Z0-9-]{2,10})\s*\(([A-Za-z\s,-]{3,50})\)', text)
print("\n=== Found ABBR (Full Form) in PDF ===")
for abbr, full in paren_patterns_rev:
    print(f"{abbr} -> '{full.strip()}'")
