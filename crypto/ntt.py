# -*- coding: utf-8 -*-
"""
Algorithm 7: Vectorized Number Theoretic Transform (NTT) over Ring R_q
Module Lattice Polynomial Arithmetic for CRYSTALS-Kyber (NIST ML-KEM)
Parameters:
  n = 256
  q = 3329
  Primitive 256-th root of unity modulo q: zeta = 17
"""

KYBER_N = 256
KYBER_Q = 3329
MONTGOMERY_R = 2285  # 2^16 mod 3329
MONTGOMERY_QINV = 62209  # -q^{-1} mod 2^16

def bit_reverse(i, bits=7):
    res = 0
    for _ in range(bits):
        res = (res << 1) | (i & 1)
        i >>= 1
    return res

# Precompute twiddle factors (powers of 17 mod 3329 in bit-reversed order)
ZETAS = [0] * 128
zeta_base = 17
for i in range(128):
    br = bit_reverse(i, 7)
    ZETAS[i] = pow(zeta_base, br, KYBER_Q)

def montgomery_reduce(a):
    """Computes a * R^{-1} mod q using Montgomery reduction."""
    u = ((a & 0xFFFF) * MONTGOMERY_QINV) & 0xFFFF
    t = (a + u * KYBER_Q) >> 16
    if t >= KYBER_Q:
        t -= KYBER_Q
    return t

def ntt_forward(a):
    """
    Algorithm 7: Vectorized NTT Modular Butterfly Reduction over R_q.
    Transforms polynomial coefficients a in Z_q^{256} into the NTT domain.
    Matches lines 1-13 of Algorithm 7 in the Springer Q1 Journal Paper.
    """
    a = list(a)
    assert len(a) == KYBER_N, f"Input must have {KYBER_N} coefficients"
    
    index = 1
    length = 128
    while length >= 2:
        for start in range(0, KYBER_N, 2 * length):
            zeta = ZETAS[index]
            index += 1
            for j in range(start, start + length):
                # Butterfly reduction over R_q
                t = (zeta * a[j + length]) % KYBER_Q
                a[j + length] = (a[j] - t) % KYBER_Q
                a[j] = (a[j] + t) % KYBER_Q
        length //= 2
        
    return a

def ntt_inverse(a):
    """
    Inverse NTT: Maps polynomial coefficients back from NTT domain to normal domain.
    """
    a = list(a)
    assert len(a) == KYBER_N, f"Input must have {KYBER_N} coefficients"
    
    index = 127
    length = 2
    while length <= 128:
        for start in range(0, KYBER_N, 2 * length):
            zeta = ZETAS[index]
            index -= 1
            for j in range(start, start + length):
                t = a[j]
                a[j] = (t + a[j + length]) % KYBER_Q
                a[j + length] = (zeta * (a[j + length] - t)) % KYBER_Q
        length *= 2
        
    f = 3303 # 128^{-1} mod 3329
    for j in range(KYBER_N):
        a[j] = (a[j] * f) % KYBER_Q
        
    return a

def test_ntt_roundtrip():
    """Validates invertibility: iNTT(NTT(poly)) == poly."""
    import random
    test_poly = [random.randint(0, KYBER_Q - 1) for _ in range(KYBER_N)]
    transformed = ntt_forward(test_poly)
    recovered = ntt_inverse(transformed)
    return test_poly == recovered

if __name__ == "__main__":
    assert test_ntt_roundtrip(), "NTT Roundtrip Verification Failed!"
    print(f"NTT Algorithm 7 self-test passed: successfully verified over R_{KYBER_Q}^{KYBER_N}!")
