# WAP which accept principle, rate and time from user and print the
# simple interest. The formula to calculate simple interest is: simple
# interest = (principle * rate * time) / 100



principle = float(input("Principle Amount: "))
rate = float(input("Interest Rate: "))
time = float(input("Time in Years: "))

interest = (principle * time * rate)/100

print("Total Interest: ", interest)