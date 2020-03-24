#Anything Less than 5 is rock
#Anything Greater than 5 but less than 10 is paper
#Anything Greater than 10 is scissors
import random, sys 

print("Welcome to Rock Paper Scissors! By Tyler Perry")
def playgame():
    c = random.randint(0, 30) 
    if ((c > 0) and (c < 30)):
        if (c < 10):
            cc = "Rock"
        if ((c > 10) and (c < 20)):
            cc = "Paper"
        if (c > 20):
            cc = "Scissors"
    u = input("Choose rock, paper, or scissors by typing it: ")
    cc = "NA"
    if ((u == "scissor") or ("S" or "s" in u[0]) and (cc == "Paper")):
        print("You won, The Computer chose Paper!")
    if ((u == "scissor") or ("S" or "s" in u[0]) and (cc == "Scissors")):
        print("It was a draw, both you and the Computer chose scissors.")
    if ((u == "scissor") or ("S" or "s" in u[0]) and (cc == "Rock")):
        print("You Lost, The Computer chose Rock")
    if ((u == "rock") or ("R" or "r" in u[0]) and (cc == "Rock")):
        print("It was a draw, both you and the Computer chose Rock.")
    if ((u == "rock") or ("R" or "r" in u[0]) and (cc == "Scissors")):
        print("You won, The Computer chose Scissors!")
    if ((u == "rock") or ("R" or "r" in u[0]) and (cc == "Paper")):
        print("You lost, the Computer chose Paper.")
    if ((u == "paper") or ("P" or "p" in u[0]) and (cc == "Rock")):
        print("You won, The Computer chose Rock.")
    if ((u == "paper") or ("P" or "p" in u[0]) and (cc == "Scissors")):
        print("You lost, The computer chose scissors.")
    if ((u == "paper") or ("P" or "p" in u[0]) and (cc == "Paper")):
        print("It was a draw, both you and the Computer chose Paper.")

isPlaying = True

while(isPlaying==True):
    playgame()
    print("Would you like to play again?")
    if ((not "Y" in input("(Y)es/(N)o: ")[0]) or (not "y" in input("(Y)es/(N)o: ")[0])):
        isPlaying = False
        print("Now exiting. Goodbye!")
