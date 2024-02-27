# ask marks in 5 sub and find lowest and highest marks

marks = []
for i in range(5):
    marks.append(int(input("Enter marks: ")))

marks.sort()
print("Highest marks: ", marks[-1])
print("Lowest marks: ", marks[0])