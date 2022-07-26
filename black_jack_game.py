import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        # only happens once upon creation of a new Deck
        self.all_cards = []
        for deck in range(5):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # remove one card from the list of all_cards
        return self.all_cards.pop()


def clear_hands(deck, dealer, player):
    deck.all_cards.extend(dealer.cards)
    deck.all_cards.extend(player.hand.cards)
    dealer.cards = []
    player.hand.cards = []


class Hand:
    def __init__(self):
        # hand is empty
        self.cards = []

    def hand_sum(self):
        sum_of_hand = 0
        for card in self.cards:
            sum_of_hand += card.value
        return sum_of_hand

    def __str__(self):
        str_cards = ""
        for card in self.cards:
            str_cards += f"{card}, "
        bj = ""
        if self.hand_sum() == 21:
            bj = "black jack!"
        return f"{str_cards[:len(str_cards) - 2]} |value {self.hand_sum()} {bj}"


class Player:

    def __init__(self, name, bank):
        self.hand = Hand()
        self.name = name
        self.bank = bank
        # A new player has no cards

    def get_bank(self):
        return self.bank

    def win(self, bet):
        self.bank += int(bet)

    def lose(self, bet):
        self.bank -= int(bet)

    def add_cards(self, new_cards):
        if type(new_cards) == (type([])):
            self.hand.cards.extend(new_cards)
        else:
            self.hand.cards.append(new_cards)


def lose_check(player):
    if player.bank <= 0:
        return True
    return False


def clear():
    print("\n" * 50)


def main():
    name = "Ovuvuevuevue Enyetuenwuevue Ugbemugbem Osas"  # input("Enter you name please: ")

    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Player(name, 1000)
    print(f"Welcome to the black jack game {name} good luck!!!")
    iteration = 0
    while True:
        playing = not lose_check(player)
        if not playing:
            print("Game Over")
            break

        print(f"bank: {player.bank}")
        if iteration > 0:
            time.sleep(5)
            clear()
        iteration += 1
        bet = input("please enter your bet : ")  # TO DO add bet validation
        # dealer.cards.append(deck.deal_one())
        clear_hands(deck, dealer, player)
        dealer.cards.append(deck.deal_one())
        player.add_cards(deck.deal_one())
        player.add_cards(deck.deal_one())
        while playing:
            print(f"dealer hand: {dealer}")
            print(f"player hand: {player.hand}")
            action = input("Do you want hit or stand ? (h/s)")
            while action == 'h':
                player.add_cards(deck.deal_one())
                print(f"player hand: {player.hand}")
                if player.hand.hand_sum() > 21:
                    print("Bust!")
                    player.lose(bet)
                    playing = False
                    break
                action = input("Do you want hit or stand ? (h/s)")

            if action == 's':
                print(f"player hand: {player.hand}")
                print(f"dealer hand: {dealer}")
                time.sleep(1)
                while dealer.hand_sum() <= 21:
                    if dealer.hand_sum() < player.hand.hand_sum():
                        dealer.cards.append(deck.deal_one())
                        print(f"dealer hand: {dealer}")
                        time.sleep(1)
                        if dealer.hand_sum() > 21:  # win
                            print(f"congratulations {name} you win {bet}")
                            player.win(bet)
                            playing = False
                            break
                    elif dealer.hand_sum() > player.hand.hand_sum():  # Lose
                        print(f" {name} you lost {bet}")
                        player.lose(bet)
                        playing = False
                        break
                    elif dealer.hand_sum() == player.hand.hand_sum():  # Tie
                        print(f"Push")
                        playing = False
                        break


if __name__ == "__main__":
    main()

    # strange bug with __str__()
