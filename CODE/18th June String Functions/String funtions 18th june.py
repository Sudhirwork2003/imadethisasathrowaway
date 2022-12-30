greeeting = "good morning "
name = "sudhir"
c = (greeeting + name)
print(name[4])
print(name[0])
print(name[0:4])
print(name[0:2] + name[0:2])
#Use (-1 ) to access the last element
print(name[-1])
print(len(name))
print(name.endswith("r")) #this will give you a true or false value on whether or not variable ends with your given input
a = input("just type anything: ")
a = str(a)
print(greeeting.count("o"))
print(greeeting.startswith(a))