# wap to withdraw money from ATM but limit of withdraw is 20% of balance

balance = int(input("Enter your balance: "))
withdraw = int(input("Enter amount to withdraw: "))
limit = balance * 0.2

if withdraw > limit:
    print("Withdraw limit exceeded")
else:
    balance = balance - withdraw
    print("Balance: ", balance)
    