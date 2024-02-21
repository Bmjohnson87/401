import os
import hashlib
from datetime import datetime

def generate_md5_hash(file_path):
    """Generate MD5 hash for a given file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory(directory):
    """Recursively scan each file in the directory and print details."""
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                file_path = os.path.join(root, name)
                hash_md5 = generate_md5_hash(file_path)
                file_size = os.path.getsize(file_path)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Timestamp: {timestamp}, File: {name}, Size: {file_size} bytes, MD5: {hash_md5}, Path: {os.path.abspath(file_path)}")
            except Exception as e:
                print(f"Error processing file {name}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path to scan: ")
    scan_directory(directory)
