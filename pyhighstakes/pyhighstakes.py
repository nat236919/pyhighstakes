"""
PROJECT: PyHighStakes
DESCRIPTION: PyHighStakes is a library offering card decks and games
AUTHOR: Nuttaphat Arunoprayoch
DATE: 27-Jan-2020
"""
# Import libraries
import random
from typing import List, Dict, Any


# Set up card decks
class CardDeck:
    """ Set up a standard deck of cards """
    
    def __init__(self) -> None:
        """ Initiate suites and their values """
        self.deck = {
            'suits': ['clubs', 'diamonds', 'hearts', 'spades'],
            'values': list(range(2, 11)) + ['A', 'J', 'Q', 'K']
        }
    
    def get_deck(self) -> List[Dict[str, int]]:
        """ Get a whole deck of cards """
        return [{suit: value} for suit in self.deck['suits'] for value in self.deck['values']]
