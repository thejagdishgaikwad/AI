import random

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Example usage
deck = create_deck()
print("Original Deck:")
print(deck)

shuffled = shuffle_deck(deck)
print("\nShuffled Deck:")
print(shuffled)

