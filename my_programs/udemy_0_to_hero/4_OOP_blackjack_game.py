import random

"""
GAME PLAY:
To play a hand of Blackjack the following steps must be followed:
    - Create a deck of 52 cards
    - Shuffle the deck
    - Ask the Player for their bet
    - Make sure that the Player's bet does not exceed their available chips
    - Deal two cards to the Dealer and two cards to the Player
    - Show only one of the Dealer's cards, the other remains hidden
    - Show both of the Player's cards
    - Ask the Player if they wish to Hit, and take another card
    - If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    - If Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
    - Determine the winner and adjust the Player's chips accordingly
    - Ask the Player if they'd like to play again
"""

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True          # to indicate if 'human' player is playing or not
game = True             # to indicate of the game will be played repeatedly or not

# player_chip_balance = 100             # use this later to make it a global rolling variable


# CLASSES
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_string = ''
        for card in self.deck:
            deck_string += '\n' + card.__str__()
        return 'The deck has:' + deck_string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value += 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# FUNCTIONS DEFINITIONS
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips would you like to bet?: "))
        except ValueError:
            print("Invalid entry!")
        else:
            if chips.bet > chips.total:
                print(f'Bet can not be higher than {chips.total}.')
            else:
                break


def show_some(player_hand, dealer_hand):
    print("\nDealer's Hand:")
    print("\t<card hidden>")
    print('\t', dealer_hand.cards[1])
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n\t')


def show_all(player_hand, dealer_hand):
    print("\nDealer's Hand:", *dealer_hand.cards, sep='\n\t')
    print("\nDealer's Value =", dealer_hand.value)
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n\t')
    print("\nPlayer's Value =", player_hand.value)


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, player_hand):
    global playing

    while True:
        user_input = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
        if user_input == 'h':
            hit(deck, player_hand)
        elif user_input == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print('Invalid entry.\n')
            continue
        break


def player_busts(player_hand, dealer_hand, chips):
    print("\nPLAYER BUSTS!")
    chips.lose_bet()


def player_wins(player_hand, dealer_hand, chips):
    print("\nPLAYER WINS!")
    chips.win_bet()


def dealer_busts(player_hand, dealer_hand, chips):
    print("\nDEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player_hand, dealer_hand, chips):
    print("\nDEALER WINS!")
    chips.lose_bet()


def push(player_hand, dealer_hand):
    print("\nDEALER AND PLAYER TIE. ITS A PUSH!")


# GAMEPLAY
while game:
    print("\n----------------------------------------------------------------------")
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. '
          'Aces count as 1 or 11.')

    playing = True

    # Initialize Deck() object and shuffle
    deck = Deck()
    deck.shuffle()

    # Initialize player and dealer Hand() objects
    player_hand = Hand()
    dealer_hand = Hand()

    # Dealing two cards to player
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Dealing two cards to dealer
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Initializing Chips() object for player and taking bet
    chips = Chips()
    take_bet(chips)

    # Loop for one hand (round)
    while playing:                              # while player is playing
        show_some(player_hand, dealer_hand)
        hit_or_stand(deck, player_hand)
        if player_hand.value > 21:
            show_all(player_hand, dealer_hand)
            player_busts(player_hand, dealer_hand, chips)
            break
    else:                                       # when player has stopped playing and has value >= 21
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)      # showing all cards at this stage since the game is over

        # if, elif, else statements to decide game result.
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, chips)
            break

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, chips)

        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, chips)

        else:
            push(player_hand, dealer_hand)

    print(f"Player winnings stand at {chips.total}")

    # Loop to check if player wants to play another hand (round)
    while True:
        play_again = input("\nWould you like to play another hand? Enter 'y' or 'n': ")
        if play_again == 'y':
            break
        elif play_again == 'n':
            print('\nThanks for playing!')
            game = False
            break
        else:
            print('Invalid entry.')
            continue
