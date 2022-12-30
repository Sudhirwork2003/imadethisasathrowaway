m1 = int(input("student 1 score: "))  #use int(input()) for sorting user given integers
m2 = int(input("student 2 score: "))
m3 = int(input("student 3 score: "))
m4 = int(input("student 4 score: "))
m5 = int(input("student 5 score: "))
m6 = int(input("student 6 score: "))

marksheet = [m1, m2, m3, m4, m5, m6]
marksheet.sort()

print(marksheet)