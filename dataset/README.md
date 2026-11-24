# Quantum-Resistant Adaptive Hybrid Storage Dataset

This folder contains empirical benchmark datasets and test payloads categorized by security sensitivity levels for evaluating the Quantum-Resistant Adaptive Hybrid Encryption Storage system.

## Structure

```text
dataset/
├── README.md                          # Dataset documentation
├── benchmark_results.csv              # Cryptographic performance metrics (RSA, ECC, Kyber, Hybrid)
├── complete_dataset/                  # Comprehensive evaluation benchmarks (thousands of samples)
│   ├── benchmark_results.csv          # Extended latency & throughput data
│   ├── files_metadata.csv             # Ingested object metadata catalog (CSV)
│   └── files_metadata.json            # Ingested object metadata catalog (JSON)
└── sample_files/                      # Test payloads categorized by sensitivity
    ├── confidential_financial_report.csv  # High sensitivity (Dual-Key Hybrid SECP256R1 + Kyber-512)
    ├── patient_health_records.json        # High sensitivity (Dual-Key Hybrid SECP256R1 + Kyber-512)
    └── system_config.xml                  # Medium sensitivity (Pure Kyber-512)
```

## Dataset Description

1. **`benchmark_results.csv`**: Contains cryptographic benchmark measurements (Key Generation latency, Encryption overhead, Key sizes, Ciphertext expansion) comparing classical and post-quantum cryptographic schemes.
2. **`complete_dataset/`**: Scaled empirical datasets with thousands of synthetic multi-tier encryption records and metadata logs for large-scale evaluation.
3. **`sample_files/`**: Standard payloads used to demonstrate uploading and encrypting files through the web interface (`/api/upload`) across different sensitivity tiers.
