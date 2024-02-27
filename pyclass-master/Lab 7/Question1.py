# read from file and print the content

fName = input("Enter the file name to read: ")

def readFile():
    # check if the file exists
    try:
        f = open(fName, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("File not found")



