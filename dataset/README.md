# Quantum-Resistant Adaptive Hybrid Storage Dataset

This folder contains benchmark empirical datasets and test payloads categorized by security sensitivity levels for evaluating the Quantum-Resistant Adaptive Hybrid Encryption Storage system.

## Structure

```text
dataset/
├── benchmark_results.csv         # Comparative cryptographic metrics (RSA, ECC, Kyber, Hybrid)
├── README.md                     # Dataset documentation
└── sample_files/                 # Test payloads categorized by sensitivity
    ├── confidential_financial_report.csv  # High sensitivity (Hybrid ECC+Kyber)
    ├── patient_health_records.json        # High sensitivity (Hybrid ECC+Kyber)
    ├── system_config.xml                  # Medium sensitivity (Kyber-512)
    └── public_readme.txt                  # Low sensitivity (ECC-256)
```

## Dataset Description

1. **`benchmark_results.csv`**: Contains cryptographic benchmark measurements (Key Generation latency, Encryption overhead, Key sizes, Ciphertext expansion) comparing classical and post-quantum cryptographic schemes.
2. **`sample_files/`**: Standard test files used to demonstrate uploading and encrypting files through the web interface (`/api/upload`) across different sensitivity tiers.
