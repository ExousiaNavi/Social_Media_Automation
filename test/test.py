from cryptography.fernet import Fernet

# Step 1: Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Your data structure
data = {
    "JeetBuzz": {
        "credentials": {
            "email": "coco.rodel@auroramy.com",
            "password": "coco_rodel.23"
        },
    },
    "BJ88": {
        "credentials": {
            "email": "explorercurious437@gmail.com",
            "password": "Bernerslee11"
        },
    },
    "sub_BJ88": {
        "credentials": {
            "email": "bs2963419@gmail.com",
            "password": "Bernerslee11"
        },
    }
}

# Step 3: Encrypt credentials
for key_name, info in data.items():
    password_bytes = info["credentials"]["password"].encode()
    encrypted_password = cipher.encrypt(password_bytes)
    info["credentials"]["password"] = encrypted_password

print(f"Encrypted Data: {data}")
print(f"Encryption Key: {key}")

# Step 4: Decrypt passwords
for key_name, info in data.items():
    encrypted_password = info["credentials"]["password"]
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    info["credentials"]["password"] = decrypted_password

print(f"Decrypted Data: {data}")
