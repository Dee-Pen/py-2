# 11.Write a program to generate fibonacci / Hosoya's pyramid


def fabo(n):
    if n <= 1:
        return n
    else:
        return fabo(n-1) + fabo(n-2)
    
def faboTri(n):
    for i in range(n):
        for j in range(i+1):
            print(fabo(j), end=" ")
        print()

faboTri(5)

