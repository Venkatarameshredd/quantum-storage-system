import sqlite3
import csv
import json
import os
import time
from crypto.ecc import ecc_manager
from crypto.kyber import kyber_manager
from crypto.hybrid import hybrid_manager
from crypto.aes_gcm import aes_gcm_manager

def export_db_dataset():
    os.makedirs("dataset/complete_dataset", exist_ok=True)
    
    # 1. Export file_metadata table to CSV & JSON
    conn = sqlite3.connect("quantum_storage.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT file_id, filename, size, encryption_mode, sensitivity, user_id, upload_date FROM file_metadata")
    rows = cursor.fetchall()
    
    headers = ["file_id", "filename", "size_bytes", "encryption_mode", "sensitivity", "user_id", "upload_date"]
    
    csv_path = "dataset/complete_dataset/stored_files_metadata.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Exported metadata to {csv_path}")

    json_data = [dict(zip(headers, r)) for r in rows]
    json_path = "dataset/complete_dataset/stored_files_metadata.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print(f"Exported metadata to {json_path}")

def generate_benchmark_dataset():
    print("Generating comprehensive empirical benchmark dataset...")
    sizes = [1024 * 100, 1024 * 1024, 5 * 1024 * 1024] # 100KB, 1MB, 5MB
    iterations = 20
    
    results = []
    
    for sz in sizes:
        sz_mb = sz / (1024 * 1024)
        data = os.urandom(sz)
        
        # ECC Benchmark
        ecc_start = time.time()
        for _ in range(iterations):
            priv, pub = ecc_manager.generate_keypair()
            key = ecc_manager.derive_shared_secret(priv, pub)
            nonce, ct = aes_gcm_manager.encrypt(key[:32], data)
        ecc_avg = ((time.time() - ecc_start) / iterations) * 1000
        
        results.append({
            "mode": "ECC-256 (Classical)",
            "file_size_mb": sz_mb,
            "iterations": iterations,
            "avg_latency_ms": round(ecc_avg, 4),
            "quantum_resistant": False,
            "public_key_bytes": 64,
            "ciphertext_expansion_bytes": 0
        })

        # Kyber Benchmark
        kyber_start = time.time()
        for _ in range(iterations):
            priv, pub = kyber_manager.generate_keypair()
            ct_k, key = kyber_manager.encapsulate(pub)
            nonce, ct = aes_gcm_manager.encrypt(key, data)
        kyber_avg = ((time.time() - kyber_start) / iterations) * 1000
        
        results.append({
            "mode": "Kyber-512 (Post-Quantum)",
            "file_size_mb": sz_mb,
            "iterations": iterations,
            "avg_latency_ms": round(kyber_avg, 4),
            "quantum_resistant": True,
            "public_key_bytes": 800,
            "ciphertext_expansion_bytes": 768
        })

        # Hybrid Benchmark
        hybrid_start = time.time()
        for _ in range(iterations):
            keys = hybrid_manager.generate_hybrid_keypair()
            ecc_ss = ecc_manager.derive_shared_secret(keys['ecc_private'], keys['ecc_public'])
            ct_k, kyber_ss = kyber_manager.encapsulate(keys['kyber_public'])
            combined = hybrid_manager.derive_combined_secret(ecc_ss, kyber_ss)
            expanded = hybrid_manager.expand_keys(combined)
            nonce, ct = aes_gcm_manager.encrypt(expanded['k_enc'], data)
        hybrid_avg = ((time.time() - hybrid_start) / iterations) * 1000

        results.append({
            "mode": "Proposed Hybrid (ECC + Kyber)",
            "file_size_mb": sz_mb,
            "iterations": iterations,
            "avg_latency_ms": round(hybrid_avg, 4),
            "quantum_resistant": True,
            "public_key_bytes": 864,
            "ciphertext_expansion_bytes": 768
        })

    csv_path = "dataset/complete_dataset/quantum_cryptography_performance_dataset.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["mode", "file_size_mb", "iterations", "avg_latency_ms", "quantum_resistant", "public_key_bytes", "ciphertext_expansion_bytes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Exported benchmark dataset to {csv_path}")

if __name__ == "__main__":
    export_db_dataset()
    generate_benchmark_dataset()
