import random

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

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
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, n):
        return [self.cards.pop() for _ in range(n)] if len(self.cards) >= n else []

class Hands:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += card.rank["value"]
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21   
    
    def display(self, show_all=False):
        owner = "Dealer's" if self.dealer else "Your"
        print(f"{owner} hand:")
        
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all and not self.is_blackjack():
                print("Hidden Card")
            else:
                print(card)   

        if not self.dealer:
            print("Value:", self.get_value())

class Game:
    def play(self):
        try:
            game_play = int(input("Enter the number of games you want to play: "))
        except ValueError:
            print("You must enter a number")
            return

        while game_play > 0:
            deck = Deck()
            deck.shuffle()
            player_hand = Hands()
            dealer_hand = Hands(dealer=True)

            # Deal initial two cards
            player_hand.add_card(deck.deal(2))
            dealer_hand.add_card(deck.deal(2))

            print("\n" + "*" * 30)
            player_hand.display()
            dealer_hand.display()

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand' (H/S): ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Invalid choice! Enter 'Hit' or 'Stand' (H/S): ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                game_play -= 1
                continue

            # Dealer plays
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))

            dealer_hand.display(show_all=True)

            print("\nFinal Results")
            print("Your hand:", player_hand.get_value())
            print("Dealer's hand:", dealer_hand.get_value())

            self.check_winner(player_hand, dealer_hand, True)

            game_play -= 1

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if player_hand.get_value() > 21:
            print("You busted! Dealer wins.")
            return True
        elif dealer_hand.get_value() > 21:
            print("Dealer busted! You win.")
            return True
        elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("It's a tie! Both got Blackjack.")
            return True
        elif player_hand.is_blackjack():
            print("You got Blackjack! You win.")
            return True
        elif dealer_hand.is_blackjack():
            print("Dealer got Blackjack! You lose.")
            return True

        if game_over:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")
            else:
                print("Dealer wins!")
            return True

        return False

g = Game()
g.play()
