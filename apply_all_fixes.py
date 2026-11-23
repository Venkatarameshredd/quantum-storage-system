import re

with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Title and authors
text = text.replace(
r'''\title{Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms}

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
\email{ramesh_madhira@srmap.edu.in}''',
r'''\title{Adaptive Quantum-Resistant Hybrid Cloud Storage With Zero-Trust Key Distribution}

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
)

# 2. Section 1 Introduction abbreviations & text
text = text.replace(
r'''Enterprise cloud storage relies on public-key ciphers (RSA-3072, ECC-256)~\cite{mell2011nist,boneh2020graduate} secured by integer factorization (IFP) and elliptic curve discrete logarithms (ECDLP)~\cite{katz2020introduction}. While classical algorithms require sub-exponential $\mathcal{O}(\exp((c + o(1))(\ln n)^{1/3}(\ln \ln n)^{2/3}))$ or exponential $\mathcal{O}(\sqrt{p})$ time, Shor's algorithm~\cite{shor1994algorithms} breaks both in polynomial time $\mathcal{O}(n^3)$. A $\sim$4,000-qubit quantum device compromises RSA/ECC in seconds, empowering adversaries to execute ``Harvest Now, Decrypt Later'' (HNDL) attacks on 50-year regulatory archives such as HIPAA and financial records~\cite{mosca2022quantum}. Naive deployment of NIST ML-KEM (CRYSTALS-Kyber)~\cite{bos2018crystals,avanzi2021crystals} introduces three critical operational barriers:
\begin{enumerate}
    \item \textbf{Key Expansion Overhead:} Kyber-512 public keys require 800 bytes, representing a $12.5\times$ expansion over SECP256R1 (65 bytes).
    \item \textbf{WAN MTU Fragmentation:} Combined lattice public keys and ciphertexts exceed standard 1500-byte WAN MTUs, resulting in packet fragmentation and connection latency penalties.
    \item \textbf{Central Repository Exposure:} Centralized key management services (KMS) present single-point targets for catastrophic database exfiltration~\cite{sahai2021use}.
\end{enumerate}

\noindent\textbf{Contributions.} We deliver five core technical contributions:
\begin{itemize}
    \item A holistic multi-layered quantum-resistant cloud storage architecture harmonizing dynamic client profiling with server-side zero-trust repositories.
    \item An IND-CCA2 dual-key hybrid KEM combining SECP256R1 ECDH and Kyber-512 via HKDF-SHA256, guaranteeing security against both classical and quantum adversaries.
    \item Zero-Trust Shamir secret sharing over Galois Field GF(257) ensuring zero Shannon mutual information for any single repository breach.
    \item An Early-Drop outer HMAC-SHA256 boundary filter rejecting forged payloads in 0.089~ms, achieving a $12.3\times$ speedup against CPU-exhaustion DoS floods.
    \item Formal verification in ProVerif 2.05 confirming master key secrecy and boundary invariance, backed by bare-metal Xeon microbenchmarks across 100~KB--10~MB payloads.
\end{itemize}''',
r'''Enterprise cloud storage relies on public-key ciphers (RSA-3072, Elliptic Curve Cryptography (ECC-256))~\cite{mell2011nist,boneh2020graduate} secured by the Integer Factorization Problem (IFP) and the Elliptic Curve Discrete Logarithm Problem (ECDLP)~\cite{katz2020introduction}. While classical algorithms require sub-exponential $\mathcal{O}(\exp((c + o(1))(\ln n)^{1/3}(\ln \ln n)^{2/3}))$ or exponential $\mathcal{O}(\sqrt{p})$ time, Shor's algorithm~\cite{shor1994algorithms} breaks both in polynomial time $\mathcal{O}(n^3)$. A $\sim$4,000-qubit quantum device compromises RSA/ECC in seconds, empowering adversaries to execute HNDL attacks on 50-year regulatory archives such as HIPAA and financial records~\cite{mosca2022quantum}. Naive deployment of NIST ML-KEM (CRYSTALS-Kyber)~\cite{bos2018crystals,avanzi2021crystals} introduces three critical operational barriers:
\begin{enumerate}
    \item \textbf{Key Expansion Overhead:} Kyber-512 public keys require 800 bytes, representing a $12.5\times$ expansion over SECP256R1 (65 bytes).
    \item \textbf{WAN MTU Fragmentation:} Combined lattice public keys and ciphertexts exceed standard 1500-byte Wide Area Network (WAN) Maximum Transmission Unit (MTU) boundaries, resulting in packet fragmentation and connection latency penalties.
    \item \textbf{Central Repository Exposure:} Centralized Key Management Services (KMS) present single-point targets for catastrophic database exfiltration~\cite{sahai2021use}.
\end{enumerate}

\noindent\textbf{Contributions.} We deliver five core technical contributions:
\begin{itemize}
    \item A holistic multi-layered quantum-resistant cloud storage architecture harmonizing dynamic client profiling with server-side zero-trust repositories.
    \item An IND-CCA2 dual-key hybrid Key Encapsulation Mechanism (KEM) combining SECP256R1 Elliptic Curve Diffie-Hellman (ECDH) and Kyber-512 via HKDF-SHA256, guaranteeing security against both classical and quantum adversaries.
    \item Zero-Trust Shamir secret sharing over the Galois Field GF(257) ensuring zero Shannon mutual information for any single repository breach.
    \item An Early-Drop outer HMAC-SHA256 boundary filter rejecting forged payloads in 0.089~ms, achieving a $12.3\times$ speedup against CPU-exhaustion Denial-of-Service (DoS) floods.
    \item Formal verification in ProVerif 2.05 confirming master key secrecy and boundary invariance, backed by bare-metal Xeon microbenchmarks across 100~KB--10~MB payloads.
\end{itemize}'''
)

# 3. Section 2 Related Work
text = text.replace(
r'''\section{Related Work and Architectural Comparison}
Post-quantum transition efforts have predominantly focused on TLS 1.3 network handshakes~\cite{sikeridis2020assessing} and hybrid KEM theoretical formulations~\cite{bindel2019hybrid,stebila2023hybrid,stebila2016post}. In storage environments, classical Shamir secret sharing~\cite{shamir1979share} has been applied for fault tolerance, but has not been integrated with lattice encapsulation, early-drop DoS defenses, and tamper-evident audit chains. Table~\ref{tab:comparison} contrasts existing security models with our proposed adaptive hybrid architecture.''',
r'''\section{Related Work and Architectural Comparison}
Post-Quantum Cryptography (PQC) transition efforts have predominantly focused on TLS 1.3 network handshakes~\cite{sikeridis2020assessing} and hybrid KEM theoretical formulations~\cite{bindel2019hybrid,stebila2023hybrid,stebila2016post}. In storage environments, classical Shamir secret sharing~\cite{shamir1979share} has been applied for fault tolerance, but has not been integrated with lattice encapsulation, early-drop DoS defenses, and tamper-evident audit chains. Table~\ref{tab:comparison} contrasts existing security models with our proposed adaptive hybrid architecture.'''
)

# 4. Table 1: Remove repeated citations
text = text.replace(
r'''Pure ECC~\cite{boneh2020graduate} & No & Yes & No & No & No & Opt. \\
Pure Kyber~\cite{bos2018crystals} & Yes & No & No & No & No & Opt. \\
Hybrid TLS 1.3~\cite{stebila2023hybrid} & Yes & Yes & No & Partial & No & No \\
KMS Cluster~\cite{sahai2021use} & Opt. & Opt. & Yes & No & No & Yes \\''',
r'''Pure ECC & No & Yes & No & No & No & Opt. \\
Pure Kyber & Yes & No & No & No & No & Opt. \\
Hybrid TLS 1.3 & Yes & Yes & No & Partial & No & No \\
KMS Cluster & Opt. & Opt. & Yes & No & No & Yes \\'''
)

# 5. Section 3.1 & 3.2 Headings & text
text = text.replace(
r'''\subsection{Dual-Key Hybrid Key Encapsulation Mechanism}
To guarantee forward secrecy against future quantum attacks without sacrificing classical compliance, the client generates dual shared secrets: classical $S_{ecc}$ via SECP256R1 ECDH and post-quantum $S_{kyber}$ via Kyber-512 KEM. The master session key $K_{master}$ is derived using HKDF-SHA256:
\begin{align}
K_{hybrid} &= \text{HKDF-Extract}(salt, S_{ecc} \parallel S_{kyber}), \label{eq:khybrid} \\
K_{master} &= \text{HKDF-Expand}(K_{hybrid}, info, 32). \nonumber
\end{align}
By the dual-PRF property of HKDF~\cite{krawczyk2010hmac}, $K_{master}$ remains indistinguishable from random unless an adversary solves both ECDLP and Module-LWE simultaneously~\cite{bindel2019hybrid}.''',
r'''\subsection{Dual-Key Hybrid KEM}
To guarantee forward secrecy against future quantum attacks without sacrificing classical compliance, the client generates dual shared secrets: classical $S_{ecc}$ via SECP256R1 ECDH and post-quantum $S_{kyber}$ via Kyber-512 KEM. The master session key $K_{master}$ is derived using the HMAC-based Key Derivation Function (HKDF-SHA256):
\begin{align}
K_{hybrid} &= \text{HKDF-Extract}(salt, S_{ecc} \parallel S_{kyber}), \label{eq:khybrid} \\
K_{master} &= \text{HKDF-Expand}(K_{hybrid}, info, 32). \nonumber
\end{align}
By the dual-PRF property of HKDF~\cite{krawczyk2010hmac}, $K_{master}$ remains indistinguishable from random unless an adversary solves both ECDLP and Module Learning With Errors (Module-LWE) simultaneously.'''
)

# 6. Table 2: Nonce definition for AES-256-GCM
text = text.replace(
r'''Payload Nonce & Deterministic IV & 12 B & Nonce for AES-256-GCM \\''',
r'''Payload Nonce & Deterministic IV & 12 B & Nonce for Advanced Encryption Standard Galois/Counter Mode (AES-256-GCM) \\'''
)

# 7. Section 3.4: Outer HMAC definition
text = text.replace(
r'''signs fixed-length container headers using an outer HMAC-SHA256 key $K_{gw}$ pre-shared during tenant onboarding''',
r'''signs fixed-length container headers using an outer Hash-based Message Authentication Code (HMAC-SHA256) key $K_{gw}$ pre-shared during tenant onboarding'''
)

# 8. Theorem 4.1 Proof: remove repeated cites to HKDF and Kyber
text = text.replace(
r'''An adversary $\mathcal{A}$ breaking $K_{hybrid}$ implies breaking the HKDF extraction lemma~\cite{krawczyk2010hmac}. Since $K_{hybrid} = \text{HKDF}(S_{ecc} \parallel S_{kyber})$, the derived key is computationally indistinguishable from uniform unless $\mathcal{A}$ solves both ECDLP and Module-LWE. Shor's algorithm solves ECDLP in polynomial time but cannot solve lattice-based Module-LWE~\cite{avanzi2021crystals}. Hence, quantum forward secrecy holds unconditionally against classical-quantum hybrid adversaries.''',
r'''An adversary $\mathcal{A}$ breaking $K_{hybrid}$ implies breaking the HKDF extraction lemma. Since $K_{hybrid} = \text{HKDF}(S_{ecc} \parallel S_{kyber})$, the derived key is computationally indistinguishable from uniform unless $\mathcal{A}$ solves both ECDLP and Module-LWE. Shor's algorithm solves ECDLP in polynomial time but cannot solve lattice-based Module-LWE. Hence, quantum forward secrecy holds unconditionally against classical-quantum hybrid adversaries.'''
)

# 9. Section 4: MitM definition
text = text.replace(
r'''holds true against active MitM adversaries;''',
r'''holds true against active Man-in-the-Middle (MitM) adversaries;'''
)

# 10. Table 3: Remove repeated cites and abbreviations
text = text.replace(
r'''Harvest Now, Decrypt Later & Shor's algorithm~\cite{shor1994algorithms} & Ingress WAN & Kyber-512 lattice encapsulation (MLWE) & Negligible ($2^{128}$) \\
Central Database Breach & SQLi / Exfiltration & PostgreSQL Metadata & Shamir (2,3)-threshold sharing over GF(257) & Zero (Info-Theoretic) \\
Denial-of-Service Flood & Malformed Kyber storms & Gateway CPU Core & Early-Drop outer HMAC check (0.089 ms) & Negligible (12.3$\times$) \\
Man-in-the-Middle (MitM) & Ciphertext substitution & Network In-Transit & AES-GCM 128-bit authentication tag & Negligible ($2^{-128}$) \\
Forensic History Tampering & Audit log modification & Historical Logs & Append-only SHA-256 hash chain & Zero (Collision-Free) \\
Grover Quantum Search & $\mathcal{O}(\sqrt{N})$ search~\cite{grover1996fast} & AES Master Key & AES-256 provides 128-bit post-quantum security & Negligible ($2^{128}$) \\''',
r'''HNDL & Shor's algorithm & Ingress WAN & Kyber-512 lattice encapsulation (Module-LWE) & Negligible ($2^{128}$) \\
Central Database Breach & SQLi / Exfiltration & PostgreSQL Metadata & Shamir (2,3)-threshold sharing over GF(257) & Zero (Info-Theoretic) \\
DoS Flood & Malformed Kyber storms & Gateway CPU Core & Early-Drop outer HMAC check (0.089 ms) & Negligible (12.3$\times$) \\
MitM & Ciphertext substitution & Network In-Transit & AES-GCM 128-bit authentication tag & Negligible ($2^{-128}$) \\
Forensic History Tampering & Audit log modification & Historical Logs & Append-only SHA-256 hash chain & Zero (Collision-Free) \\
Grover Quantum Search & $\mathcal{O}(\sqrt{N})$ search~\cite{grover1996fast} & AES Master Key & AES-256 provides 128-bit post-quantum security & Negligible ($2^{128}$) \\'''
)

# 11. Section 5.1 & 5.2 Headings and abbreviations
text = text.replace(
r'''\subsection{Denial-of-Service Mitigation and Dynamic Telemetry}''',
r'''\subsection{DoS Mitigation and Dynamic Telemetry}'''
)

text = text.replace(
r'''Fig.~\ref{fig:sat}(a) shows the security-SLA satisfaction ratio''',
r'''Fig.~\ref{fig:sat}(a) shows the security Service-Level Agreement (SLA) satisfaction ratio'''
)

# 12. Reorder thebibliography
new_bib_order = [
    'mell2011nist',
    'boneh2020graduate',
    'katz2020introduction',
    'shor1994algorithms',
    'mosca2022quantum',
    'bos2018crystals',
    'avanzi2021crystals',
    'sahai2021use',
    'sikeridis2020assessing',
    'bindel2019hybrid',
    'stebila2023hybrid',
    'stebila2016post',
    'shamir1979share',
    'krawczyk2010hmac',
    'grover1996fast'
]

import parse_bib
parsed_entries = parse_bib.entries
new_bib_body = '\n\n'.join([parsed_entries[k] for k in new_bib_order])

bib_header = r'''\begin{thebibliography}{15}

%%% ====================================================================
%%% NOTE TO THE USER: you can override these defaults by providing
%%% customized versions of any of these macros before the \bibliography
%%% command.  Each of them MUST provide its own final punctuation,
%%% except for \shownote{}, \showDOI{}, and \showURL{}.  The latter two
%%% do not use final punctuation, in order to avoid confusing it with
%%% the Web address.
%%%
%%% To suppress output of a particular field, define its macro to expand
%%% to an empty string, or better, \unskip, like this:
%%%
%%% \newcommand{\showDOI}[1]{\unskip}   % LaTeX syntax
%%%
%%% \def \showDOI #1{\unskip}           % plain TeX syntax
%%%
%%% ====================================================================

\ifx \showCODEN    \undefined \def \showCODEN     #1{\unskip}     \fi
\ifx \showDOI      \undefined \def \showDOI       #1{#1}\fi
\ifx \showISBNx    \undefined \def \showISBNx     #1{\unskip}     \fi
\ifx \showISBNxiii \undefined \def \showISBNxiii  #1{\unskip}     \fi
\ifx \showISSN     \undefined \def \showISSN      #1{\unskip}     \fi
\ifx \showLCCN     \undefined \def \showLCCN      #1{\unskip}     \fi
\ifx \shownote     \undefined \def \shownote      #1{#1}          \fi
\ifx \showarticletitle \undefined \def \showarticletitle #1{#1}   \fi
\ifx \showURL      \undefined \def \showURL       {\relax}        \fi
% The following commands are used for tagged output and should be
% invisible to TeX
\providecommand\bibfield[2]{#2}
\providecommand\bibinfo[2]{#2}
\providecommand\natexlab[1]{#1}
\providecommand\showeprint[2][]{arXiv:#2}
'''

new_full_bib = bib_header + '\n\n' + new_bib_body + '\n\n\\end{thebibliography}'

old_bib_start = text.find(r'\begin{thebibliography}{15}')
old_bib_end = text.find(r'\end{thebibliography}') + len(r'\end{thebibliography}')
text = text[:old_bib_start] + new_full_bib + text[old_bib_end:]

with open('updated_main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

# Also write to C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex
with open(r'C:\Users\AsuS\OneDrive\Desktop\Quantum_Resistant_ACM_6Pages\main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated_main.tex and Desktop main.tex successfully! File length:", len(text))
