# WAP to create a dictionary named year whose keys are month names and values are their
# corresponding number of days.

year = {}

for i in range(12):
    month = input("Enter the month name: or done to exit:")
    if month == "done":
        break
    if month in year:
        print("The month is already in the list")
    else:
        days = input("Enter the number of days in the month: ")
        year[month] = days
print(year)