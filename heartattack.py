from os import system
from random import randint
from time import sleep as sp
comp = randint(1,10)
print("!!Guess the number!!")
p = int(input("Enter your guess: "))
if p == comp:
    print("You Won")
else:
    for _ in range(7,1,-1):
        print("deleting system32.. in ",_," ",end="\r")
        sp(1)
    system("shutdown /h")