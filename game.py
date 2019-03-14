from cards import Card

NAMES = ["Henning", "Sofus", "Ib", "Karen"]

class Player:
    """
    Game respresentation of a player
    """

    def __init__(self, name):
        """ 
        """
        self.name = name
        self.points = 0
        self.hand = {}
        self.played_cards = {}

    def check_opponents_cards(self, opponent):
        """
        Check if a card in the hand can be played
        by checking players cards against the opponents played cards
        """
        pass

        
    def draw_card(self, pile,* , n=1):
        """
        Player draws n card from a pile

        *Parameters:*
        pile : cards.Pile Determines where to draw the card from
        n : Determines number of cards to draw.
        """
        pass
    
    def check_cards(self):
        """ Checks if a player has a matching set of 3 cards to play to gain points
        """
        pass

    


class Game_Loop:
    """ The game logic for playing the game.
    
    *Parameters:*
    None
    """
    def __init__(self, N:int):
        """ initializes a game with N players

        *parameters*
        N:int number of players 
        """
        pass