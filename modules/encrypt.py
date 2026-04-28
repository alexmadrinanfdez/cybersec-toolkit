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

def rsa_encrypt(message: str, public_key) -> bytes:
    """Encrypts a string message using RSA."""
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(ciphertext: bytes, private_key) -> str:
    """Decrypts a ciphertext using RSA."""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

if __name__ == "__main__":
    message = "This is a secret message."
    # AES Example
    key = AESGCM.generate_key(bit_length=256)  # Generate a random 256-bit key
    ciphertext = aes_encrypt(message, key)
    print("AES Ciphertext:", ciphertext.hex())
    decrypted_message = aes_decrypt(ciphertext, key)
    print("AES Decrypted message:", decrypted_message)
    # RSA Example
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    ciphertext = rsa_encrypt(message, public_key)
    print("RSA Ciphertext:", ciphertext.hex())
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("RSA Decrypted message:", decrypted_message)