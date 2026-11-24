class AdaptiveEngine:
    def __init__(self):
        self.LARGE_THRESHOLD = 5 * 1024 * 1024 # 5 MB

    def decide(self, sensitivity, file_size):
        if sensitivity == 'low':
            return {
                'selected_mode': 'ecc',
                'quantum_resistant': False,
                'reasoning': 'Low sensitivity: ECC provides fast, classical security',
                'estimated_overhead': 0.05
            }
        elif sensitivity == 'medium':
            return {
                'selected_mode': 'kyber',
                'quantum_resistant': True,
                'reasoning': 'Medium sensitivity: Kyber provides quantum safety with minimal overhead',
                'estimated_overhead': 0.10
            }
        elif sensitivity == 'high':
            if file_size > self.LARGE_THRESHOLD:
                return {
                    'selected_mode': 'kyber',
                    'quantum_resistant': True,
                    'reasoning': 'High sensitivity but large file: Kyber provides quantum safety with better performance than hybrid',
                    'estimated_overhead': 0.15
                }
            else:
                return {
                    'selected_mode': 'hybrid',
                    'quantum_resistant': True,
                    'reasoning': 'High sensitivity: Hybrid ECC+Kyber provides defense against both classical and quantum adversaries',
                    'estimated_overhead': 0.25
                }
        else:
            return {
                'selected_mode': 'ecc',
                'quantum_resistant': False,
                'reasoning': 'Unknown sensitivity: Defaulting to standard ECC encryption',
                'estimated_overhead': 0.05
            }

    def evaluate_risk_model(self, x1_threat=0.1, x2_health=0.1, x3_sensitivity=0.4, x4_horizon=0.2, weights=None, theta1=0.35, theta2=0.70):
        """
        Closed-loop operational evaluation of the Adaptive Encryption Decision Engine (AEDE):
        R = sum_{i=1}^4 w_i * x_i
        Profiles:
          - LOW (R < theta1): NIST Level 1 Classical ECC-256 + (2,3) Shamir over GF(257)
          - MEDIUM (theta1 <= R < theta2): NIST Level 3 Kyber-512 + (2,3) Shamir over GF(257)
          - HIGH (R >= theta2): NIST Level 5 Hybrid ECC+Kyber-512 + (2,3) or (3,5) Shamir
        """
        if weights is None:
            weights = [0.25, 0.25, 0.35, 0.15]
            
        indicators = [x1_threat, x2_health, x3_sensitivity, x4_horizon]
        r_score = sum(w * x for w, x in zip(weights, indicators))
        
        if r_score < theta1:
            profile = "LOW"
            selected_mode = "ecc"
            quantum_resistant = False
            shamir_config = (2, 3)
        elif r_score < theta2:
            profile = "MEDIUM"
            selected_mode = "kyber"
            quantum_resistant = True
            shamir_config = (2, 3)
        else:
            profile = "HIGH"
            selected_mode = "hybrid"
            quantum_resistant = True
            shamir_config = (3, 5) if r_score > 0.85 else (2, 3)
            
        return {
            'risk_score': round(r_score, 4),
            'profile': profile,
            'selected_mode': selected_mode,
            'quantum_resistant': quantum_resistant,
            'shamir_config': shamir_config,
            'indicators': {
                'x1_threat': x1_threat,
                'x2_health': x2_health,
                'x3_sensitivity': x3_sensitivity,
                'x4_horizon': x4_horizon
            }
        }

adaptive_engine = AdaptiveEngine()
