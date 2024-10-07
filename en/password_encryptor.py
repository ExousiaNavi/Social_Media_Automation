from cryptography.fernet import Fernet
import json
import os
import logging

class PasswordEncryptor:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, file_path, key_file):
        self.file_path = file_path  # Path to the JSON file with credentials
        self.encrypted_passwords = {}  # Store encrypted passwords or keys (if needed)
        self.key_file = key_file  # Path to the encryption key file
        self.data = self.load_json_data()  # Load the JSON data

    def load_json_data(self):
        """Load JSON data from the provided file."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None

    def generate_key(self):
        """Generate an encryption key and save it to a file."""
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        logging.info(f"Encryption key generated and saved to {self.key_file}")
        return key

    def load_key(self):
        """Load the encryption key from the file specified during initialization."""
        try:
            with open(self.key_file, "rb") as key_file:
                key = key_file.read()
            logging.info(f"Loaded key from {self.key_file}: {key}")
            return key
        except FileNotFoundError:
            logging.error(f"Key file not found: {self.key_file}")
            return None

    def is_encrypted(self, password):
        """
        Check if a password is already encrypted.
        Fernet-encrypted strings usually start with 'gAAAA' as a prefix.
        """
        return password.startswith('gAAAA')

    def encrypt_passwords(self, key):
        """Encrypt passwords in the JSON data."""
        if not self.data:
            logging.error("No data to encrypt.")
            return None

        for entry in self.data["data"]:
            for account, info in entry.items():
                if isinstance(info, dict) and "credentials" in info and "password" in info["credentials"]:
                    password = info["credentials"]["password"]
                    
                    # Only encrypt if it's not already encrypted
                    if not self.is_encrypted(password):  # Use self.is_encrypted()
                        fernet = Fernet(key)
                        encrypted_password = fernet.encrypt(password.encode())  # Encrypt password
                        
                        # Replace plaintext password with encrypted one
                        info["credentials"]["password"] = encrypted_password.decode()  # Store as string for JSON compatibility
                        logging.info(f"Encrypted password for account: {account}")
                        self.encrypted_passwords[account] = key.decode()  # Store the encryption key for future decryption (optional)
                    else:
                        logging.info(f"Password for {account} is already encrypted. Skipping.")

        return self.data

    def decrypt_password(self, encrypted_password):
        """Decrypt a specific password using the loaded key."""
        key = self.load_key()
        if not key:
            logging.error("No key found. Cannot decrypt password.")
            return None

        fernet = Fernet(key)
        try:
            logging.info(f"Attempting to decrypt password: {encrypted_password}")
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            # logging.info(f"Successfully decrypted password: {decrypted_password}"
            return decrypted_password
        except Exception as e:
            logging.error(f"Error decrypting password: {e}")
            return None

    def save_encrypted_data(self):
        """Save the encrypted JSON data back to the file."""
        if not self.data:
            logging.error("No data to save.")
            return

        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)
        logging.info(f"Encrypted data saved to {self.file_path}.")