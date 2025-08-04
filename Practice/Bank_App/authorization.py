import json

def get_user_data():                               #kullanici verilerini yukledik
    with open ("users.json", "r") as file:
        return json.load(file)
    
    
    
def login():
    users = get_user_data()
    username = input("Username: ").strip().lower()            
    password = input("Password: ").strip().lower() 

    if username in users and users[username]["password"] == password: #burada == password`u [] icinde yazmistim calismadi.
        print("Login successful!") 
        return username    #tekrar username`e ihtiyacimiz var (balance vs).
    else: 
        print("Wrong username or password. Try again.") 
        return None 
    