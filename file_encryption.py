from cryptography.fernet import Fernet
import os
import time
from colorama import Fore, Style, init
init(autoreset=True)

def main():
    menu()

def menu():
    generate_keys()
    key=load_keys()
  
    while True:
        print("\n ===================================== MENU =========================================")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        
        try:
          option=int(input("Choose from the above options: "))
        except ValueError:
            print("Invalid input, please input a number.")
            continue

        match option:
            case 1:
                filename=input(Fore.CYAN + "Enter filename to encrypt: ")
                if not os.path.exists(filename):
                    print(Fore.RED + f"❌ File '{filename}' not found. Please check the name and try again.")
                    continue
                encrypt_file(filename,key)
            case 2:
                filename=input(Fore.CYAN + "Enter filename to decrypt: ")
                if not os.path.exists(filename):
                    print(Fore.RED + f"❌ File '{filename}' not found. Please check the name and try again.")
                    continue
                decrypt_file(filename,key)
            case 3:
                print("Exiting main menu", end="", flush=True)
                for _ in range(4):
                    time.sleep(0.6)
                    print(".",end="",flush=True)
                print()
                break
            case _:
                print("Please choose from the above options. (1-3)")
                continue

def generate_keys():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("✅ Key generated and saved as 'secret.key'")
    else:
        print("Key already exists. Using the existing one.")

def load_keys():
    try:
        with open("secret.key", "rb") as key_load:
            key = key_load.read()
        return key
    except FileNotFoundError:
        print(Fore.RED + "❌ Key file 'secret.key' not found.")
        return None

def encrypt_file(filename, key):
    try:
        fernet = Fernet(key)
        with open(filename, "rb") as original_file:
            original = original_file.read()
        encrypted = fernet.encrypt(original)
        with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"🔒 File '{filename}' has been encrypted successfully.")
    except Exception as e:
        print(Fore.RED + f"❌ Error encrypting file '{filename}': {e}")

def decrypt_file(filename, key):
    try:
        fernet = Fernet(key)
        with open(filename, "rb") as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        print(f"🔓 File '{filename}' has been decrypted successfully.")
    except Exception as e:
        print(Fore.RED + f"❌ Error decrypting file '{filename}': {e}")

if __name__ == "__main__":
    main()
