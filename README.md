# The cardgame 500

This project is a card game of 500, A danish cardgame , created solely for my own purpose.
I am testing out how to write multi module program from scratch.
The purpose of the game is to win enough games to reach 500 points in total.

## Playing the game

* Choose a starting player
* First round actions

1. Either "Draw top card from discards" or "Draw 1 card from the new pile"

* Remaining rounds actions:

1. Either "Draw card from pile" or "Draw top card from discards" or "Draw all cards from discard pile"
2. Play cards to table for points in suits of atleast 3 consecquitive cards
3. Play a card that can continue from an opponents cards on the desk.
4. Discard 1 card if any cards are left

### Rules of the game

* Number of players: 2 to 5
* Cards at start: 7
* Points:
* * Card 0-9: 5 points
* * 10, Jack, Queen, King: 10 points
* * Ace: 15 points

### Conditional rules

The following rules are condtional and depends on another event happening:

* The game ends, when a player discards the last card from his hand
* If a player draws all discards, he must play atleast a suit of 3 cards or take a penalty of -50 points
* If a player ends the game the cards points on the hand of opponent(s) are deducted from his game score, and it can go negative
