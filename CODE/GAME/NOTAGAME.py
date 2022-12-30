import random

def game(cpu, player1):
    if cpu == 's':
        if player1 == 'p':
            print("hahahahaha loser!")
        elif player1 == 's':
            print("you lose! hahahaha!")
        elif player1 == 'c':
            print("hahahah noob!")
    elif cpu == 'p':
        if player1 == 's':
            print("you lose, punk!")
        elif player1 == 'p':
            print("you'll never win punk!")
        elif player1 == 'c':
            print("you really think you can win?")
    elif cpu == 'c':
        if player1 == 's':
            print("nope, you lose!")
        elif player1 == 'p':
            print("keep trying, you might just get a tie! hahahaha!")
        elif player1 == 'c':
            print("it's not gonna happen, give up!")
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