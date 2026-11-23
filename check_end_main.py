with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Lines 390 to end:')
for i, l in enumerate(lines[390:]):
    print(f'{391+i}: {l.strip()}')
