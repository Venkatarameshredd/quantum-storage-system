with open('overleaf_project/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove 3rd uploaded item (Corresponding author footnote and email addresses)
old_authors = r'''\author[qti,srm]{Varsha Sambhaje\corref{cor1}}
\ead{varsha.s@srmap.edu.in}

\author[srm]{Madhira Venkata Ramesh Reddy}
\ead{ramesh\_madhira@srmap.edu.in}

\cortext[cor1]{Corresponding author: varsha.s@srmap.edu.in}'''

new_authors = r'''\author[qti,srm]{Varsha Sambhaje}

\author[srm]{Madhira Venkata Ramesh Reddy}'''

if old_authors in text:
    text = text.replace(old_authors, new_authors)
    print('1. Authors and footnote updated (3rd uploaded item removed)')
else:
    print('1. Authors block not found exactly!')

# 2. Fix page 5 equations going out of column
old_eq2 = r'''\begin{equation}
  S_{\text{ecc}} = d_{\text{eph}} \cdot Q_{\text{static}} \pmod{p}, \quad (c_{\text{kyber}}, S_{\text{kyber}}) = \text{Kyber512\_Encaps}(\text{PK}_{\text{kyber}})
\end{equation}'''

new_eq2 = r'''\begin{equation}
\begin{aligned}
  S_{\text{ecc}} &= d_{\text{eph}} \cdot Q_{\text{static}} \pmod{p}, \\
  (c_{\text{kyber}}, S_{\text{kyber}}) &= \text{Kyber512\_Encaps}(\text{PK}_{\text{kyber}})
\end{aligned}
\end{equation}'''

if old_eq2 in text:
    text = text.replace(old_eq2, new_eq2)
    print('2a. Equation (2) updated to aligned format')
else:
    print('2a. Equation (2) not found exactly!')

old_eq4 = r'''\begin{equation}
  K_{\text{enc}} = \text{HKDF-Expand}(\text{PRK}, \text{``cloud-storage-enc-v1''}, 32), \quad K_{\text{auth}} = \text{HKDF-Expand}(\text{PRK}, \text{``cloud-storage-auth-v1''}, 32)
\end{equation}'''

new_eq4 = r'''\begin{equation}
\begin{aligned}
  K_{\text{enc}} &= \text{HKDF-Expand}(\text{PRK}, \text{``cloud-storage-enc-v1''}, 32), \\
  K_{\text{auth}} &= \text{HKDF-Expand}(\text{PRK}, \text{``cloud-storage-auth-v1''}, 32)
\end{aligned}
\end{equation}'''

if old_eq4 in text:
    text = text.replace(old_eq4, new_eq4)
    print('2b. Equation (4) updated to aligned format')
else:
    print('2b. Equation (4) not found exactly!')

# 3. Fix Table 6 going out of page -> make it double-column table*
old_t6 = r'''\begin{table}[!ht]
  \centering
  \scriptsize
  \setlength{\tabcolsep}{2.5pt}
  \caption{Energy Consumption, Memory RSS Footprint, and Instruction Count Microbenchmarks}
  \label{tab:6}
  \begin{tabularx}{\linewidth}{p{2.2cm}cccc}
    \toprule
    \textbf{Cryptographic Primitive} & \textbf{Instruction Count (K)} & \textbf{L1D Cache Miss Rate} & \textbf{Energy (mJ / Op)} & \textbf{Peak Memory RSS (KB)} \\
    \midrule
    ECDH-256 (Scalar) & 142.6 & 0.12\% & 0.028 & 14.2 \\
    Kyber-512 (Scalar C) & 218.4 & 0.38\% & 0.048 & 28.5 \\
    Kyber-512 (AVX-512) & 52.1 & 0.04\% & 0.010 & 22.1 \\
    AES-256-GCM (AES-NI) & 1,840.2 & 0.02\% & 0.412 & 36.4 \\
    Shamir (2,3) GF(257) & 31.8 & 0.01\% & 0.006 & 8.5 \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\tiny \textit{Note:} AVX-512 vectorization reduces Kyber energy dissipation by 79\%.
\end{table}'''

new_t6 = r'''\begin{table*}[!t]
  \centering
  \footnotesize
  \caption{Energy Consumption, Memory RSS Footprint, and Instruction Count Microbenchmarks}
  \label{tab:6}
  \begin{tabularx}{\textwidth}{p{4.2cm}cccc}
    \toprule
    \textbf{Cryptographic Primitive} & \textbf{Instruction Count (K)} & \textbf{L1D Cache Miss Rate} & \textbf{Energy (mJ / Op)} & \textbf{Peak Memory RSS (KB)} \\
    \midrule
    ECDH-256 (Scalar) & 142.6 & 0.12\% & 0.028 & 14.2 \\
    Kyber-512 (Scalar C) & 218.4 & 0.38\% & 0.048 & 28.5 \\
    Kyber-512 (AVX-512) & 52.1 & 0.04\% & 0.010 & 22.1 \\
    AES-256-GCM (AES-NI) & 1,840.2 & 0.02\% & 0.412 & 36.4 \\
    Shamir (2,3) GF(257) & 31.8 & 0.01\% & 0.006 & 8.5 \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\scriptsize \textit{Note:} AVX-512 vectorization reduces Kyber energy dissipation by 79\%.
\end{table*}'''

if old_t6 in text:
    text = text.replace(old_t6, new_t6)
    print('3. Table 6 updated to table*')
else:
    print('3. Table 6 not found exactly!')

# 4. Fix Table 9 overriding column 2 -> make it double-column table*
old_t9 = r'''\begin{table}[!ht]
  \centering
  \scriptsize
  \setlength{\tabcolsep}{2.5pt}
  \caption{Denial-of-Service Early-Drop Rejection Latency and Speedup Dynamics}
  \label{tab:9}
  \begin{tabularx}{\linewidth}{p{2.4cm}cccc}
    \toprule
    \textbf{Attack Scenario / Pipeline Stage} & \textbf{Rejection Latency} & \textbf{Throughput (Ops/sec)} & \textbf{CPU Load @ 10k Req/s} & \textbf{Speedup Factor} \\
    \midrule
    Baseline Architecture (No Early-Drop) & 1.095 ms & 913 ops/s & 100\% (Saturated) & 1.0x \\
    Inner GCM Tag Check (After Decaps) & 0.742 ms & 1,347 ops/s & 82.4\% & 1.5x \\
    Encrypted Share Parse Check & 0.410 ms & 2,439 ops/s & 46.5\% & 2.7x \\
    \textbf{Proposed Early-Drop HMAC Boundary} & \textbf{0.089 ms} & \textbf{11,235 ops/s} & \textbf{8.8\% (Healthy)} & \textbf{12.3x} \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\tiny \textit{Note:} Early-Drop outer HMAC rejects forged payloads in 0.089 ms, keeping gateway CPU utilization below 9\%.
\end{table}'''

new_t9 = r'''\begin{table*}[!t]
  \centering
  \footnotesize
  \caption{Denial-of-Service Early-Drop Rejection Latency and Speedup Dynamics}
  \label{tab:9}
  \begin{tabularx}{\textwidth}{p{5.5cm}cccc}
    \toprule
    \textbf{Attack Scenario / Pipeline Stage} & \textbf{Rejection Latency} & \textbf{Throughput (Ops/sec)} & \textbf{CPU Load @ 10k Req/s} & \textbf{Speedup Factor} \\
    \midrule
    Baseline Architecture (No Early-Drop) & 1.095 ms & 913 ops/s & 100\% (Saturated) & 1.0x \\
    Inner GCM Tag Check (After Decaps) & 0.742 ms & 1,347 ops/s & 82.4\% & 1.5x \\
    Encrypted Share Parse Check & 0.410 ms & 2,439 ops/s & 46.5\% & 2.7x \\
    \textbf{Proposed Early-Drop HMAC Boundary} & \textbf{0.089 ms} & \textbf{11,235 ops/s} & \textbf{8.8\% (Healthy)} & \textbf{12.3x} \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\scriptsize \textit{Note:} Early-Drop outer HMAC rejects forged payloads in 0.089 ms, keeping gateway CPU utilization below 9\%.
\end{table*}'''

if old_t9 in text:
    text = text.replace(old_t9, new_t9)
    print('4. Table 9 updated to table*')
else:
    print('4. Table 9 not found exactly!')

# 5. Fix Table 12 -> make it double-column table*
old_t12 = r'''\begin{table}[!ht]
  \centering
  \scriptsize
  \setlength{\tabcolsep}{2.5pt}
  \caption{Comprehensive Threat Vector Resilience Matrix comparing Security Foundations}
  \label{tab:12}
  \begin{tabularx}{\linewidth}{p{2.0cm}p{1.4cm}p{1.4cm}X}
    \toprule
    \textbf{Threat Vector / Attack Class} & \textbf{Classical ECC-256} & \textbf{Pure Kyber-512} & \textbf{Proposed Adaptive Hybrid System} \\
    \midrule
    Harvest Now, Decrypt Later (HNDL) & Vulnerable (Shor's) & Resilient & Resilient (Dual-Key HKDF Hybrid) \\
    Single Storage Domain Compromise & Vulnerable & Vulnerable & Resilient (Shamir 2-of-3 GF(257)) \\
    Denial-of-Service (Malformed Floods) & Vulnerable (High CPU) & Vulnerable (High CPU) & Resilient (Early-Drop HMAC Envelope) \\
    Audit Ledger Tampering / Rollback & Vulnerable & Vulnerable & Resilient (Append-Only SHA-256 Chain) \\
    Brute-Force Attack Velocity & Vulnerable & Vulnerable & Resilient (Bayesian Anomaly Classifier) \\
    Transport Segmentation Poisoning & Moderate & Vulnerable & Resilient (Payload-Aware Coalescence) \\
    Mathematical Premise Fragility & High (Quantum Break) & Moderate (Newer Math) & Resilient (Either Primitive Suffices) \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\tiny \textit{Note:} Our hybrid design preserves security even if either ECC or Kyber is computationally broken.
\end{table}'''

new_t12 = r'''\begin{table*}[!t]
  \centering
  \footnotesize
  \caption{Comprehensive Threat Vector Resilience Matrix comparing Security Foundations}
  \label{tab:12}
  \begin{tabularx}{\textwidth}{p{4.5cm}p{3.2cm}p{3.2cm}X}
    \toprule
    \textbf{Threat Vector / Attack Class} & \textbf{Classical ECC-256} & \textbf{Pure Kyber-512} & \textbf{Proposed Adaptive Hybrid System} \\
    \midrule
    Harvest Now, Decrypt Later (HNDL) & Vulnerable (Shor's) & Resilient & Resilient (Dual-Key HKDF Hybrid) \\
    Single Storage Domain Compromise & Vulnerable & Vulnerable & Resilient (Shamir 2-of-3 GF(257)) \\
    Denial-of-Service (Malformed Floods) & Vulnerable (High CPU) & Vulnerable (High CPU) & Resilient (Early-Drop HMAC Envelope) \\
    Audit Ledger Tampering / Rollback & Vulnerable & Vulnerable & Resilient (Append-Only SHA-256 Chain) \\
    Brute-Force Attack Velocity & Vulnerable & Vulnerable & Resilient (Bayesian Anomaly Classifier) \\
    Transport Segmentation Poisoning & Moderate & Vulnerable & Resilient (Payload-Aware Coalescence) \\
    Mathematical Premise Fragility & High (Quantum Break) & Moderate (Newer Math) & Resilient (Either Primitive Suffices) \\
    \bottomrule
  \end{tabularx}
  \vspace{2pt}
  \flushleft\scriptsize \textit{Note:} Our hybrid design preserves security even if either ECC or Kyber is computationally broken.
\end{table*}'''

if old_t12 in text:
    text = text.replace(old_t12, new_t12)
    print('5. Table 12 updated to table*')
else:
    print('5. Table 12 not found exactly!')

with open('overleaf_project/main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print('All requested adjustments written to overleaf_project/main.tex and main.tex!')
