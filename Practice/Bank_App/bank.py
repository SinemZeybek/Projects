import json
from datetime import datetime


def get_balance(username):
    with open("users.json", "r") as file:
        users = json.load(file)
    return float(users[username]["balance"])



def update_balance(username, amount):
    with open("users.json", "r") as file:
        users = json.load(file)

    users[username]["balance"] += amount

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4) 




def logs(username, action):
    with open("{username}.txt", "a") as logs_file:
        logs_file.write(f"{datetime.now()} - {action}\n")



def withdraw_money(username, amount):
    balance = get_balance(username)
    
    if amount > balance:
        print("Not enough balance to withdraw.") 

    else:
        logs(username, f"{amount} $ withdrawn.") 
        update_balance(username, -amount)
        print("Withdrawal successful.") 

    
def deposit_money(username, amount):
    
    logs(username, f"{amount} $ depositted.")
    update_balance(username, +amount)
    print(f"{amount}$ was successfully depositted into your account.")



