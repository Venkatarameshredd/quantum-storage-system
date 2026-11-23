import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import win32com.client
import fitz
import io
import os
from PIL import Image

# 1. GENERATE COVERING LETTER
doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.55)
    s.bottom_margin = Inches(0.55)
    s.left_margin = Inches(0.75)
    s.right_margin = Inches(0.75)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'

def add_p(text='', bold=False, italic=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3, space_before=0, line_spacing=1.05):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
    return p

# Header / Sender Info
p_head = add_p(bold=True, size=12, space_after=1)
p_head.add_run('MADHIRA VENKATA RAMESH REDDY')

p_contact = add_p(size=9, space_after=6)
p_contact.add_run('M.Tech. Data Science (CGPA: 8.92) | Department of Computer Science and Engineering\n')
p_contact.add_run('SRM University-AP, Amaravati, Andhra Pradesh – 522240, India\n')
p_contact.add_run('Phone: +91-6301979587 | Email: ramesh_madhira@srmap.edu.in | LinkedIn: linkedin.com/in/madhira-venkata-ramesh-reddy')

# Date
add_p('Date: October 26, 2026', size=9.5, space_after=4)

# Recipient
p_to = add_p(size=9.5, space_after=5)
p_to.add_run('To,\nThe Awards & Honors Evaluation Committee,\n4th Indo-Canada International Conference on Advances in Research and Development (ICARD 2026)')

# Subject
p_sub = add_p(bold=True, size=10.5, space_after=5)
p_sub.add_run('Subject: Self-Nomination for "Best PG Research Thesis Award" – ICARD 2026')

# Salutation
add_p('Respected Committee Members,', size=9.5, space_after=3)

# Body Paragraph 1: Intent & Nomination Details
p_b1 = add_p(size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=3)
p_b1.add_run('I am pleased to submit my self-nomination for the ')
r_aw = p_b1.add_run('Best PG Research Thesis Award')
r_aw.bold = True
p_b1.add_run(' at the 4th Indo-Canada International Conference on Advances in Research and Development (ICARD 2026). I am currently an M.Tech. Data Science scholar at SRM University-AP (CGPA: 8.92/10). Below are my nomination credentials:')

# Metadata bullet points
items = [
    ('Name of Nominee', 'Madhira Venkata Ramesh Reddy'),
    ('Degree & Program', 'Master of Technology (M.Tech.) in Data Science (2025–2027) | Current CGPA: 8.92'),
    ('Award Nominated For', 'Best PG Research Thesis Award'),
    ('Research Area / Domain', 'Post-Quantum Cryptography, Quantum Computing & Cloud Storage Security'),
    ('Thesis Title', 'Adaptive Quantum-Resistant Hybrid Cloud Storage With Zero-Trust Key Distribution'),
    ('Research Advisor', 'Dr. Varsha Sambhaje, Quantum Technology, SRM University-AP')
]

for label, val in items:
    p_item = doc.add_paragraph()
    p_item.paragraph_format.space_before = Pt(0)
    p_item.paragraph_format.space_after = Pt(1.5)
    p_item.paragraph_format.left_indent = Inches(0.15)
    p_item.paragraph_format.line_spacing = 1.05
    r_l = p_item.add_run('• ' + label + ': ')
    r_l.bold = True
    r_l.font.name = 'Times New Roman'
    r_l.font.size = Pt(9)
    r_v = p_item.add_run(val)
    r_v.font.name = 'Times New Roman'
    r_v.font.size = Pt(9)

# Body Paragraph 2: Thesis Summary & Innovation
p_b2 = add_p(size=9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=3, space_after=3)
p_b2.add_run('Research Significance & Thesis Innovations: ').bold = True
p_b2.add_run(
    'My postgraduate thesis addresses Harvest Now, Decrypt Later (HNDL) attacks by quantum adversaries running Shor’s algorithm against classical public-key cryptography (RSA/ECC). To circumvent key expansion (12.5×) and transmission latency from direct post-quantum primitive deployment, this research synthesizes a five-fold defense architecture: '
    '(1) an Adaptive Encryption Decision Engine (AEDE) matching cipher strength to payload sensitivity; '
    '(2) a Dual-Key Hybrid KEM combining SECP256R1 and NIST ML-KEM (CRYSTALS-Kyber-512) via HKDF-SHA256 ensuring classical-quantum IND-CCA2 security; '
    '(3) Zero-Trust Shamir (2,3)-threshold secret sharing over GF(257) eliminating single repository compromise; '
    '(4) an Early-Drop outer HMAC-SHA256 boundary filter dropping forged requests in 0.089 ms (12.3× speedup against DoS); and '
    '(5) an append-only SHA-256 hash-chain audit ledger. Master key secrecy is mathematically proved via ProVerif 2.05 symbolic verification. Xeon benchmarks confirm hybrid encryption adds only 1.28 ms overhead for 1 MB payloads with 79% AVX-512 energy reduction.'
)

# Body Paragraph 3: Academic Track Record & Achievements
p_b3 = add_p(size=9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=3)
p_b3.add_run('Academic Excellence & Technical Leadership: ').bold = True
p_b3.add_run(
    'Alongside an 8.92 CGPA in M.Tech Data Science (and B.Tech CSE, CGPA: 7.54), I have developed quantum teleportation simulations with 99.4% state fidelity on Qiskit Aer, engineered production ML/deep learning pipelines, and served in leadership as Class Representative (M.Tech & B.Tech) and Vice President of the Code Geek Club.'
)

# Closing
p_close = add_p(size=9, space_after=5)
p_close.add_run('The technical novelty, formal proofs, and computational viability of this thesis make it a strong candidate for the Best PG Research Thesis Award. My brief CV is appended. Thank you for your consideration.')

# Sign-off
p_sign = add_p(size=9, space_after=0)
p_sign.add_run('Sincerely,\n')
r_sname = p_sign.add_run('Madhira Venkata Ramesh Reddy\n')
r_sname.bold = True
p_sign.add_run('M.Tech. Scholar | SRM University-AP | Mobile: +91-6301979587 | Email: ramesh_madhira@srmap.edu.in')

# Save covering letter docx & pdf
docx_out = os.path.abspath('Nomination_Covering_Letter.docx')
doc.save(docx_out)

word = win32com.client.Dispatch('Word.Application')
word.Visible = False
wb = word.Documents.Open(docx_out)
pdf_cov_out = os.path.abspath('Nomination_Covering_Letter.pdf')
wb.SaveAs(pdf_cov_out, FileFormat=17)
wb.Close()
word.Quit()
print('Nomination letter generated!')

doc_cov = fitz.open(pdf_cov_out)
print('Cover letter page count:', len(doc_cov))

# 2. MERGE WITH CV AND OPTIMIZE FILE SIZE (< 500 KB)
cv_path = os.path.abspath('C:/Users/AsuS/.gemini/antigravity/brain/b89b8ca2-2883-435b-a3bb-200173f01632/.user_uploaded/media_1792994482263_df7073ab.pdf')
doc_cv = fitz.open(cv_path)

merged_doc = fitz.open()
merged_doc.insert_pdf(doc_cov)

cv_page = doc_cv[0]
pix = cv_page.get_pixmap(dpi=160)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
buf = io.BytesIO()
img.save(buf, format='JPEG', quality=78, optimize=True)

new_p = merged_doc.new_page(width=cv_page.rect.width, height=cv_page.rect.height)
new_p.insert_image(cv_page.rect, stream=buf.getvalue())

merged_pdf_path = os.path.abspath('Best_PG_Thesis_Award_Nomination_Ramesh_Reddy.pdf')
merged_doc.save(merged_pdf_path, garbage=4, deflate=True, clean=True)
merged_doc.close()

size_kb = os.path.getsize(merged_pdf_path) / 1024
print(f'Final Merged PDF saved to: {merged_pdf_path}')
print(f'Total size: {size_kb:.2f} KB (must be < 500 KB: {size_kb < 500})')
print('Page count of final PDF:', len(fitz.open(merged_pdf_path)))
