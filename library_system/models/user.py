# models.py
import bcrypt

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.role = role
        self.password = self.hash_password(password)  # store hashed password

    def hash_password(self, password):
        """Hashes a plain text password"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """Checks if the provided password matches the stored hash"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))