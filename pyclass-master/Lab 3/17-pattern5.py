# 17.WAP To Print
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


for i in range(1,10,2): # 1,3,5,7,9
    for j in range(5-i//2):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
    
