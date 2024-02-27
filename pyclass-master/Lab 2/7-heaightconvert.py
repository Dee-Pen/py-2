# 7. WAP that asks your height in centimeters and converts it into foot and inches

height = float(input("Enter your height in centimeters: "))

foot = height // 30.48
height = height % 30.48

inches = height // 2.54
height = height % 2.54

print("Your height is ", foot, " foot ", inches, " inches ")