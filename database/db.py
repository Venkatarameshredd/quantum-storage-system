import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='quantum_storage.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS file_metadata (
                    file_id TEXT PRIMARY KEY,
                    filename TEXT,
                    size INTEGER,
                    encryption_mode TEXT,
                    sensitivity TEXT,
                    user_id TEXT,
                    hybrid_salt BLOB,
                    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS key_fragments (
                    file_id TEXT,
                    fragment BLOB,
                    fragment_id INTEGER,
                    PRIMARY KEY (file_id, fragment_id)
                )
            ''')
            conn.commit()

    def save_metadata(self, file_id, filename, size, mode, sensitivity, user_id, hybrid_salt=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO file_metadata (file_id, filename, size, encryption_mode, sensitivity, user_id, hybrid_salt)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (file_id, filename, size, mode, sensitivity, user_id, hybrid_salt))
            conn.commit()

    def get_metadata(self, file_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM file_metadata WHERE file_id = ?', (file_id,))
            row = cursor.fetchone()
            if row:
                return {
                    'file_id': row[0],
                    'filename': row[1],
                    'size': row[2],
                    'encryption_mode': row[3],
                    'sensitivity': row[4],
                    'user_id': row[5],
                    'hybrid_salt': row[6],
                    'upload_date': row[7]
                }
            return None

    def save_key_fragment(self, file_id, fragment, fragment_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO key_fragments (file_id, fragment, fragment_id)
                VALUES (?, ?, ?)
            ''', (file_id, fragment, fragment_id))
            conn.commit()

    def get_key_fragment(self, file_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT fragment, fragment_id FROM key_fragments WHERE file_id = ? LIMIT 1', (file_id,))
            row = cursor.fetchone()
            if row:
                return {'fragment': row[0], 'fragment_id': row[1]}
            return None

    def update_key_fragment(self, file_id, fragment, fragment_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO key_fragments (file_id, fragment, fragment_id)
                VALUES (?, ?, ?)
            ''', (file_id, fragment, fragment_id))
            conn.commit()
            
    def get_all_files(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT file_id, filename, size, upload_date FROM file_metadata ORDER BY upload_date DESC')
            rows = cursor.fetchall()
            return [{'file_id': r[0], 'filename': r[1], 'size': r[2], 'upload_date': r[3]} for r in rows]

db_manager = DatabaseManager()
