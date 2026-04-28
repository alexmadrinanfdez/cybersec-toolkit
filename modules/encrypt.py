import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def aes_encrypt(message: str, key: bytes) -> bytes:
    """Encrypts a string message using AES-GCM."""
    aes = AESGCM(key)
    nonce = secrets.token_bytes(12)  # 96-bit nonce
    plaintext = message.encode()
    ciphertext = aes.encrypt(nonce, plaintext, None)
    return nonce + ciphertext  # Prepend nonce for later use

def aes_decrypt(ciphertext: bytes, key: bytes) -> str:
    """Decrypts a ciphertext using AES-GCM."""
    aes = AESGCM(key)
    nonce = ciphertext[:12]  # Extract the nonce
    ct = ciphertext[12:]  # Extract the actual ciphertext
    plaintext = aes.decrypt(nonce, ct, None)
    return plaintext.decode()

if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256)  # Generate a random 256-bit key
    message = "This is a secret message."
    ciphertext = aes_encrypt(message, key)
    print("Ciphertext:", ciphertext.hex())
    decrypted_message = aes_decrypt(ciphertext, key)
    print("Decrypted message:", decrypted_message)