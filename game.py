from cards import Card

NAMES = ["Henning", "Sofus", "Ib", "Karen"]

def check_set(set_playable: list, expected: list ) -> bool:
    """ helperfunction for testing playable sets
    
    **Params**:
    ------------------------
    set_playable: A set of cards 

    Description
    """
    return all(True for card in set_playable if card in expected)

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

        
    def draw(self, pile,* , n=1):
        """
        Player draws n card from a pile

        *Parameters:*
        pile : cards.Pile Determines where to draw the card from
        n : Determines number of cards to draw.
        """
        pass
    
    def lay_down_set(self):
        """ Checks if a player has a matching set of 3 cards to play to gain points
        """
        for suits, player_cards in self.hand:
            if len(player_cards) > 3:
                """ You need at least 3 cards to play for points
                """
                low = min(player_cards)
                high = max(player_cards)
                lowest_set = range(low, low + 3)
                highest_set = range(high - 2, high + 1)

            else: 
                continue
            


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