# auth.py
import os
import bcrypt
from getpass import getpass

USERS_FILE = "library_system/data/users.txt"

def register(role="user"):
    username = input("Enter new username: ")
    password = getpass("Enter new password: ")

    # Check if user already exists
    if os.path.exists(USERS_FILE):
    # auth.py (inside register/login)
# login()
        with open(USERS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue  # skip old/malformed lines
                u, stored_hash, role = parts
                if u == username and bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                    print(f"Login successful! Welcome {username} ({role})")
                    return role           
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Store username, hashed password, role
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{hashed},{role}\n")

    print(f"Registration successful! Role: {role}")
    return True

def login():
    username = input("Username: ")
    password = getpass("Password: ")

    if not os.path.exists(USERS_FILE):
        print("No users found. Please register first.")
        return None

    with open(USERS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # skip bad lines
            u, stored_hash, role = parts
            if u == username and bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                print(f"Login successful! Welcome {username} ({role})")
                return role
    print("Invalid username or password!")
    return None