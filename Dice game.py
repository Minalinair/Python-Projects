import random
print("Welcome to the Dice Game")
print("Let's begin!")
print("Lets start with Player 1")
player1=int(input("enter the initial number from 1-6:"))
count1,count2=0,0
for i in range(1,player1+1):
        choice=int(input("Enter your choice (1-6):"))
        count1=count1+choice
print(f"You have scored {count1}")
print("Lets continue with Player 2")
player2=int(input("enter the initial number from 1-6:"))
for j in range(1,player2+1):
        choice2=int(input("Enter your choice (1-6):"))
        count2=count2+choice2
print(f"You have scored {count2}")
if count1>count2:
        print("Player 1 wins")
else:
        print("Player 2 wins")



