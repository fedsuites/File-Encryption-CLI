# 🔐 File Encryption CLI Tool

A command-line Python utility for **secure file encryption and decryption** using the `cryptography` library’s `Fernet` symmetric encryption algorithm.  
The tool ensures confidentiality and integrity of your data with simple menu-driven interaction.

---

##  Overview
This project demonstrates the practical use of **symmetric key cryptography** in Python.  
It allows users to:
- Generate and persist encryption keys securely.
- Encrypt and decrypt files of any type.
- Interact via a robust and user-friendly CLI with error handling.

---

## ⚙️ Technical Details

###  Encryption Algorithm
The project uses **Fernet** from the `cryptography` library.  
Fernet guarantees:
- **AES in CBC mode with a 128-bit key**
- **PKCS7 padding**
- **HMAC (SHA256)** for message authentication  
This means each encrypted file is **authenticated and tamper-proof**.

###  Key Management
- The key is generated **once** and saved locally as `secret.key`.
- If the file exists, it’s reused — avoiding accidental key overwrites.
- The same key must be used to decrypt files that were encrypted with it.

---

##  Code Structure

| File | Description |
|------|--------------|
| `encryption_tool.py` | Main script containing all core functions and CLI logic |
| `secret.key` | Binary file storing the symmetric encryption key (auto-generated) |

---

##  Features
✅ Generate and persist symmetric encryption keys  
✅ Encrypt and decrypt any file type (text, CSV, PDF, etc.)  
✅ Robust error handling for missing or invalid files  
✅ Simple and interactive command-line menu  
✅ Prevents accidental key regeneration  

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/file-encryption-cli.git
cd file-encryption-cli
```
### 2. Install dependencies
```bash
pip install cryptography
```

### Usage

Run the script:

python encryption_tool.py

You’ll see a simple interactive menu:

=====================================
1. Encrypt a file
2. Decrypt a file
3. Exit
=====================================

Example workflow:

-Choose Encrypt a file

-Enter the filename (e.g., data.csv)

-The file will be encrypted using Fernet and overwritten with ciphertext.

-Choose Decrypt a file to restore it to plaintext.

### Important Notes

-Do not delete secret.key, or you won’t be able to decrypt your files.

-Each key is unique; files encrypted with one key cannot be decrypted with another.

-The script encrypts files in-place, so consider backing up original data.

### Future Improvements

-Add support for multiple keys or password-based key derivation (PBKDF2)

-Option to specify output directory instead of overwriting

-File integrity verification logs

-Unit testing with pytest

🧑‍💻 Author:
Mubarak Awwal

