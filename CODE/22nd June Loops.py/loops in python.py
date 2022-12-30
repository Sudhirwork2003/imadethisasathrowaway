a = 1
while a<=10:
    print("OK " + str(a))  #here youll get output as "ok *value of a in current loop*"
    a = a + 1   #here the value of a will keep increasing by 1 after every loop. loop will pause after a isw greater than 15.

print("done")

L = [1, 2, 3, 4, 5, 6]
for numbers in L:
    print(L)   #this will cause the list of 6 numbers to print 6 times
    print(numbers)   #this will cause the 6 numbers to be printed seperately