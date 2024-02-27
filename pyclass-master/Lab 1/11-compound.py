# Write a program which prompts the user to input principle, rate and
# time and calculate compound interest. The formula is :
# CI = P(1+R/100)^T - P

principle = float(input("Principle Amount: "))
rate = float(input("Interest Rate: "))
time = float(input("Time in Years: "))

interest = principle * (1+rate/100)**time - principle

print("Total Interest: ", interest)
