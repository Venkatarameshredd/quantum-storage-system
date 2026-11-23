with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check citations in body:
c1 = r'public-key ciphers (RSA-3072, ECC-256)~\cite{mell2011nist,boneh2020graduate}'
print("c1 in text:", c1 in text)

c2 = r'elliptic curve discrete logarithms (ECDLP)~\cite{katz2020introduction}'
print("c2 in text:", c2 in text)

c3 = r'Shor\'s algorithm~\cite{shor1994algorithms}'
print("c3 in text:", c3 in text)

c4 = r'HIPAA and financial records~\cite{mosca2022quantum}'
print("c4 in text:", c4 in text)

c5 = r'NIST ML-KEM (CRYSTALS-Kyber)~\cite{bos2018crystals,avanzi2021crystals}'
print("c5 in text:", c5 in text)

c6 = r'exfiltration of databases~\cite{sahai2021use}'
print("c6 in text:", c6 in text)

c7 = r'TLS 1.3 network handshakes~\cite{sikeridis2020assessing}'
print("c7 in text:", c7 in text)

c8 = r'hybrid KEM theoretical formulations~\cite{bindel2019hybrid,stebila2023hybrid,stebila2016post}'
print("c8 in text:", c8 in text)

c9 = r'classical Shamir secret sharing~\cite{shamir1979share}'
print("c9 in text:", c9 in text)

c10_t1_1 = r'Pure ECC~\cite{boneh2020graduate}'
print("c10_t1_1 in text:", c10_t1_1 in text)

c10_t1_2 = r'Pure Kyber~\cite{bos2018crystals}'
print("c10_t1_2 in text:", c10_t1_2 in text)

c10_t1_3 = r'Hybrid TLS 1.3~\cite{stebila2023hybrid}'
print("c10_t1_3 in text:", c10_t1_3 in text)

c10_t1_4 = r'KMS Cluster~\cite{sahai2021use}'
print("c10_t1_4 in text:", c10_t1_4 in text)

c11 = r'property of HKDF~\cite{krawczyk2010hmac}'
print("c11 in text:", c11 in text)

c12 = r'Module-LWE simultaneously~\cite{bindel2019hybrid}'
print("c12 in text:", c12 in text)

c13 = r'HKDF extraction lemma~\cite{krawczyk2010hmac}'
print("c13 in text:", c13 in text)

c14 = r'lattice-based Module-LWE~\cite{avanzi2021crystals}'
print("c14 in text:", c14 in text)

c15_1 = r'Shor\'s algorithm~\cite{shor1994algorithms}'
print("c15_1 in text:", c15_1 in text)

c15_2 = r'O(\sqrt{N})\text{ search}~\cite{grover1996fast}'
print("c15_2 in text:", c15_2 in text)
