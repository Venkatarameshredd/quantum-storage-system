import hashlib
import json
import time

class SecureLogger:
    def __init__(self):
        self.log_chain = []
        self.anomalies = []
        
        # Create genesis block
        self._append_log({
            "action": "system_start",
            "timestamp": time.time(),
            "status": "success"
        })

    def _hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def _append_log(self, data):
        if len(self.log_chain) > 0:
            previous_hash = self.log_chain[-1]['hash']
        else:
            previous_hash = "0" * 64
            
        block = {
            "index": len(self.log_chain),
            "data": data,
            "previous_hash": previous_hash
        }
        
        block_hash = self._hash_block(block)
        block['hash'] = block_hash
        self.log_chain.append(block)
        return block

    def log_operation(self, action, file_id, user_id, status, details=""):
        data = {
            "action": action,
            "file_id": file_id,
            "user_id": user_id,
            "status": status,
            "details": details,
            "timestamp": time.time()
        }
        
        self._append_log(data)
        self._analyze_anomalies(data)

    def compute_anomaly_score(self, window_size=50):
        """
        Algorithm 6: Sliding-Window Bayesian Anomaly Classification Routine.
        Evaluates a window W of up to 50 consecutive audit events.
        Computes failure rate r_f and Shannon entropy H_T over inter-arrival times delta_t.
        Returns anomaly likelihood score S = 0.70 * r_f + 0.30 * (1 - min(H_T / 4.0, 1.0)).
        """
        import math
        w = self.log_chain[-window_size:] if len(self.log_chain) >= window_size else self.log_chain
        if len(w) < 2:
            return 0.0, 0.0, 4.0
            
        failures = sum(1 for entry in w if str(entry['data'].get('status', '')).lower() != 'success')
        r_f = failures / float(len(w))
        
        timestamps = [entry['data'].get('timestamp', 0) for entry in w]
        delta_t = [max(0.0, timestamps[i] - timestamps[i-1]) for i in range(1, len(timestamps))]
        
        if len(delta_t) == 0:
            h_t = 4.0
        else:
            bins = [0] * 8
            for dt in delta_t:
                if dt < 0.001:
                    bins[0] += 1
                elif dt < 0.01:
                    bins[1] += 1
                elif dt < 0.1:
                    bins[2] += 1
                elif dt < 1.0:
                    bins[3] += 1
                elif dt < 5.0:
                    bins[4] += 1
                elif dt < 10.0:
                    bins[5] += 1
                elif dt < 60.0:
                    bins[6] += 1
                else:
                    bins[7] += 1
            
            n_intervals = float(len(delta_t))
            h_t = 0.0
            for count in bins:
                if count > 0:
                    p = count / n_intervals
                    h_t -= p * math.log2(p)
                    
        s = 0.70 * r_f + 0.30 * (1.0 - min(h_t / 4.0, 1.0))
        return s, r_f, h_t

    def _analyze_anomalies(self, recent_log):
        # Algorithm 6: Sliding-Window Bayesian Anomaly Classification (Window W=50, threshold tau=0.65)
        s_score, r_f, h_t = self.compute_anomaly_score(window_size=50)
        if s_score >= 0.65:
            self._record_anomaly(
                "bayesian_window_anomaly",
                "critical",
                f"Bayesian Anomaly Score S={s_score:.3f} >= 0.65 (Failure rate: {r_f*100:.1f}%, Entropy: {h_t:.2f} bits)"
            )

        # Concentrated failed decryptions on specific object (DoS / Brute-force rule)
        if recent_log.get('status') == 'failure' and recent_log.get('action') == 'download':
            failed_decrypts = [log for log in self.log_chain[-20:] 
                               if log['data'].get('action') == 'download' 
                               and log['data'].get('status') == 'failure'
                               and log['data'].get('file_id') == recent_log.get('file_id')]
            
            if len(failed_decrypts) >= 5:
                self._record_anomaly(
                    "high_failed_decrypts", 
                    "high", 
                    f"Concentrated decryption failures on object {recent_log.get('file_id')} ({len(failed_decrypts)} failures in window)."
                )

    def _record_anomaly(self, type, severity, description):
        # Prevent duplicate identical anomalies from flooding
        for a in self.anomalies:
            if a['description'] == description:
                return
                
        anomaly = {
            "id": len(self.anomalies) + 1,
            "type": type,
            "severity": severity,
            "description": description,
            "timestamp": time.time(),
            "status": "open"
        }
        self.anomalies.append(anomaly)
        print(f"[ANOMALY DETECTED] {severity.upper()} - {type}: {description}")

    def verify_chain(self):
        errors = []
        for i in range(1, len(self.log_chain)):
            current = self.log_chain[i]
            previous = self.log_chain[i-1]
            
            # Verify chain link
            if current['previous_hash'] != previous['hash']:
                errors.append(f"Broken link at block {i}")
                
            # Verify hash
            temp_block = {k: v for k, v in current.items() if k != 'hash'}
            if self._hash_block(temp_block) != current['hash']:
                errors.append(f"Invalid hash at block {i}")
                
        return len(errors) == 0, errors

secure_logger = SecureLogger()
