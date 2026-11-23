import re

with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Title and Authors / Affiliation
old_title_authors = r'''\title{Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms}

\author{Varsha Sambhaje}

\affiliation{%
  \institution{SRM University-AP}
  \department{Department of Computer Science and Engineering}
  \city{Neerukonda, Amaravati}
  \state{Andhra Pradesh}
  \country{India}
  \postcode{522240}
}
\email{varsha.s@srmap.edu.in}

\author{Madhira Venkata Ramesh Reddy}
\affiliation{%
  \institution{SRM University-AP}
  \department{Department of Computer Science and Engineering}
  \city{Neerukonda, Amaravati}
  \state{Andhra Pradesh}
  \country{India}
  \postcode{522240}
}
\email{ramesh_madhira@srmap.edu.in}'''

new_title_authors = r'''\title{Adaptive Quantum-Resistant Hybrid Cloud Storage With Zero-Trust Key Distribution}

\author{Madhira Venkata Ramesh Reddy}
\affiliation{%
  \institution{SRM University-AP}
  \department{Department of Computer Science and Engineering}
  \city{Neerukonda, Amaravati}
  \state{Andhra Pradesh}
  \country{India}
}
\email{ramesh_madhira@srmap.edu.in}

\author{Varsha Sambhaje}
\affiliation{%
  \institution{SRM University-AP}
  \department{Quantum Technology \& Institute}
  \department{Department of Computer Science and Engineering}
  \streetaddress{Neerukonda}
  \city{Amaravati}
  \state{Andhra Pradesh}
  \postcode{522240}
  \country{India}
}
\email{varsha.s@srmap.edu.in}'''

print("Title/authors match:", old_title_authors in text)
