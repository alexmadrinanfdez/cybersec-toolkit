# Cybersecurity Tools

A lightweight Python toolkit for basic cybersecurity utilities, inspired by [this tutorial](https://youtu.be/kb_scuDUHls?si=fRaTzwHG8lP0AL0C).

## Features

- Compute SHA-256 file hashes
- Verify file integrity by comparing hashes
- Encrypt and decrypt messages with AES and RSA
- Check password strength with zxcvbn
- Hash and verify passwords with bcrypt

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Examples

Run the provided modules directly **from the root** project **folder**:

```bash
python -m src.hash
python -m src.encrypt
python -m src.password
```
