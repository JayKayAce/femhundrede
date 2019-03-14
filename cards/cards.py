""" 
# 500 the card game
This is an object oriented version of the danish game 500.

The game is played by 2 to 4 players and each player gets
7 cards from a standard deck of 52 cards.
Jokers will be added later.


"""
import random



DECK = {"low" : range(2,10), 
        "high" :range(10,14),
        "Ace" : 14, 
        "suites": ["C", "H", "S", "D"],
        "suite_values": list(range(2,15))
        }

class Card:
    """
    A representation of a card in a card game

    """
    def __init__(self, suite:str, value:int):
        """ Instantiates a card object
        """
        self.suite = suite
        self.value = value
        self.position = None
        self.points = 0
    
    def __repr__(self):
        """ String representation of a card
        """
        if self.value <= 10:
            return f"{self.suite}{self.value}"
        elif self.value == 11:
            return f"{self.suite}J"
        elif self.value == 12:
            return f"{self.suite}Q"
        elif self.value == 13:
            return f"{self.suite}K"
        else:
            return f"{self.suite}A"
    
    def calculate_worth(self):
        """ Calculates the points of a card
        """
        if self.value in DECK["low"]:
            self.points = 5
        elif self.value in DECK["high"]:
            self.points = 10
        else:
            self.points = 15
    
    def get_neighbours(self):
        pass


class Discards:
    """
    Class for containing the discard pile of cards

    """
    def __init__(self):
        """ Creates an empty discard pile
        
        """
        self.topcard = None
        self.cards = {suite:[] for suite in DECK["suites"]}

    def add_card(self, card):
        self.cards[card.suite].append[card.value]
        self.topcard = card

class Pile:
    ""
    def __init__(self):
        """ Initializes the pile of cards from where to draw a card.
            
        **Parameters:**
        None
        
        """
        self.cards = [Card(s,v) for v in DECK["suite_values"] for s in DECK["suites"]]
    def __repr__(self):
        return f"""
        Clubs: {[c for c in self.cards if c.suite == 'C']}\n
        Hearts: {[c for c in self.cards if c.suite == 'H']}\n
        Spades: {[c for c in self.cards if c.suite == 'S']}\n
        Diamonds: {[c for c in self.cards if c.suite == 'D']}\n
        """