# display file size in bytes

fName = input("Enter the file name to read: ")

f = open(fName, "r", encoding="utf-8")
print("File size in bytes: ", len(f.read()))
f.close()
