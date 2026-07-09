import random
 
options = ("rock","paper","scissors")

player = None

computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock,paper,scissors): ")
print(f"player: {player}")
print(f"Computer: {computer}")

if player==computer:
    print("its a tie!")
elif player=="rock" and computer=="scissors":
    print("You won!")
elif player=="scissors" and computer=="paper":
    print("You won!")
elif player=="paper" and computer=="rock":
    print("You won!")
elif computer=="rock" and player=="scissors":
    print("Computer won!")
elif computer=="scissors" and player=="paper":
    print("Computer won!")
elif computer=="paper" and player=="rock":
    print("Computer won!")