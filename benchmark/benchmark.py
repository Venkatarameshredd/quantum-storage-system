import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto.ecc import ecc_manager
from crypto.kyber import kyber_manager
from crypto.hybrid import hybrid_manager
from crypto.aes_gcm import aes_gcm_manager

def run_benchmarks():
    print("======================================================================")
    print("QUANTUM-RESISTANT ADAPTIVE HYBRID ENCRYPTION BENCHMARK SUITE")
    print("======================================================================")
    
    iters = 10
    
    # 1. ECC
    start = time.time()
    for _ in range(iters):
        ecc_manager.generate_keypair()
    ecc_time = (time.time() - start) / iters * 1000
    print(f"\n=== ECC Keypair Generation ({iters} iterations) ===")
    print(f"  Average: {ecc_time:.4f} ms")
    
    # 2. Kyber
    start = time.time()
    for _ in range(iters):
        kyber_manager.generate_keypair()
    kyber_time = (time.time() - start) / iters * 1000
    print(f"\n=== Kyber Keypair Generation ({iters} iterations) ===")
    print(f"  Average: {kyber_time:.4f} ms")
    
    # 3. Hybrid
    start = time.time()
    for _ in range(iters):
        hybrid_manager.generate_hybrid_keypair()
    hybrid_time = (time.time() - start) / iters * 1000
    print(f"\n=== Hybrid Keypair Generation ({iters} iterations) ===")
    print(f"  Average: {hybrid_time:.4f} ms")
    
    # 4. AES-GCM Throughput (1MB)
    data = os.urandom(1024 * 1024)
    key = os.urandom(32)
    start = time.time()
    for _ in range(iters):
        aes_gcm_manager.encrypt(key, data)
    aes_time = (time.time() - start) / iters * 1000
    throughput = (1024 * 1024 * iters) / (time.time() - start) / (1024 * 1024)
    print(f"\n=== AES-256-GCM Encryption (1 MB file, {iters} iterations) ===")
    print(f"  Average: {aes_time:.4f} ms")
    print(f"  Throughput: {throughput:.2f} MB/s")
    
    print("\n======================================================================")
    print("BENCHMARK SUMMARY TABLE")
    print("======================================================================")
    print(f"{'Operation':<30} {'Avg (ms)':<10}")
    print("-" * 70)
    print(f"{'ECC Keypair Generation':<30} {ecc_time:.4f}")
    print(f"{'Kyber Keypair Generation':<30} {kyber_time:.4f}")
    print(f"{'Hybrid (ECC + Kyber)':<30} {hybrid_time:.4f}")
    print(f"{'AES-256-GCM Encryption (1MB)':<30} {aes_time:.4f}")

if __name__ == "__main__":
    run_benchmarks()
