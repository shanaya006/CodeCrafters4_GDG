import bcrypt

# Enter the password you want to hash
password = "admin123"

# Generate a salt and hash the password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Print the hashed password as a UTF-8 string
print("Hashed password:")
print(hashed.decode('utf-8'))
