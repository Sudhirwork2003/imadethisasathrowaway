import random

def game(cpu, player1):
    if cpu == 's':
        if player1 == 'p':
            return True
        elif player1 == 's':
            return None
        elif player1 == 'c':
            return False
    elif cpu == 'p':
        if player1 == 's':
            return False
        elif player1 == 'p':
            return None
        elif player1 == 'c':
            return True
    elif cpu == 'c':
        if player1 == 's':
            return True
        elif player1 == 'p':
            return False
        elif player1 == 'c':
            return None
print("cpu player: Stone(s) Paper(p) Scissor(c)")
NPC = random.randint(1, 3)
if NPC == 1:
    cpu = 's'
elif NPC == 2:
    cpu = 'p'
elif NPC == 3:
    cpu = 'c' 
player1 = input("player 1: Stone(s) Paper(p) Scissor(c): ")

a = game(cpu, player1) 
if a == None:
    print("tied!")
elif a:
    print("player1 wins!")
else:
    print ("cpu wins!")