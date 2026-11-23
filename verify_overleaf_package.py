import re
import os

with open('overleaf_project/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

# 1. FloatBarrier check
fb_count = text.count('FloatBarrier')
print(f'1. FloatBarrier count: {fb_count} (Should be 0)')
assert fb_count == 0, 'FloatBarrier found!'

# 2. clearpage / newpage check
cp_count = len(re.findall(r'\\(clearpage|newpage|pagebreak)', text))
print(f'2. clearpage/newpage count: {cp_count} (Should be 0)')
assert cp_count == 0, 'Forced page break found!'

# 3. Math delimiter balance
in_math = False
math_errors = 0
for i, l in enumerate(lines):
    pos = l.find('%')
    while pos != -1:
        if pos == 0 or l[pos-1] != '\\':
            l = l[:pos]
            break
        pos = l.find('%', pos+1)
    clean = l.replace(r'\$', '')
    for c in clean:
        if c == '$':
            in_math = not in_math
    if l.strip() == '' and in_math:
        math_errors += 1

print(f'3. Paragraph in math errors: {math_errors}, Final in_math: {in_math}')
assert math_errors == 0 and not in_math, 'Math delimiters unbalanced!'

# 4. Environments balance
begins = re.findall(r'\\begin\{([^}]+)\}', text)
ends = re.findall(r'\\end\{([^}]+)\}', text)
from collections import Counter
bc = Counter(begins)
ec = Counter(ends)
env_diffs = []
for k in set(bc.keys()) | set(ec.keys()):
    if bc[k] != ec[k]:
        env_diffs.append((k, bc[k], ec[k]))
print(f'4. Environments: {len(begins)} begins, {len(ends)} ends. Mismatches: {env_diffs}')
assert len(env_diffs) == 0, f'Environment mismatch: {env_diffs}'

# 5. Figures audit (15 total: 4 figure, 11 figure*)
figs = re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}', text, re.DOTALL)
print(f'5. Figures count: {len(figs)} (Should be 15)')
assert len(figs) == 15, f'Expected 15 figures, found {len(figs)}'

# 6. Tables audit (14 total: 8 table*, 6 table)
tabs = re.findall(r'\\begin\{(table\*?)\}(.*?)\\end\{\1\}', text, re.DOTALL)
print(f'6. Tables count: {len(tabs)} (Should be 14)')
assert len(tabs) == 14, f'Expected 14 tables, found {len(tabs)}'

# 7. Algorithms audit (7 total)
algs = re.findall(r'\\begin\{(algorithm\*?)\}(.*?)\\end\{\1\}', text, re.DOTALL)
print(f'7. Algorithms count: {len(algs)} (Should be 7)')
assert len(algs) == 7, f'Expected 7 algorithms, found {len(algs)}'

# 8. References audit (48 total)
bibs = re.findall(r'\\bibitem\{([^}]+)\}', text)
print(f'8. Bibitems count: {len(bibs)} (Should be 48)')
assert len(bibs) == 48, f'Expected 48 bibitems, found {len(bibs)}'

# 9. Preamble packages
assert r'\usepackage{dblfloatfix}' in text, 'dblfloatfix missing from preamble'
print('9. dblfloatfix confirmed in preamble')

# 10. Check double-column float specifiers: should NOT have [!b] without [t]
for m in re.finditer(r'\\begin\{(figure\*|table\*)\}\[([^\]]*)\]', text):
    env = m.group(1)
    spec = m.group(2)
    assert 'b' not in spec or 't' in spec, f'{env} has invalid bottom-only specifier: [{spec}]'

print('10. All double-column float specifiers verified to be safe (top-placed)!')
print('\n*** ALL 10 QUALITY ASSURANCE CRITERIA PASSED! ***')
