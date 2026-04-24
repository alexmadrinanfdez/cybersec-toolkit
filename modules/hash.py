import hashlib

def hash_file(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as file:
         chunk = file.read(1024)
         while chunk != b'':
              h.update(chunk)
              chunk = file.read(1024)
    return h.hexdigest()

if __name__ == "__main__":
    print("The SHA-256 hash of the file is:", hash_file("sample_files/sample.txt"))