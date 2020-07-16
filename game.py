from deck import Deck
from player import Player
from CardGame import CardGame

deck = Deck()
me = Player("Monty Python")
dealer = Player("Dealer", True)

game = CardGame(deck, me, dealer)