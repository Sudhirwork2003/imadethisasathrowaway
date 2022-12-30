a = "hi my name is <|NAME|>, and i like <|favorite car|>"
name = input("enter name here: ")
car = input("enter name here: ")
a = a.replace("<|NAME|>", name)
a = a.replace("<|favorite car|>", car)
print(a)
