from authorization import login
from bank import get_balance, withdraw_money, deposit_money
from credit import credit_score_status

def main(): 
    username = login()
    if username == None:
       return


    while True: 
        print("""   MENU
              1. Check Balance
              2. Withdraw Money
              3. Deposit Money
              4. Credit Status
              5. Exit
                 """)
        
        choice = input("What would you like to do? (1/2/3/4/5): ").strip() 

        if choice == "1":
            print(f"Current Balance: {get_balance(username)}")

        elif choice == "2":
            amount = float(input("How much $ would you like to withdraw?"))
            withdraw_money(username, amount)
        
        elif choice == "3":
            amount = float(input("How much $ would you like to deposit?"))
            deposit_money(username, amount)

        elif choice == "4":
            balance = get_balance(username)   #balance`i getirmemistim basta calismadi.
            credit_score_status(balance)

        elif choice == "5":
            print("Exiting...")
            break
        
        else: 
            print("Please choose one of these numbers: 1/2/3/4/5")

main()