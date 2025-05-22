import json

def get_user_data():
    with open ("users.json", "r") as file:
        return json.load(file)
    
    
    
def login():
    users = get_user_data()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        print("Login successful!") 
        return username
    else: 
        print("Wrong username or password. Try again.") 
        return None 
    