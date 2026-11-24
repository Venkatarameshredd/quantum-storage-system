# Quantum-Resistant Adaptive Hybrid Cloud Storage (QHCS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10894215.svg)](https://doi.org/10.5281/zenodo.10894215)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-brightgreen.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](tests/)

> **Reference Implementation & Open Science Research Artifact**  
> **Authors:** Varsha Sambhaje (Corresponding Author), Madhira Venkata Ramesh Reddy  
> **Affiliation:** Department of Computer Science and Engineering, SRM University-AP, Amaravati, India  
> **Paper Title:** *Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms*

---

## 📌 Executive Architecture Overview

This repository provides the reference implementation of the **Quantum-Resistant Adaptive Hybrid Cloud Storage System (QHCS)**. Designed to repel active **Harvest Now, Decrypt Later (HNDL)** attacks without incurring prohibitive cloud computing penalties, the architecture synthesizes five defense pillars:

```text
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
   ├── Share 2: Encrypted in Relational Database (Storage Domain B: SQLite/PostgreSQL)
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
```

---

## 📊 Data & Code Availability

- **Permanent Data DOI:** [https://doi.org/10.5281/zenodo.10894215](https://doi.org/10.5281/zenodo.10894215)
- **Source Code Repository:** [https://github.com/Venkatarameshredd/quantum-storage-system](https://github.com/Venkatarameshredd/quantum-storage-system)
- **Container Specification:** `Dockerfile` & `docker-compose.yml` included in root

---

## 🚀 Quickstart & Installation

### Option 1: Local Python Environment

```bash
# 1. Clone repository
git clone https://github.com/Venkatarameshredd/quantum-storage-system.git
cd quantum-storage-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Flask API gateway
python app.py
```

The REST API will be active at `http://127.0.0.1:5000`.

### Option 2: Docker / Docker Compose

```bash
docker-compose up --build
```

---

## 🧪 Verification & Empirical Benchmarking

### 1. Run Automated Test Suite

```bash
python -m unittest discover -s tests
```

Validates the AEDE engine, Shamir GF(257) rejection sampling, hybrid key exchange, Early-Drop filter, and hash-chain audit ledger (10/10 tests pass).

### 2. Simulate Attack & DoS Early-Drop Mitigation

```bash
python simulate_attack.py
```

Simulates:
- Legitimate upload and 2-of-3 Lagrange key reconstruction.
- Malicious DoS burst of 50 forged requests demonstrating socket-boundary rejection in **0.089 ms**.
- Automated Bayesian anomaly triggering and tamper-evident audit ledger verification.

### 3. Export Complete Dataset for Zenodo Archival

```bash
python export_complete_dataset.py
```

Generates clean CSV and JSON datasets across all payload sizes (100 KB, 1 MB, 5 MB, 10 MB).

---

## 📁 Repository Directory Structure

```text
quantum-storage-system/
├── app.py                      # Flask REST API Gateway & Ingress/Egress Controller
├── simulate_attack.py          # Automated DoS Attack & Defense Simulator
├── export_complete_dataset.py  # Dataset Exporter for Zenodo Archival
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build specification
├── docker-compose.yml          # Microservice deployment topology
├── LICENSE                     # Apache-2.0 License
├── README.md                   # Repository documentation & DOI links
├── .gitignore                  # Environment, cache, and database exclusion rules
│
├── crypto/                     # Cryptographic Core Modules
│   ├── adaptive_engine.py      # Adaptive Encryption Decision Engine (AEDE)
│   ├── aes_gcm.py              # Hardware AES-256-GCM payload encryption
│   ├── ecc.py                  # SECP256R1 ECDH Key Exchange
│   ├── hmac_verify.py          # Outer HMAC-SHA256 Boundary Filter (Early-Drop)
│   ├── hybrid.py               # Dual-Key Hybrid Combiner (HKDF-SHA256)
│   ├── kyber.py                # NIST ML-KEM-512 (800B pk, 768B ct, 32B ss)
│   └── ntt.py                  # Vectorized NTT Modular Butterfly Reduction (R_3329^256)
│
├── security/                   # Zero-Trust, Forensics & Formal Verification
│   ├── key_split.py            # Shamir (2,3) Secret Sharing & Key Rotation over GF(257)
│   ├── secure_logs.py          # Hash-Chain Ledger & Bayesian Anomaly Classifier
│   └── proverif_model.pv       # ProVerif Applied pi-Calculus Formal Verification Model
│
├── database/                   # Metadata & fragment database connectors (SQLite)
│   └── db.py
│
├── storage/                    # Cloud object store interface (Local / MinIO / S3)
│   └── minio_client.py
│
├── benchmark/                  # Microbenchmark suites
│   └── benchmark.py
│
├── dataset/                    # Empirical data logs & CSV exports
│   ├── README.md
│   ├── benchmark_results.csv
│   ├── complete_dataset/
│   └── sample_files/
│
├── templates/                  # Frontend User Interface
│   └── index.html
│
└── tests/                      # System Test Suite (10/10 tests validating Algs 1-7)
    └── test_system.py
```

---

## 📜 Citation

If you use this codebase or reference our architecture in your research, please cite our Q1 journal article:

```bibtex
@article{sambhaje2026quantum,
  author    = {Varsha Sambhaje and Madhira Venkata Ramesh Reddy},
  title     = {Quantum-Resistant Adaptive Hybrid Cloud Storage: A Multi-Layered Defense Architecture Integrating Lattice-Based Key Encapsulation, Threshold Secret Sharing, and Tamper-Evident Audit Mechanisms},
  journal   = {Journal of Cloud Computing: Advances, Systems and Logistics},
  publisher = {Springer Nature},
  year      = {2026},
  doi       = {10.5281/zenodo.10894215}
}
```
