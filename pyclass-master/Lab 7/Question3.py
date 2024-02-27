#write to a user given file

fName = input("Enter the file name to create: ")

f = open(fName, "w", encoding="utf-8")
f.write(input("Enter the content: "))
f.close()








