def greet(name= "N/A"):
    print("Guten Tag, "+ name )

a = str(input("enter your name: "))
greet(a)
greet() #here the program wont show an error as we have set up a default argument, so in the case of an unspecified name, it will show us NA, as thats what we specified