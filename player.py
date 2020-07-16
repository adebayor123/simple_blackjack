class Player:

    def __init__(self, name, is_dealer=False):
        self._name = name
        self._is_dealer = is_dealer
        self._hand = []

    @property
    def name(self):
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer

    def draw(self, deck):
        self._hand.append(deck.draw())
        return self  # this allows method chain!

    def show_hand(self, reveal_card=False):
        if not self.is_dealer:
            for card in self._hand:
                card.show()
        else:
            # two scenarios
            # hide the last card
            for i in range(len(self._hand) - 1):
                self._hand[i].show()

            # if we need to show the last
            if reveal_card:
                self._hand[-1].show()
            else:
                print("X")

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value