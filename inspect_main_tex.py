with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines in main.tex: {len(lines)}')

# Let's inspect sections and headings
for idx, l in enumerate(lines):
    if l.startswith(r'\section') or l.startswith(r'\subsection') or l.startswith(r'\subsubsection') or l.startswith(r'\title') or l.startswith(r'\author'):
        print(f'{idx+1}: {l.strip()}')
