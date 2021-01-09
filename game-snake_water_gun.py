import random

lose=0
win=0

def gameWin(comp,you):
    global lose
    global win
    print(f"\n\nComputer chose {comp}\n")
    print(f"You choosed {you}\n")

    if comp==you:
        print("The game is tie!")
        print(f"\nComp Score - {lose}\n")
        print(f"Your Score - {win}\n")

    elif comp =='s':
        if you =='w':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")

        elif you == 'g':
            win=win+1
            print("You Win!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")

    elif comp=='g':
        if you=='s':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")

        elif you=='w':
            win=win+1
            print("You Win!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")
            
    elif comp=='w':
        if you=='g':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")
            
        elif you=='s':
            win=win+1
            print("You Win!")
            print(f"\nComp Score - {lose}\n")
            print(f"Your Score - {win}\n")



print("\n\nPlease enter the number of points you want to have in the match : ")
n=int(input())

while (win!=n and lose!=n):

    print("\n\nComputer Turn: Snake(s) Water(w) Gun(g) ?")
    ranNo = random.randint(1,4)           
    if ranNo==1:
        comp='s'
    elif ranNo==2:
        comp='w'
    elif ranNo==3:
        comp='g'

    you=input("Your Turn: Snake(s) Water(w) Gun(g) ?")
    
    a=gameWin(comp,you)
if win==n:
    print("\n\nCONGRATULATIONS, YOU ARE THE WINNER\n\n")
else:
    print("\n\nBETTER LUCK NEXT TIME\n\n")
