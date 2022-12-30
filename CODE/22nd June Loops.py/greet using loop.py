N = str(input("Enter name: "))
for name in N:
    if name.startswith("S") or name.startswith("s"):
        print("Good Morning, " + N)
        break
else:
    print("no")
