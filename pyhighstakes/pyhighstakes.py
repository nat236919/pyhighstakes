"""
PROJECT: PyHighStakes
DESCRIPTION: PyHighStakes is a library offering card decks and games
AUTHOR: Nuttaphat Arunoprayoch
DATE: 27-Jan-2020
"""
# Import libraries
import random
from typing import List, Dict, Any
from modules.blackjack import BlackJack


# Set up card decks
class CardDeck:
    """ Set up a standard deck of cards """

    def __init__(self) -> None:
        """ Initiate suites and their values """
        self.standard_cards = {
            'suits': ['clubs', 'diamonds', 'hearts', 'spades'],
            'values': list(range(2, 11)) + ['A', 'J', 'Q', 'K']
        }
        self.deck = None

    def get_deck(self) -> List[Dict[str, int]]:
        """ Get a whole deck of cards """
        self.deck = [{suit: value} for suit in self.standard_cards['suits'] for value in self.standard_cards['values']]
        return self.deck

    def shuffle(self) -> List[Dict[str, int]]:
        """ Shuffle a current deck """
        if not self.deck:
            self.deck = self.get_deck()

        return sorted(self.deck, key=lambda x: random.random())

    def play_blackjack(self) -> None:
        """ Play BlackJack game """
        if not self.deck:
            self.deck = self.shuffle()

        return BlackJack.play(self.deck)
