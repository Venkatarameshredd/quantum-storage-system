import os

class LocalStorageManager:
    def __init__(self, storage_dir='local_storage'):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def save_file(self, file_id, data):
        path = os.path.join(self.storage_dir, file_id)
        with open(path, 'wb') as f:
            f.write(data)
        return path

    def get_file(self, file_id):
        path = os.path.join(self.storage_dir, file_id)
        if not os.path.exists(path):
            return None
        with open(path, 'rb') as f:
            return f.read()

storage_manager = LocalStorageManager()
