with open('updated_main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('Theorem 4.1')
print(text[pos:pos+700])
