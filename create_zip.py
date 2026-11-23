import os
import zipfile

src_dir = r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages'
out_zips = [
    r'C:\Users\AsuS\Downloads\Quantum_Resistant_ACM_6Pages_Updated.zip',
    r'd:\files (Quantum upodated code)\quantum_storage_system\Quantum_Resistant_ACM_6Pages_Updated.zip'
]

files_to_include = [
    'main.tex',
    'fig1_wide.png',
    'fig1_wide.pdf',
    'fig7_wide.png',
    'fig7_wide.pdf',
    'fig_cost_tradeoff.png',
    'fig_cost_tradeoff.pdf',
    'fig_satisfaction_distribution.png',
    'fig_satisfaction_distribution.pdf',
    'references_lncs.bib'
]

for out_zip in out_zips:
    with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files_to_include:
            p = os.path.join(src_dir, f)
            if os.path.exists(p):
                z.write(p, arcname=f)
                print(f"Added {f} to {out_zip}")
            else:
                print(f"WARNING: {f} not found!")

print("Overleaf packages created successfully!")
