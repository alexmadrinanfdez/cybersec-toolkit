import modules.hash as hash
import modules.encrypt as encrypt
import modules.password as pw

from getpass import getpass

def menu():
    print("Select an option:")
    print("1. Hash a file")
    print("2. Check file integrity")
    print("3. Encrypt a message (AES)")
    print("4. Decrypt a message (AES)")
    print("5. Check password strength")
    print("0. Exit") 

if __name__ == "__main__":
    print("Welcome to the Cybersecurity Toolkit!")
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            file = input("Enter the file path to hash: ")
            print("Hash value:", hash.hash_file(file))
        elif choice == '2':
            orig_path = input("Enter the original file path: ")
            dest_path = input("Enter the file path to check: ")
            check = hash.verify_integrity(orig_path, dest_path)
            print("Integrity check: files", "are identical." if check else "differ.")
        elif choice == '3':
            message = input("Enter the message to encrypt: ")
            key = encrypt.generate_key("AES")
            ciphertext = encrypt.aes_encrypt(message, key)
            print("Encrypted message:", ciphertext.hex())
            print("Encryption key:", key.hex())
        elif choice == '4':
            ciphertext = input("Enter the ciphertext to decrypt: ")
            key = input("Enter the encryption key: ")
            plaintext = encrypt.aes_decrypt(bytes.fromhex(ciphertext), bytes.fromhex(key))
            print("Decrypted message:", plaintext)
        elif choice == '5':
            password = getpass("Enter the password to check: ", echo_char='*')
            score, feedback = pw.check_password_strength(password)
            print(f"Password strength: {score}/4")
            print(pw.parse_feedback(feedback))
        else:
            print("Invalid choice. Please try again.")