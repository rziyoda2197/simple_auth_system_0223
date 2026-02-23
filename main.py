import json
import hashlib

FILE = "users.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = load()

while True:
    print("1.Register 2.Login 0.Exit")
    c = input("> ")

    if c == "1":
        username = input("Username: ")
        password = input("Password: ")
        users[username] = hash_password(password)
        save(users)
        print("Registered!")

    elif c == "2":
        username = input("Username: ")
        password = input("Password: ")
        if users.get(username) == hash_password(password):
            print("Login success!")
        else:
            print("Invalid credentials")

    else:
        break
