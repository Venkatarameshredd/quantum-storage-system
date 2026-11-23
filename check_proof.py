with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('HKDF extraction lemma')
print(text[pos-100:pos+400])
