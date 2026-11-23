# Quantum-Resistant Adaptive Hybrid Cloud Storage (QHCS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10894215.svg)](https://doi.org/10.5281/zenodo.10894215)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-brightgreen.svg)](https://www.python.org/)
[![Target Journal](https://img.shields.io/badge/Journal-Springer%20Nature%20(Q1)-orange.svg)](manuscripts_and_papers/springer_q1_journal_36pages/)

> **Reference Implementation & Open Science Research Artifact**  
> **Authors:** Varsha Sambhaje (Corresponding Author), Madhira Venkata Ramesh Reddy  
> **Affiliation:** Department of Computer Science and Engineering, SRM University-AP, Amaravati, India  
> **Paper Title:** *Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms*

---

## 📌 Executive Architecture Overview

This repository provides the reference implementation of the **Quantum-Resistant Adaptive Hybrid Cloud Storage System (QHCS)**. Designed to repel active **Harvest Now, Decrypt Later (HNDL)** attacks without incurring prohibitive cloud computing penalties, the architecture synthesizes five defense pillars:

`
[ Ingress Payload ] 
        │
        ▼
1. 🛡️ Adaptive Encryption Decision Engine (AEDE)
   ├── Mode 1: Classical ECC-256 (Low Sensitivity, Fast)
   ├── Mode 2: Pure CRYSTALS-Kyber-512 (Medium Sensitivity / Bulk)
   └── Mode 3: Dual-Key Hybrid (SECP256R1 + Kyber-512 via HKDF-SHA256)
        │
        ▼
2. 🔑 Zero-Trust Shamir (2,3)-Threshold Key Distribution over GF(257)
   ├── Share 1: Embedded into Object Container Header (Storage Domain A: S3/MinIO)
   ├── Share 2: Encrypted in Relational Database (Storage Domain B: PostgreSQL)
   └── Share 3: Stored in Air-Gapped Cold HSM (Storage Domain C: Disaster Recovery)
   └── Guarantee: Shannon Mutual Information I(K_master; Share_i) = 0
        │
        ▼
3. ⚡ Early-Drop Outer HMAC-SHA256 Boundary Filter
   ├── Intercepts and validates header authentication envelope in 0.089 ms
   └── 12.3x Rejection Speedup, keeping CPU load below 8.8% under 10k req/s floods
        │
        ▼
4. 📜 Immutable Hash-Chain Audit Ledger & Sliding-Window Bayesian Anomaly Engine
   ├── Cryptographic linkage: H_i = SHA-256(H_{i-1} || Action || FileID || Timestamp)
   └── Real-time anomaly classification flagging >= 5 failed attempts
`

---

## 📊 Data & Code Availability

- **Permanent Data DOI:** [https://doi.org/10.5281/zenodo.10894215](https://doi.org/10.5281/zenodo.10894215)
- **Source Code Repository:** [https://github.com/quantum-storage-lab/quantum-hybrid-cloud-storage](https://github.com/quantum-storage-lab/quantum-hybrid-cloud-storage)
- **Container Registry:** ghcr.io/quantum-storage/eval-testbed:v1.0
- **Full 36-Page Camera-Ready Manuscript:** Located in [manuscripts_and_papers/springer_q1_journal_36pages/SPRINGER_Q1_JOURNAL_30PAGES.pdf](manuscripts_and_papers/springer_q1_journal_36pages/SPRINGER_Q1_JOURNAL_30PAGES.pdf)

---

## 🚀 Quickstart & Installation

### Option 1: Local Python Environment
`ash
# 1. Clone repository
git clone https://github.com/quantum-storage-lab/quantum-hybrid-cloud-storage.git
cd quantum-hybrid-cloud-storage

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Flask API gateway
python app.py
`
The REST API will be active at http://127.0.0.1:5000.

### Option 2: Docker / Docker Compose
`ash
docker-compose up --build
`

---

## 🧪 Verification & Empirical Benchmarking

### 1. Run Automated Test Suite
`ash
python -m unittest discover -s tests
`
Validates the AEDE engine, Shamir GF(257) rejection sampling, hybrid key exchange, Early-Drop filter, and hash-chain audit ledger.

### 2. Simulate Attack & DoS Early-Drop Mitigation
`ash
python simulate_attack.py
`
Simulates:
- Legitimate upload and 2-of-3 Lagrange key reconstruction.
- Malicious DoS burst of 50 forged requests demonstrating socket-boundary rejection in **0.089 ms**.
- Automated Bayesian anomaly triggering and tamper-evident audit ledger verification.

### 3. Export Complete Dataset for Zenodo Archival
`ash
python export_complete_dataset.py
`
Generates clean CSV and JSON datasets across all payload sizes (100 KB, 1 MB, 5 MB, 10 MB).

---

## 📁 Repository Directory Structure

`
├── app.py                      # Flask REST API Gateway & Ingress/Egress Controller
├── simulate_attack.py          # Automated DoS Attack & Defense Simulator
├── export_complete_dataset.py  # Dataset Exporter for Zenodo Archival
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build specification
├── docker-compose.yml          # Microservice deployment topology
├── LICENSE                     # Apache-2.0 License
├── README.md                   # Repository documentation & DOI links
├── crypto/                     # Cryptographic core modules
│   ├── adaptive_engine.py      # Adaptive Encryption Decision Engine (AEDE, Fig. 3, Eq. 1)
│   ├── aes_gcm.py              # Hardware AES-256-GCM payload encryption
│   ├── ecc.py                  # SECP256R1 ECDH Key Exchange
│   ├── hmac_verify.py          # Outer HMAC-SHA256 Boundary Filter (0.089 ms Early-Drop)
│   ├── hybrid.py               # Dual-Key Hybrid Combiner (HKDF-SHA256, Fig. 4)
│   ├── kyber.py                # NIST ML-KEM-512 (800B pk, 768B ct, 32B ss, Tables 2 & 5)
│   └── ntt.py                  # Algorithm 7: Vectorized NTT Modular Butterfly Reduction (R_3329^256)
├── security/                   # Zero-Trust, Forensics & Formal Verification
│   ├── key_split.py            # Shamir (2,3) Secret Sharing & Alg. 5 Key Rotation over GF(257)
│   ├── secure_logs.py          # Alg. 3 Hash-Chain Ledger & Alg. 6 Bayesian Anomaly Classifier
│   └── proverif_model.pv       # ProVerif 2.05 Applied pi-Calculus Formal Verification Model
├── database/                   # Metadata & fragment database connectors (SQLite)
├── storage/                    # Cloud object store interface (Local / MinIO / S3)
├── benchmark/                  # Microbenchmark suites
├── dataset/                    # Empirical data logs & CSV exports
├── tests/                      # Exhaustive test suite (10/10 tests validating Algs 1-7)
└── manuscripts_and_papers/     # Camera-ready journal & conference manuscripts
    ├── springer_q1_journal_36pages/  # 36-page Q1 Journal Manuscript, LaTeX & BibTeX
    ├── ieee_conference_paper_6pages/ # 6-page IEEE Conference Paper & Overleaf Zip
    └── other_papers_and_reports/     # Technical reports and documentation
`

---

## 📜 Citation

If you use this codebase or reference our architecture in your research, please cite our Q1 journal article:

`ibtex
@article{sambhaje2026quantum,
  author    = {Varsha Sambhaje and Madhira Venkata Ramesh Reddy},
  title     = {Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms},
  journal   = {Journal of Cloud Computing: Advances, Systems and Logistics},
  publisher = {Springer Nature},
  year      = {2026},
  doi       = {10.5281/zenodo.10894215}
}
`
