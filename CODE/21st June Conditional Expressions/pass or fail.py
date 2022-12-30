sub1 = int(input("physics marks: "))
sub2 = int(input("maths marks: "))
sub3 = int(input("chemistry marks: "))

sum = sub1+sub2+sub3
perc = (sum/300)*100

if (sub1<33 or sub2<33 or sub3<33):
    print("Result: Fail" + str(perc))
elif (perc<45):
    print("Result: Fail" + str(perc))
else:
    print("Result: Pass.\nPercentage: " + str(perc))
