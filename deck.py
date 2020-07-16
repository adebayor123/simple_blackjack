from card import Card
import random


class Deck:

    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        self._cards = []
        self.build()

    def build(self):
        for suit in Deck.suits:
            for i in range(1, 12):
                self._cards.append(Card(suit, i))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        """
        Fisher Yates Shuffle based shuffle
        :return: None
        """
        for i in range(len(self._cards)):
            index = random.randint(i, len(self._cards) - 1)
            self._cards[index], self._cards[i] = self._cards[i], self._cards[index]

    def draw(self):
        if self._cards:
            return self._cards.pop() #remove last element from deck