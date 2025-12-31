# Tricky Ace
# Ganela Mayo-Johnson
# May 20th, 2025

import random
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#CREATING
suits = ["spades", "clubs", "hearts", "diamonds"]
values = {"ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
"10": 10, "jack": 11, "queen": 12}
deck = [(value, suit) for suit in suits for value in values]
discard_pile = []

#SHUFFLING
random.shuffle(deck)

#DEALING
player_hand = deck[:8]
computer_hand = deck[8:16]
deck = deck[16:]

#BEGINNING
player_score = 0
computer_score = 0
lead_player = random.choice(["player", "computer"])
round_number = 1
round_scores = []
start_time = time.time()

#DETERMINING
while len(player_hand) > 0 and (player_score < 9 and computer_score < 9):
    print(f"\nRound {round_number}")

    print("Your hand:\n")
    i = 0
    for card in player_hand:
        print(f"{i}: {card[0]} of {card[1]}")
        i += 1
    
    if lead_player == "player":
        choice = int(input("\nChoose a card from your hand to lead with (0-{}): ".format(len(player_hand)-1)))
        player_card = player_hand.pop(choice)
        
        same_suit = [c for c in computer_hand if c[1] == player_card[1]]
        if same_suit:
            computer_card = max(same_suit, key=lambda c: values[c[0]])
            computer_hand.remove(computer_card)
        else:
            computer_card = random.choice(computer_hand)
            computer_hand.remove(computer_card)
    
    else:
        computer_card = random.choice(computer_hand)
        computer_hand.remove(computer_card)
        print(f"Computer leads with {computer_card[0]} of {computer_card[1]}")
        
        valid_choices = [i for i, c in enumerate(player_hand) if c[1] == computer_card[1]]
        if valid_choices:
            choice = int(input(f"Choose a card in suit {computer_card[1]} (options: {valid_choices}): "))
        else:
            choice = int(input("No matching suit. Choose another card:"))
        player_card = player_hand.pop(choice)

    #CHOOSING
    print ("Computer is thinking....")
    time.sleep(1)

    #SHOWING
    print(f"Player plays: {player_card[0]} of {player_card[1]}")
    print(f"Computer plays: {computer_card[0]} of {computer_card[1]}")

    #OUTCOME
    lead_suit = player_card[1] if lead_player == "player" else computer_card[1]
    if player_card[1] == lead_suit and computer_card[1] == lead_suit:
        winner = "player" if values[player_card[0]] > values[computer_card[0]] else "computer"

    elif player_card[1] == lead_suit:
        winner = "player"
    else:
        winner = "computer"
    
    if winner == "player":
        player_score += 1
        lead_player = "player"
        print("You win the round!")

    else:
        computer_score += 1
        lead_player = "computer"
        print("Computer wins the round!")

    time.sleep (1)

    #RECORDING
    round_scores.append({
        "Round": round_number,
        "Player": player_score,
        "Computer": computer_score
    })

    #DISCARDING
    if deck:
        discarded = deck.pop()
        discard_pile.append(discarded)
        print(f"Card discarded from deck: {discarded[0]} of {discarded[1]}")

    #REFILLING HAND
    if len(player_hand) == 4 and len(deck) >= 8:
        player_hand += deck[:4]
        computer_hand += deck[4:8]
        deck = deck[8:]
        print("Both players must draw 4 more cards.")

    round_number += 1

    #END
    if player_score == 9 and computer_score > 0:
        break
    if computer_score == 9 and player_score > 0:
        break
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)

#RESULTS
print("\nGAME OVER")
print(f"Game duration was: {elapsed} seconds.\n")
if player_score == 0 and computer_score == 16:
    print("You shot the moon! You win with 17 points!")
elif computer_score == 0 and player_score == 16:
    print("Computer shot the moon and wins with 17 points!")
else:
    print(f"Final Score — Player: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("Computer wins!")

#GRAPH
df = pd.DataFrame(round_scores)
sns.lineplot(x = "Round", y = "value", hue = "variable", data = pd.melt(df, ["Round"]))
plt.title("Score Progress")
plt.xlabel("Round")
plt.ylabel("Score")
plt.show()
