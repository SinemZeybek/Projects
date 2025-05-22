from bank import get_balance


def credit_score_calculation(balance, max_balance = 2000000):
    if balance == 0:
        return 300
    elif balance >= max_balance:
        return 850
    else:
        return int(300 + (balance / max_balance) * (850 - 300))
    

def credit_options(balance):
    score = credit_score_calculation(balance)

    if score < 600: 
        return ("Unfortunately you are not eligible for a credit.")

    elif score >= 600 and score < 640:
        return ("You are eligible for 1M $ credit.")
    
    elif score >= 640 and score < 710:
        return ("You are eligible for 2M $ credit.")
    
    elif score >= 710 and score < 800:
        return ("You are eligible for 3M $ credit.")
    
    elif score >= 800 and score < 850:
        return ("You are eligible for 5M $ credit.")
    
    else:
        return ("You are eligible for more than 5M $. Please contact for more information.")
    


def credit_score_status(balance):

    score = credit_score_calculation(balance)
    print(f"Your credit score: {score}") 
    print(credit_options(balance))


        

