import random

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append({ "rank": rank["rank"], "value": rank["value"]})

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        card_dealt = []
        for i in range(n):
            card = self.cards.pop()
            card_dealt.append(card)
        return card_dealt

# Create a deck instance
deck1 = Deck()
deck2=Deck()
deck1.shuffle()
print(deck1.cards)