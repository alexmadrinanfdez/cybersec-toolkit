# Cybersecurity Toolkit

A lightweight Python toolkit for basic cybersecurity utilities, inspired by [this tutorial](https://youtu.be/kb_scuDUHls?si=fRaTzwHG8lP0AL0C).

## Features

- Compute SHA-256 file hashes
- Verify file integrity by comparing hashes
- Encrypt and decrypt messages using AES-GCM
- Check password strength with zxcvbn

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate # on Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the main script:

```bash
python main.py
```

Follow the interactive menu to select a task.
