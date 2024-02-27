# 15. WAP to print
# A
# B B
# C C C
# D D D D
# E E E E E

for i in range(65,70):
    for j in range(i-64):
        print(chr(i), end=" ")
    print()

    