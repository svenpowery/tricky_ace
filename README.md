# Tricky Ace

Created by: Ganela Mayo-Johnson
Human vs. Computer Python card game
Uses a standard deck of 48 playing cards with the kings removed

## RULES

- Game begins with deck faced down shuffled and 8 random cards are dealt to you and the computer
- Computer will randomly determine which player will play a card first (also called leading)
- Each round, each player plays a card
- Whatever suit the lead player puts out, the other player must follow, if possible
- If the second player can't play a card in the same suit they can play any card they wish
- The player with the highest-value card in the “lead” suit wins that round, and that player earns a point
- The player who wins the point gets to lead in the next round
- After every round, one of the cards in the deck is removed and shown to both players (This has no effect on scoring/points)
- At the end of a round if both players are down to four cards they are each dealt four more cards
- This will happen twice in a game
- The third time both players are down to 4 cards, the deck will also have 4 cards left
- The players do not draw any more and will continue playing until they are out of cards 
- The player with the most points at the end of the game wins

## SPECIAL FEATURES

- Included time.sleep() function to simulate real-time actions
- After you choose a card, the computer will "think" for a moment before choosing its card to play back
- At the end of the game, a line graph will pop up displaying how the player and computer scores changed every round

## REQUIREMENTS TO RUN

- Must have Python 3.9+ version
- pandas, seaborn, and matplotlib must be installed
- install these libraries with: pip install pandas seaborn matplotlib
- Run in terminal with: python3 tricky_ace.py
