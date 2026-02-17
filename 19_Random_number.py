import random

#print(random.randint(1,100))

cards = ["2","3","4","5","6","7","8","9","Jack","Queen","King","Ace"]

random.shuffle(cards)

#print(cards)

rps = ["Rock","Paper","Scissors"]

rps1 = random.choice(rps)

rps2 = random.choice(rps)

print(f"Player 1 = {rps1} vs Player 2 = {rps2}")

if rps1 == rps2:
    print("Draw")
elif rps1 == "Rock" and rps2 == "Paper" or rps1 == "Paper" and rps2 == "Scissors" or rps1 == "Scissors" and rps2 == "Rock":
    print("Player 2 Won")
else:
    print("Player 1 Won")

