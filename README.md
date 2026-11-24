# Quantum-Resistant Adaptive Hybrid Cloud Storage (QHCS)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-brightgreen.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/tests-10%2F10%20passing-brightgreen.svg)](tests/)

A robust, production-ready reference implementation of the **Quantum-Resistant Adaptive Hybrid Cloud Storage (QHCS)** platform. Engineered to defend sensitive data against **Harvest Now, Decrypt Later (HNDL)** quantum adversary threats without sacrificing cloud throughput or inflating compute costs.

---

## 📌 Architecture Overview

```text
[ Ingress Payload ] 
        │
        ▼
1. 🛡️ Adaptive Encryption Decision Engine (AEDE)
   ├── Mode 1: Classical ECC-256 (Low Sensitivity, High Throughput)
   ├── Mode 2: Pure CRYSTALS-Kyber-512 (Post-Quantum Lattice KEM)
   └── Mode 3: Dual-Key Hybrid (SECP256R1 + Kyber-512 via HKDF-SHA256)
        │
        ▼
2. 🔑 Zero-Trust Shamir (2,3)-Threshold Key Distribution over GF(257)
   ├── Share 1: Embedded in Object Header (Storage Domain A)
   ├── Share 2: Stored in Relational Metadata Database (Storage Domain B)
   └── Share 3: Escrowed in Offline Disaster Recovery Vault (Storage Domain C)
        │
        ▼
3. ⚡ Early-Drop Outer HMAC-SHA256 Boundary Filter
   ├── Socket-boundary verification rejecting unauthorized bursts in < 0.1 ms
   └── Protects downstream decryption pipelines from CPU exhaustion attacks
        │
        ▼
4. 📜 Immutable Hash-Chain Audit Ledger & Anomaly Detection
   ├── Tamper-evident cryptographic ledger: H_i = SHA-256(H_{i-1} || Action || FileID || Timestamp)
   └── Sliding-window anomaly detection for intrusion prevention
```

---

## 📁 Repository Directory Structure

```text
quantum-storage-system/
├── benchmark/                  # Benchmark scripts and test measurements
│   └── benchmark.py
├── crypto/                     # Cryptographic core modules
│   ├── adaptive_engine.py      # Adaptive Encryption Decision Engine (AEDE)
│   ├── aes_gcm.py              # Hardware AES-256-GCM payload encryption
│   ├── ecc.py                  # SECP256R1 ECDH Key Exchange
│   ├── hmac_verify.py          # Outer HMAC-SHA256 Boundary Filter (Early-Drop)
│   ├── hybrid.py               # Dual-Key Hybrid Combiner (HKDF-SHA256)
│   ├── kyber.py                # NIST ML-KEM-512 Lattice Implementation
│   └── ntt.py                  # Vectorized Number Theoretic Transform (NTT)
├── database/                   # Database connectors and schema (SQLite)
│   └── db.py
├── dataset/                    # Empirical data logs & CSV exports
│   ├── README.md
│   ├── benchmark_results.csv
│   ├── complete_dataset/
│   └── sample_files/
├── security/                   # Zero-Trust & Forensics
│   ├── key_split.py            # Shamir (2,3) Secret Sharing over GF(257)
│   ├── proverif_model.pv       # Formal Security Verification Model
│   └── secure_logs.py          # Hash-Chain Ledger & Anomaly Detection
├── storage/                    # Cloud object store interface (MinIO / S3)
│   └── minio_client.py
├── templates/                  # Web dashboard UI
│   └── index.html
├── tests/                      # Automated test suite (10/10 passing)
│   └── test_system.py
├── .gitignore                  # Git exclusion rules
├── Dockerfile                  # Container build specification
├── LICENSE                     # Apache-2.0 License
├── README.md                   # Project documentation
├── app.py                      # Flask REST API Gateway & Web Interface
├── docker-compose.yml          # Container orchestration configuration
├── export_complete_dataset.py  # Dataset generator and exporter
├── requirements.txt            # Python dependencies
└── simulate_attack.py          # DoS attack & Early-Drop defense simulator
```

---

## 🚀 Quickstart & Installation

### Option 1: Local Python Environment

```bash
# 1. Clone the repository
git clone https://github.com/Venkatarameshredd/quantum-storage-system.git
cd quantum-storage-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Flask API Gateway & Web UI
python app.py
```

Access the web dashboard and REST API at `http://127.0.0.1:5000`.

### Option 2: Docker / Docker Compose

```bash
docker-compose up --build
```

---

## 🧪 Verification & Benchmarking

### 1. Run Automated Test Suite
```bash
python -m unittest discover -s tests
```
Executes the full test suite validating cryptographic engines, key splitting, Early-Drop filters, and hash chains (10/10 tests pass).

### 2. Simulate Attack & Early-Drop Mitigation
```bash
python simulate_attack.py
```
Simulates:
- Authorized file encryption, threshold share distribution, and 2-of-3 reconstruction.
- Rapid burst of 50 unauthorized requests rejected at the socket boundary.
- Real-time audit log chaining and anomaly event detection.

### 3. Generate Benchmark Datasets
```bash
python export_complete_dataset.py
```
Exports comprehensive performance evaluation datasets across all payload sizes (100 KB, 1 MB, 5 MB, 10 MB).

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
