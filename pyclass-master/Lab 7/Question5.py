#wap to copy the contents of one file to another file and replace if 2 consecutive spaces are found with a single space.

fName = input("Enter the file name to read: ")

f = open(fName, "r")
content = f.read()
f.close()

fName = input("Enter the file name to create: ")

f = open(fName, "w")
f.write(content.replace("  ", " "))
f.close()
