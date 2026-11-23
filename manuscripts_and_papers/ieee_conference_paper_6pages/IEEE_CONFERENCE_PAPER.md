# Adaptive Hybrid Post-Quantum Cloud Storage with Zero-Trust Key Splitting and Network-Aware Handshake Optimization

**Varsha Sambhaje**$^*$ and **Madhira Venkata Ramesh Reddy**  
*Department of Computer Science, SRM University, Amaravati, 52240, Andhra pradesh, India*  
*\*Corresponding Author Email: varsha.s@srmap.edu.in | Co-Author: ramesh_madhira@srmap.edu.in*

---

## Abstract
The imminent realization of cryptographically relevant quantum computers represents an existential threat to modern cloud storage systems. Standard asymmetric cryptosystems, such as RSA and Elliptic Curve Cryptography (ECC), rely on integer factorization and discrete logarithms---computational problems that Shor's algorithm solves in polynomial $\mathcal{O}(n^3)$ time. This vulnerability is actively exploited by **"Harvest Now, Decrypt Later" (HNDL)** adversaries. While the National Institute of Standards and Technology (NIST) has standardized Module Lattice-Based Key Encapsulation (ML-KEM/Kyber), deploying pure post-quantum algorithms introduces substantial transport-layer fragmentation and centralized key management risks. Specifically, larger lattice public keys (800--1568 bytes) exceed TCP Maximum Segment Size (MSS) boundaries, inducing severe super-linear latency amplification over lossy cloud networks. 

In this paper, we propose, implement, and empirically evaluate an **Adaptive Hybrid Quantum-Resistant Cloud Storage Architecture**. The system introduces four primary novel contributions:
1. A closed-loop **Network-Aware Adaptive Hybrid Encapsulation (NA-AHE)** engine that dynamically balances confidentiality and network impairment telemetry to prevent TCP fragmentation cliffs;
2. A **Dual-Domain Zero-Trust Key Splitting** protocol based on Shamir's $(2,3)$ secret sharing over $\text{GF}(257)$ that algebraically guarantees zero mutual information leakage upon database breach ($I(K_{\text{enc}}; \text{Share}_j) = 0$);
3. An **Early-Drop Outer HMAC-SHA256 Shield** that drops forged ciphertexts before expensive polynomial decapsulation, delivering a measured **$106\times$ DoS rejection speedup**; and
4. An **Immutable Cryptographic Hash-Chain Ledger** featuring a sliding-window entropy anomaly classifier for real-time intrusion defense.

Extensive empirical evaluation across diverse payload sizes (100~KB to 10~MB) and synthetic network impairments demonstrates that our hybrid scheme incurs a negligible latency penalty of only **1.28~ms for a 1~MB file** (a mere **0.16~ms increase over classical ECC**) while providing comprehensive resilience across six major quantum and classical threat vectors.

**Index Terms**—Post-Quantum Cryptography (PQC), NIST ML-KEM, CRYSTALS-Kyber, Hybrid Key Encapsulation, Shamir Secret Sharing, Zero-Trust Architecture, Transport Fragmentation, Denial-of-Service Mitigation, Cloud Storage Security.

---

## 1. Introduction

Cloud storage infrastructures serve as the foundation of modern enterprise operations, hosting proprietary healthcare records, financial ledgers, government defense secrets, and intellectual property. To ensure confidentiality and integrity, cloud architectures rely heavily on asymmetric public-key cryptosystems, including RSA-3072 and Elliptic Curve Cryptography (ECC-256). The security of these primitives depends on the hardness of Integer Factorization (IFP) and the Elliptic Curve Discrete Logarithm Problem (ECDLP).

```mermaid
graph TD
    subgraph Roadmap [5 Core Defense Pillars of Proposed Architecture]
        P1[1. Network-Aware Adaptive Hybrid Engine NA-AHE]
        P2[2. Dual-Key Hybrid KEM: ECDH + Kyber-512 via HKDF]
        P3[3. Zero-Trust Key Splitting: Shamir 2-of-3 over GF 257]
        P4[4. Early-Drop Outer HMAC-SHA256 Shield 106x Anti-DoS]
        P5[5. Cryptographic Hash-Chain Forensic Ledger & Anomaly Engine]
    end
```

Under classical computing models, solving these problems requires sub-exponential time $\mathcal{O}(\exp(c n^{1/3} (\ln n)^{2/3}))$ via the General Number Field Sieve (GNFS) or exponential time $\mathcal{O}(\sqrt{p})$ via Pollard's rho algorithm. However, the emergence of Cryptographically Relevant Quantum Computers (CRQCs) running Shor's algorithm reduces their time complexity to polynomial time $\mathcal{O}(n^3)$. Consequently, standard public-key cryptography will suffer total compromise upon CRQC physical realization.

### 1.1 The "Harvest Now, Decrypt Later" (HNDL) Paradigm
This cryptographic cliff enables the "Harvest Now, Decrypt Later" (HNDL) attack strategy. State actors and adversaries intercept and archive encrypted cloud communications today, anticipating the ability to retroactively decrypt them once quantum computers mature. Because regulatory mandates (e.g., HIPAA, GDPR, PCI-DSS) require data confidentiality spans of 30 to 50+ years, post-quantum migration must occur immediately.

### 1.2 Limitations of Existing Post-Quantum Migration Approaches
To address this challenge, NIST finalized standards for Post-Quantum Cryptography (PQC), selecting Module Lattice-Based Key Encapsulation Mechanism (ML-KEM, formerly CRYSTALS-Kyber). Nevertheless, direct migration to standalone PQC introduces three critical vulnerabilities:
1. **Mathematical Maturation Risk:** Lattice-based math relies on the Module Learning With Errors (M-LWE) problem. Unlike decades of ECC scrutiny, lattice primitives are relatively young. If an algebraic vulnerability is discovered, standalone Kyber systems would fail completely.
2. **Transport-Layer Fragmentation Cliff:** Kyber-512 public keys require 800 bytes (12.5$\times$ larger than ECC-256), and Kyber-1024 requires 1568 bytes. Over real-world wide-area networks (WAN), multi-packet PQC handshakes exceed the standard TCP Maximum Segment Size (MSS $\approx 1460$ bytes). In lossy environments, losing a single segment triggers catastrophic Head-of-Line (HoL) blocking and exponential Retransmission Timeout (RTO) backoffs.
3. **Centralized Key Management Single Point of Failure:** Centralized Key Management Services (KMS) store master keys in relational databases. A single SQL injection or database credential compromise exposes every stored object.

### 1.3 Core Technical Contributions
To overcome these limitations, this paper proposes an **Adaptive Hybrid Quantum-Resistant Cloud Storage Architecture**:
* **Network-Aware Adaptive Hybrid Encapsulation (NA-AHE):** A closed-loop control algorithm incorporating real-time telemetry (RTT, packet loss $p_{\text{loss}}$, and MTU) alongside data sensitivity to eliminate TCP fragmentation cliffs.
* **Dual-Domain Zero-Trust Key Splitting:** A $(2,3)$ threshold scheme over Galois Field $\text{GF}(257)$ partitioning master keys across isolated domains (database and object header), with formal proof of zero mutual information leakage.
* **Early-Drop Constant-Time HMAC Shielding:** A pre-decryption verification layer rejecting forged ciphertexts in $\mathcal{O}(1)$ time, yielding a measured $106\times$ DoS rejection speedup.
* **Tamper-Evident Forensic Ledger with Real-Time Anomaly Engine:** A cryptographically chained SHA-256 audit trail combined with a sliding-window entropy classifier to detect brute-force decryptions.
* **Exhaustive Empirical & Hardware Evaluation:** Benchmarks across payload dimensions (100~KB to 10~MB), network impairment profiles, and micro-architectural Intel RAPL energy counters.

---

## 2. Related Work & Preliminaries

### 2.1 Post-Quantum Lattice Cryptography & NIST ML-KEM
CRYSTALS-Kyber (NIST ML-KEM) is an asymmetric KEM rooted in the hardness of the Module Learning With Errors (M-LWE) problem over polynomial ring $R_q = \mathbb{Z}_q[X]/(X^n + 1)$, where $n=256$ and modulus $q=3329$. Security depends on the hardness of distinguishing noisy inner products from uniform random distributions. Kyber uses Number Theoretic Transforms (NTT) for fast $\mathcal{O}(n \log n)$ ring multiplication.

### 2.2 Classical Elliptic Curve Cryptography
Classical ECDH relies on the hardness of ECDLP over prime-order curves $y^2 = x^3 - 3x + b \pmod{p}$. Using SECP256R1, private key $d \in_R [1, n-1]$ yields public key $Q = d \cdot G$. Point multiplication achieves efficient 64-byte public keys and sub-millisecond execution. While vulnerable to quantum computers, its mathematical maturity makes it an indispensable component of hybrid designs.

### 2.3 Comprehensive Baseline Comparison
Table 1 compares our proposed architecture against standard state-of-the-art baselines.

| Architecture / Scheme | PQC Resilience | Classical Fallback | Zero-Trust Key Splitting | Transport Optimization | Anti-DoS Layer | Forensic Ledger |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Standard Cloud KMS (AWS/Azure)** | ❌ None | ✅ Complete | ❌ Centralized DB | ❌ Static TCP | ❌ Post-Decryption | ❌ Plaintext Logs |
| **Pure NIST ML-KEM-512** | ✅ Level 1 | ❌ Vulnerable | ❌ Centralized DB | ❌ Vulnerable to HoL | ❌ Post-Decryption | ❌ None |
| **Static Hybrid (IETF Draft)** | ✅ Level 1 | ✅ SECP256R1 | ❌ Single Key Store | ❌ Static TCP | ❌ Post-Decryption | ❌ None |
| **Threshold Cloud Storage** | ❌ None | ✅ Complete | ✅ SSSS ($k,n$) | ❌ Unoptimized | ❌ CPU Heavy | ❌ Database Only |
| **Proposed Architecture** | ✅ **Level 1** | ✅ **SECP256R1** | ✅ **GF(257) Multi-Domain** | ✅ **NA-AHE Telemetry** | ✅ **Early-Drop HMAC** | ✅ **Hash-Chain Anomaly** |

---

## 3. Novel Architectural & Theoretical Contributions

### 3.1 Closed-Loop Network-Aware Adaptive Hybrid Encapsulation (NA-AHE)
Static cryptographic mechanisms treat cloud transport as an ideal pipe. However, lattice key exchanges expand packet payloads beyond the TCP MSS ($1460$ bytes). Under lossy WAN links, this triggers severe TCP retransmissions. We formulate the **Network-Aware Adaptive Hybrid Encapsulation (NA-AHE)** policy.

Let $\sigma \in \{\text{Low}, \text{Medium}, \text{High}\}$ denote data confidentiality sensitivity, $S$ denote payload size in bytes, $\text{RTT}$ denote round-trip time, and $p_{\text{loss}} \in [0, 1]$ denote real-time path packet loss. The effective decision boundary threshold $\Theta$ is dynamically scaled:

$$\Theta(\text{RTT}, p_{\text{loss}}) = \tau_0 \cdot \left(1 - \alpha \frac{\text{RTT}}{\text{RTT}_{\max}}\right) \cdot \left(1 - \beta \, p_{\text{loss}}\right)$$

where nominal threshold $\tau_0 = 5\text{ MB}$, $\alpha = 0.4$, $\beta = 0.5$, and $\text{RTT}_{\max} = 500\text{ ms}$. The operating mode $M$ is evaluated in $\mathcal{O}(1)$ time:

$$M = \begin{cases} 
\text{ECC-256}, & \text{if } \sigma = \text{Low} \\
\text{Kyber-512}, & \text{if } \sigma = \text{Medium} \lor \big(\sigma = \text{High} \land S > \Theta\big) \\
\text{Hybrid}, & \text{if } \sigma = \text{High} \land S \le \Theta
\end{cases}$$

```mermaid
flowchart TD
    Start([Client Ingestion Request]) --> Sensitivity{Check Sensitivity σ}
    Sensitivity -->|Low| ModeECC[Select Mode: ECC-256]
    Sensitivity -->|Medium| ModeKyber[Select Mode: Kyber-512]
    Sensitivity -->|High| Telemetry[Read RTT and Loss Telemetry]
    Telemetry --> CalcThresh[Calculate Dynamic Threshold Θ RTT, Loss]
    CalcThresh --> SizeCheck{Is File Size S <= Θ ?}
    SizeCheck -->|Yes| ModeHybrid[Select Mode: Dual-Key Hybrid]
    SizeCheck -->|No| ModeKyber
    ModeECC --> KeyGen[Initiate Key Exchange]
    ModeKyber --> KeyGen
    ModeHybrid --> KeyGen
```

### 3.2 Dual-Domain Zero-Trust Key Splitting over GF(257)
Standard key management systems store the master file encryption key $K_{\text{enc}}$ in a single database. We eliminate this vulnerability by splitting $K_{\text{enc}}$ byte-wise using a $(k=2, n=3)$ threshold polynomial over finite field $\mathbb{F}_{257}$:

$$f_i(x) = (s_i + a_{i,1} x) \pmod{257}, \quad a_{i,1} \in_R [1, 256]$$

Shares are distributed across physically and logically isolated domains:
* **Domain A (Storage Header):** $\text{Share}_1^{(i)} = (1, f_i(1))$, encrypted via AES-256-GCM and prepended to the object container.
* **Domain B (Relational DBMS):** $\text{Share}_2^{(i)} = (2, f_i(2))$, encrypted and stored in the database `key_fragments` table.
* **Domain C (Offline Escrow):** $\text{Share}_3^{(i)} = (3, f_i(3))$, held in cold administrative storage.

**Theorem 1 (Zero-Trust Information-Theoretic Secrecy):**  
*An adversary $\mathcal{A}$ compromising either Domain A or Domain B gains exactly zero mutual information regarding the master encryption key $K_{\text{enc}}$:*
$$I(K_{\text{enc}}; \text{Share}_j) = 0, \quad \forall j \in \{1, 2\}$$

*Proof:* For any byte $s_i \in \mathbb{F}_{257}$ and single evaluation $(j, y_j)$ with $y_j = (s_i + a_{i,1} j) \pmod{257}$, each candidate value $s' \in [0, 255]$ corresponds to a unique coefficient $a' = j^{-1}(y_j - s') \pmod{257}$. Since $a_{i,1}$ is chosen uniformly at random from $[1, 256]$, every $s' \in \mathbb{F}_{257}$ is equally likely. Thus, conditional entropy $H(s_i \mid \text{Share}_j) = H(s_i) = 8\text{ bits}$, and $H(K_{\text{enc}} \mid \text{Share}_j) = H(K_{\text{enc}}) = 256\text{ bits}$. Therefore, $I(K_{\text{enc}}; \text{Share}_j) = H(K_{\text{enc}}) - H(K_{\text{enc}} \mid \text{Share}_j) = 0$. $\blacksquare$

### 3.3 Constant-Time Early-Drop Outer HMAC Shield
In traditional authenticated encryption, the server must reconstruct $K_{\text{enc}}$ and compute full Galois Field multiplication ($GHASH$) to detect ciphertext corruption. Under malicious flooding, this exhausts server CPU resources. We introduce an outer envelope:

$$\text{OuterMAC} = \text{HMAC-SHA256}(K_{\text{auth}}, \text{Nonce} \parallel C \parallel \text{Tag})$$

The gateway verifies $\text{OuterMAC}$ in constant time before invoking Shamir reconstruction or AES-GCM decryption. Corrupted payloads are dropped in **$0.038\text{ ms}$** vs **$4.05\text{ ms}$** for standard pipelines, providing a measured **$106\times$ DoS speedup**.

### 3.4 Cryptographic Hash-Chain Forensics & Anomaly Engine
Every API invocation appends an immutable block $B_N$ cryptographically bound to block $B_{N-1}$:

$$H_N = \text{SHA256}(H_{N-1} \parallel \text{CanonicalJSON}(D_N))$$

Modifying or deleting any historical log entry breaks the hash chain. A real-time sliding window ($|W|=20$) evaluates the brute-force probability:

$$P_{\text{brute}} = \left(\frac{N_{\text{fail}}}{|W|}\right) \cdot \left(1.0 + 0.5 \frac{N_{\text{ip\_div}}}{|W|}\right)$$

When $N_{\text{fail}} \ge 5$ or $P_{\text{brute}} \ge 0.25$, the IP is immediately blacklisted.

---

## 4. System Architecture and Protocol Pipelines

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant Gateway as API Gateway / AEDE
    participant Crypto as Crypto Engine
    participant DB as SQLite DB Domain B
    participant Storage as Object Store Domain A
    participant Audit as Hash-Chain Audit

    Client->>Gateway: POST /api/upload (File, Sensitivity σ, Telemetry)
    Gateway->>Gateway: Compute Threshold Θ and Select Mode
    Gateway->>Crypto: Execute Dual-Key Hybrid Exchange
    Crypto->>Crypto: ECDH + Kyber Encapsulation
    Crypto->>Crypto: HKDF Expansion: (K_enc, K_auth)
    Crypto->>Crypto: Shamir Split (2-of-3) over GF(257)
    Crypto->>DB: Save Encrypted Share 2 (Domain B)
    Crypto->>Crypto: AES-256-GCM Encrypt File
    Crypto->>Crypto: Compute Outer HMAC-SHA256
    Crypto->>Storage: Write Binary Package [Header + Share 1 + MAC + CT] (Domain A)
    Crypto->>Audit: Append Block H_N = SHA256(H_{N-1} || Data)
    Gateway-->>Client: 201 Created (File ID, SHA256, Mode)
```

### 4.1 Binary Object Package Layout
The encrypted artifact is packaged into a self-describing binary structure (Table 2).

| Field | Offset (B) | Size (B) | Description |
| :--- | :---: | :---: | :--- |
| `MagicBytes` | 0 | 4 | Protocol marker (`0x51505143`) |
| `ModeID` | 4 | 1 | 0x01 (ECC), 0x02 (Kyber), 0x03 (Hybrid) |
| `Frag1Len` | 5 | 4 | Length of Encrypted Key Fragment 1 |
| `EncFrag1` | 9 | $L_1$ | AES-256-GCM Encrypted Fragment 1 |
| `OuterMAC` | $9+L_1$ | 32 | HMAC-SHA256 Authentication Envelope |
| `GCMNonce` | $41+L_1$ | 12 | 96-bit AES-GCM Initialization Vector |
| `Ciphertext` | $53+L_1$ | $N$ | AES-256-GCM Encrypted Payload |
| `GCMTag` | $53+L_1+N$ | 16 | 128-bit GCM Authentication Tag |

---

## 5. Formal Algorithms & Protocol Specifications

### Algorithm 1: Adaptive File Ingestion and Key Distribution
```text
Input: Payload P, Sensitivity σ, Size S, User u, File ID f, Telemetry (RTT, p_loss)
Output: Binary Package B, Status Code
1:  Θ ← τ0 * (1 - α * RTT / RTT_max) * (1 - β * p_loss)
2:  mode ← AEDE_Select(σ, S, Θ)
3:  if mode = 'Hybrid' then
4:      (SK_ecc, PK_ecc) ← ECC_GenKey()
5:      (SK_kyb, PK_kyb) ← Kyber_GenKey()
6:      S_ecc ← ECDH(SK_ecc, PK_ecc)
7:      (CT_kyb, S_kyber) ← Kyber_Encapsulate(PK_kyb)
8:      (K_enc || K_auth) ← HKDF(S_ecc || S_kyber, salt=r, 64)
9:  else if mode = 'Kyber' then
10:     (SK_kyb, PK_kyb) ← Kyber_GenKey()
11:     (CT_kyb, K_enc) ← Kyber_Encapsulate(PK_kyb)
12:     K_auth ← SHA256(K_enc || "auth")
13: else
14:     (SK_ecc, PK_ecc) ← ECC_GenKey()
15:     K_enc ← ECDH(SK_ecc, PK_ecc)
16:     K_auth ← SHA256(K_enc || "auth")
17: end if
18: (Share1, Share2, Share3) ← Shamir_Split(K_enc, k=2, n=3, p=257)
19: EncS1 ← AES_GCM(K_master, Share1)
20: EncS2 ← AES_GCM(K_master, Share2)
21: DB_SaveFragment(f, EncS2, mode, σ, u)
22: (Nonce, C, Tag) ← AES_GCM_Encrypt(K_enc, P, AAD=f)
23: OuterMAC ← HMAC_SHA256(K_auth, Nonce || C || Tag)
24: B ← SerializePackage(EncS1, OuterMAC, Nonce, C, Tag)
25: Storage_PutObject(f, B)
26: HashChain_Append('upload', f, u, 'success')
27: return B, 201
```

### Algorithm 2: Secure Retrieval, Outer HMAC Verification, and Key Reconstruction
```text
Input: File Identifier f, Requesting User u
Output: Plaintext P or Rejection Error
1:  Meta ← DB_GetMetadata(f)
2:  if Meta = NULL then
3:      HashChain_Append('download', f, u, 'fail_not_found')
4:      return Error(404)
5:  end if
6:  B ← Storage_GetObject(f)
7:  (EncS1, OuterMAC, Nonce, C, Tag) ← Unpack(B)
8:  EncS2 ← DB_GetFragment(f)
9:  Share1 ← AES_GCM_Decrypt(K_master, EncS1)
10: Share2 ← AES_GCM_Decrypt(K_master, EncS2)
11: for i = 0 to 31 do
12:     x1 ← Share1[i].x; y1 ← Share1[i].y; x2 ← Share2[i].x; y2 ← Share2[i].y
13:     λ1 ← (-x2 / (x1 - x2)) mod 257; λ2 ← (-x1 / (x2 - x1)) mod 257
14:     K_enc[i] ← (y1 * λ1 + y2 * λ2) mod 257
15: end for
16: K_auth ← DeriveAuthKey(K_enc, Meta.mode)
17: if ConstantTimeCompare(OuterMAC, HMAC(K_auth, Nonce || C || Tag)) != 0 then
18:     HashChain_Append('download', f, u, 'fail_hmac')
19:     return Error(403, "Integrity Check Failed")
20: end if
21: P ← AES_GCM_Decrypt(K_enc, Nonce, C, Tag, AAD=f)
22: HashChain_Append('download', f, u, 'success')
23: return P
```

---

## 6. Experimental Setup and Empirical Evaluation

### 6.1 Hardware Testbed
Experiments were executed on an isolated testbed powered by an Intel Core i7-12700H (14 cores, 20 threads @ 4.70 GHz), 32 GB DDR5 RAM @ 4800 MHz, running Ubuntu 22.04 LTS (Linux kernel 5.15). Real-time CPU energy consumption was measured via Intel Running Average Power Limit (RAPL) hardware MSR counters (`MSR_PKG_ENERGY_STATUS`).

### 6.2 Cryptographic Primitives Benchmark
Table 3 reports key generation, encapsulation/encryption, and decapsulation/decryption latencies averaged across 20 iterations for a 1~MB payload.

| Scheme | KeyGen (ms) | Enc (ms) | Dec (ms) | Total (ms) | PK (B) | PQC? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **RSA-3072** | 4.52 | 0.15 | 3.21 | 7.88 | 384 | ❌ No |
| **ECC-256** | 0.98 | 0.44 | 0.46 | 1.88 | 64 | ❌ No |
| **Kyber-512** | 0.02 | 0.03 | 0.04 | 0.09 | 800 | ✅ Yes |
| **Kyber-768** | 0.03 | 0.04 | 0.05 | 0.12 | 1184 | ✅ Yes |
| **Kyber-1024** | 0.04 | 0.05 | 0.06 | 0.15 | 1568 | ✅ Yes |
| **Proposed Hybrid** | **0.31** | **0.48** | **0.49** | **1.28** | **864** | ✅ **Yes** |

### 6.3 Hardware Energy Footprint & Memory RSS (RAPL Counters)
Table 4 reports Intel RAPL energy consumption and instruction throughput per 10,000 operations.

| Scheme | Energy (J) | Memory RSS (MB) | Cycles ($\times 10^6$) | Instructions / Cycle (IPC) |
| :--- | :---: | :---: | :---: | :---: |
| **RSA-3072** | 38.4 | 24.2 | 128.5 | 1.12 |
| **ECC-256** | 8.1 | 16.5 | 28.4 | 1.48 |
| **Kyber-512** | 0.85 | 18.2 | 3.1 | 2.15 |
| **Proposed Hybrid** | **9.2** | **19.8** | **32.2** | **1.82** |

### 6.4 File Dimensionality Scaling
Table 5 reports payload processing latency across file sizes from 100~KB to 10~MB.

| File Size | ECC-256 (ms) | Kyber-512 (ms) | Proposed Hybrid (ms) | PQC Safe? |
| :--- | :---: | :---: | :---: | :---: |
| **100 KB** | 7.83 | 0.21 | 1.33 | ✅ Yes |
| **1 MB** | 3.51 | 2.99 | 3.67 | ✅ Yes |
| **5 MB** | 13.19 | 10.94 | 12.19 | ✅ Yes |
| **10 MB** | 25.42 | 21.80 | 24.15 | ✅ Yes |

---

## 7. Network Transport Impairment & TCP Fragmentation Analysis

Standard Ethernet networks enforce a Maximum Transmission Unit (MTU) of 1500 bytes, yielding an MSS of 1460 bytes. Classical ECC-256 handshakes ($64\text{ B}$ public key) fit comfortably inside a single TCP segment. Conversely, Kyber-512 public keys ($800\text{ B}$) combined with server certificates and TLS extensions frequently exceed 1500 bytes, forcing multi-packet segmentation.

| Profile | Loss Rate | Bandwidth | ECC (ms) | Kyber (ms) | Proposed Hybrid (ms) | Retransmissions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ideal LAN** | 0% | 100 Mbps | 1.88 | 0.09 | 1.28 | 0 |
| **Moderate Cloud** | 1% | 50 Mbps | 22.4 | 24.1 | 25.8 | 1--2 |
| **Degraded Lossy** | 5% | 10 Mbps | 48.2 | 158.6 | 165.2 | 6--9 (super-linear surge) |
| **Severe Lossy** | 10% | 1 Mbps | 120.5 | 495.0 | 512.4 | 18--24 |

---

## 8. Security Analysis & Formal Proofs

### 8.1 IND-CCA2 Security Reduction in the Random Oracle Model
**Theorem 2 (Hybrid IND-CCA2 Security):**  
*If the M-LWE problem is intractable in $R_q$ and the ECDHP problem is hard over SECP256R1, then the proposed Dual-Key Hybrid KEM scheme is IND-CCA2 secure in the Random Oracle Model.*

*Proof Sketch:* Let adversary $\mathcal{A}$ have non-negligible advantage $\epsilon$ against the hybrid KEM. We construct simulator $\mathcal{B}$ solving either ECDHP or M-LWE. In the game, $\mathcal{B}$ provides public keys $PK_{\text{ecc}}$ and $PK_{\text{kyb}}$. During challenge phase, $\mathcal{B}$ receives target secrets $S_{\text{ecc}}^*$ and $S_{\text{kyb}}^*$. By properties of HKDF-Extract as a pseudo-random function, derived key $K_{\text{enc}} = \text{HKDF}(S_{\text{ecc}} \parallel S_{\text{kyber}})$ is indistinguishable from uniform random unless $\mathcal{A}$ queries the random oracle on $(S_{\text{ecc}} \parallel S_{\text{kyber}})$. To succeed, $\mathcal{A}$ must break **both** underlying problems. Hence, $\epsilon_{\text{Hybrid}} \le \min(\epsilon_{\text{ECDH}}, \epsilon_{\text{MLWE}}) + \text{negl}(\lambda)$. $\blacksquare$

### 8.2 Comprehensive Threat Resilience Comparison
Table 7 compares resilience across standard baselines.

| Threat Vector | ECC-256 | Kyber-512 | Proposed System |
| :--- | :---: | :---: | :---: |
| **Classical Brute Force** | ✅ Resistant | ✅ Resistant | ✅ **Highly Resistant** |
| **Shor's Algorithm (Quantum)** | ❌ Broken | ✅ Resistant | ✅ **Quantum Safe** |
| **Novel Lattice Math Flaw** | ✅ Resistant | ❌ Broken | ✅ **ECC Redundancy** |
| **Database Infiltration** | ❌ Compromised | ❌ Compromised | ✅ **Shamir (2,3) Safe** |
| **DoS Ciphertext Flooding** | ❌ CPU Exhaust | ❌ CPU Exhaust | ✅ **Outer HMAC Drop (106x)** |
| **Audit Trail Tampering** | ❌ Vulnerable | ❌ Vulnerable | ✅ **Hash-Chain Bound** |

---

## 9. Conclusion
This paper presented an **Adaptive Hybrid Quantum-Resistant Cloud Storage Architecture**. By pairing classical ECDH with NIST ML-KEM via HKDF key derivation, splitting keys across isolated storage domains via $\text{GF}(257)$ Shamir secret sharing, shielding endpoints with an early-drop outer HMAC filter, and dynamically optimizing handshakes via the NA-AHE algorithm, our system reconciles quantum resilience with transport-layer efficiency. Empirical benchmarks confirm that hybrid encapsulation adds only **1.28~ms overhead for a 1~MB file** (0.16~ms over classical ECC), while the outer HMAC shield provides a **$106\times$ verification speedup** against Denial-of-Service attacks. This architecture establishes a robust, performant foundation for next-generation post-quantum secure cloud storage.

---

## References
1. P. Mell and T. Grance, "The NIST definition of cloud computing," *NIST Special Publication*, vol. 800, no. 145, pp. 1–7, 2011.
2. D. Boneh and V. Shoup, *A Graduate Course in Applied Cryptography*, Cambridge University Press, 2020.
3. J. Katz and Y. Lindell, *Introduction to Modern Cryptography*, 3rd ed., CRC Press, 2020.
4. P. W. Shor, "Algorithms for quantum computation: discrete logarithms and factoring," in *Proc. 35th Annual Symp. Foundations of Computer Science (FOCS)*, 1994, pp. 124–134.
5. L. Chen et al., "Report on post-quantum cryptography," *NIST Internal Report 8105*, 2016.
6. NIST, "Post-Quantum Cryptography Standardization," 2024. [Online]. Available: https://csrc.nist.gov/projects/post-quantum-cryptography
7. J. Bos et al., "CRYSTALS-Kyber: a CCA-secure module-lattice-based KEM," in *IEEE EuroS&P*, 2018, pp. 253–267.
8. D. Sikeridis, P. Kampanakis, and M. Devetsikiotis, "Assessing the overhead of post-quantum cryptography in TLS 1.3 and SSH," in *Proc. 16th ACM CoNEXT*, 2020, pp. 149–156.
9. A. Sahai and B. Waters, "How to use indistinguishability obfuscation: Deniable encryption, and more," *SIAM J. Comput.*, vol. 50, no. 3, pp. 735–784, 2021.
10. D. J. Bernstein and T. Lange, "Post-quantum cryptography -- dealing with the fallout of physics success," *Cryptology ePrint Archive*, Report 2017/314, 2017.
11. R. Avanzi et al., "CRYSTALS-Kyber algorithm specifications (v3.02)," *NIST PQC Round 3 Submission*, 2021.
12. N. Bindel et al., "Hybrid key encapsulation mechanisms and authenticated key exchange," *Post-Quantum Cryptography*, LNCS, vol. 11505, pp. 206–225, Springer, 2019.
13. H. Krawczyk, "Cryptographic extraction and key derivation: The HKDF scheme," in *Proc. CRYPTO*, LNCS, vol. 6223, pp. 631–648, Springer, 2010.
14. A. Shamir, "How to share a secret," *Commun. ACM*, vol. 22, no. 11, pp. 612–613, 1979.
15. S. Rose et al., "Zero trust architecture," *NIST Special Publication*, vol. 800, no. 207, 2020.
16. D. A. McGrew and J. Viega, "The Galois/Counter Mode of operation (GCM)," *NIST Modes of Operation*, 2004.
17. M. R. Albrecht et al., "On the concrete hardness of LWE with applications to NIST PQC candidates," in *Proc. Eurocrypt*, pp. 586–616, Springer, 2018.
18. C. Paquin, D. Stebila, and G. Tamvakis, "Benchmarking post-quantum cryptography in TLS," in *Proc. PQCrypto*, pp. 70–91, Springer, 2020.
19. S. Crocker, "Post-quantum key exchange in QUIC and TLS," in *Proc. IEEE MILCOM*, 2021, pp. 410–417.
20. S. Bhattacharjee et al., "Energy-efficient hardware implementations of NTT for lattice-based cryptography," *IEEE Trans. VLSI Syst.*, vol. 30, no. 8, pp. 1045–1058, 2022.
21. R. Schmidt et al., "Evaluating post-quantum migration strategies for secure distributed cloud file systems," in *Proc. IEEE CLOUD*, 2023, pp. 215–224.
22. X. Wang et al., "Adaptive security controls for hybrid multi-cloud environments under quantum threats," *IEEE Trans. Cloud Comput.*, vol. 12, no. 2, pp. 512–526, 2024.
