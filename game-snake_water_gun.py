
import time
from gtts import gTTS
import os
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
        print(f"\nComp's Score - {lose}\n")
        print(f"{name}'s Score - {win}\n")

    elif comp =='s':
        if you =='w':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")

        elif you == 'g':
            win=win+1
            print("You Win!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")

    elif comp=='g':
        if you=='s':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")

        elif you=='w':
            win=win+1
            print("You Win!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")
            
    elif comp=='w':
        if you=='g':
            lose=lose+1
            print("You Lose!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")
            
        elif you=='s':
            win=win+1
            print("You Win!")
            print(f"\nComp's Score - {lose}\n")
            print(f"{name}'s Score - {win}\n")


name=str(input("\nPlease enter your name : "))

print(f"\n\t\t\t\t\t\t{name.upper()} VS COMPUTER")
finalName = name.upper()

gameDeclare = (f"{finalName} verses computer")

language = 'en'
output = gTTS(text=gameDeclare, lang=language, slow=False)
output.save("output1.mp3")
os.system("start output1.mp3")

time.sleep(8)
print(f"\n\t\t\t\t\tCOME ON {name} LET'S PLAY THE MATCH\n\n")
gameDeclare1 = (f"COME ON {name},LET'S PLAY THE MATCH")
language = 'en'
output = gTTS(text=gameDeclare1, lang=language, slow=False)
output.save("output2.mp3")
os.system("start output2.mp3")

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
    print(f"\n\nCONGRATULATIONS {finalName}, YOU ARE THE WINNER\n\n")
    myText1 = (f"CONGRATULATIONS {finalName}, YOU ARE THE WINNER")
    language = 'en'
    output = gTTS(text=myText1, lang=language, slow=False)
    output.save("output3.mp3")
    os.system("start output3.mp3")
else:
    print(f"\n\nYOU LOST BETTER LUCK NEXT TIME, {finalName}\n\n")
    myText2 = (f"YOU LOST BETTER LUCK NEXT TIME, {finalName}")
    language = 'en'
    output = gTTS(text=myText2, lang=language, slow=False)
    output.save("output4.mp3")
    os.system("start output4.mp3")
