import hashlib

def hash_file(file_path: str) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(1024):
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(orig_file: str, dest_file: str) -> bool:
    orig_hash = hash_file(orig_file)
    dest_hash = hash_file(dest_file)
    return orig_hash == dest_hash

if __name__ == "__main__":
    print("The SHA-256 hash of the file is:", hash_file("sample_files/sample.txt"))

    orig_file = "sample_files/python-powered-w.svg"
    dest_file = "sample_files/python-powered-h.svg"
    print(f"Integrity check between {orig_file} and {dest_file}:")
    if verify_integrity(orig_file, dest_file):
        print("Files are identical.")
    else:
        print("Files differ.")
    dest_file = "sample_files/python-powered-w-copy.svg"
    print(f"Integrity check between {orig_file} and {dest_file}:")
    if verify_integrity(orig_file, dest_file):
        print("Files are identical.")
    else:
        print("Files differ.")