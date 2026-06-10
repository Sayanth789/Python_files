from dataclasses import dataclass 

@dataclass(order=True)
class Card:
    rank: str 
    suit: str 

    ranks = [str(n) for n in range(2, 10)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

card1 = Card('A', 'spades')
card2 = Card('C', 'hearts')

print(card1)
