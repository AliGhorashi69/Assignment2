
import random

S=input("please enter S to start the game")


if S=="S":
    while True:
        a=int(random.uniform(1,6))
        print("the toss value is: ", a)
        if a==6:
            print("Great!!! you can repeat again") 
        else:
            break

print("The game is finished")
