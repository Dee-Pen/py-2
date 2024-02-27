# 1. Write a program that accepts seconds from keyboard as integer. Your
# program should converts seconds in hours, minutes and seconds. Your
# output should like this :
# Enter seconds: 13400
# Hours: 3
# Minutes: 43
# Seconds: 20

seconds = int(input("Enter seconds: "))

hour = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("Hours: ", hour)
print("Minutes: ", minutes)
print("Seconds: ", seconds)



