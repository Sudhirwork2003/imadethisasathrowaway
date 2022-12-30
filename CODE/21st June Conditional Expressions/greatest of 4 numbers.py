num1 = int(input("give number: "))
num2 = int(input("give number: "))
num3 = int(input("give number: "))
num4 = int(input("give number: "))

if (num1>num2):
    win1 = num1
else:
    win1 = num2
if (num3>num4):
    win2 = num3
else:
    win2 = num4
if (win1>win2):
    print("the biggest number is: " + str(win1)) #use str because string can only be spliced to another string
else:
    print("the biggest number is: " + str(win2))
     