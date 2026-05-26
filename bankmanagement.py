bal = 0.0


def withdraw_amt(bal, amt):
    if bal > amt:
        bal = bal - amt
        print(f"Succesfully withdraw amount {amt} remaining Balance : {bal}")
        # return bal
    else:
        print(f"Insufficient Balance : {bal}")


def deposit(bal, amt):
    if amt > 0:
        bal += amt
        print(f"Amount deposite Successful bal : {bal}")
        # return bal
    else:
        print("Deposit a valid amount")
    return bal


def bal_check(bal):
    print(f"Available Balance : {bal}")


while True:
    try:
        print("---Bank Management---")
        print("1.Balance Check\n2.Withdraw amount\n3.Deposit\n4.Exit")
        key = int(input("Enter a Number(1-4) : "))
    except ValueError:
        print("Enter a valid number between 1 and 4.")
        continue

    match key:
        case 1:
            bal_check(bal)
        case 2:
            amt = float(input("Enter an amount to withdraw: "))
            bal = withdraw_amt(bal, amt)
        case 3:
            amt = float(input("Enter an amount to deposit: "))
            bal = deposit(bal, amt)
        case 4:
            break
        case _:
            print("Enter a Number between 1 and 4.")
        
