import unittest
from cards import Card
from cards import Pile

class CardsTest(unittest.TestCase):
    def test_numeric_card_creation(self):
        """
        Tests that a numeric card is created correctly
        """
        c = Card("S",9)
        self.assertEqual(str(c),"S9")
    
    def test_jack_card_creation(self):
        c = Card("S",11)
        self.assertEqual(str(c),"SJ")
    
    def test_queen_card_creation(self):
        c = Card("S",12)
        self.assertEqual(str(c),"SQ")

    def test_King_card_creation(self):
        c = Card("S",13)
        self.assertEqual(str(c),"SK")

    def test_ace_card_creation(self):
        c = Card("S",14)
        self.assertEqual(str(c),"SA")


class PileTest(unittest.TestCase):
    def test_creation(self):
        p = Pile()
        self.assertEqual(len(p.cards),52)


if __name__ == "__main__":
    unittest.main()