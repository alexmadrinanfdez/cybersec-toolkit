import hashlib

def hash_file(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as file:
         chunk = file.read(1024)
         while chunk != b'':
              h.update(chunk)
              chunk = file.read(1024)
    return h.hexdigest()

def verify_integrity(orig_file, dest_file):
    orig_hash = hash_file(orig_file)
    dest_hash = hash_file(dest_file)
    print(f"Integrity check between {orig_file} and {dest_file}:")
    if orig_hash == dest_hash:
        return "Files are identical."
    return "Files are different."

if __name__ == "__main__":
    print("The SHA-256 hash of the file is:", hash_file("sample_files/sample.txt"))

    print(verify_integrity("sample_files/python-powered-w.svg", "sample_files/python-powered-h.svg"))
    print(verify_integrity("sample_files/python-powered-w.svg", "sample_files/python-powered-w-copy.svg"))