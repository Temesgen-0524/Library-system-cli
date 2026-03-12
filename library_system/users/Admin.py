import bcrypt

# Choose an admin username and password
username = "admin"
password = "adminpass"

# Hash the password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Format for your users.txt
role = "admin"
line = f"{username},{hashed},{role}\n"

# Append to your users.txt
with open("library_system/data/users.txt", "a") as f:
    f.write(line)

print("Admin account created successfully!")