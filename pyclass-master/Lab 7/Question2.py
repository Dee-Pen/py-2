# print no of lines in a file

fName = input("Enter the file name: ")

# check if the file exists
try:
    f = open(fName, "r")
    print(len(f.readlines()))
    f.close()
except FileNotFoundError:
    print("File not found")
