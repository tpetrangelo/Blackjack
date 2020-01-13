import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print ("{} of {}".format(self.value,self.suit))

class Deck():
    def __init__(self,numDecks):
        self.card = []
        self.numDecks = numDecks
        self.build(numDecks)

    def build(self, numDecks):
        i = 1
        while i <= numDecks:
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for v in range(1, 14):
                    if (v == 11):
                        v = "Jack"
                    elif (v == 12):
                        v = "Queen"
                    elif (v == 13):
                        v = "King"
                    elif (v == 1):
                        v = "Ace"
                    self.card.append(Card(s, v))
            i += 1
        
    def show(self):
        for c in self.card:
            c.show()

    def shuffle(self):
        for i in range(len(self.card) - 1, 0, -1):
            rand = random.randint(0, i)
            self.card[i], self.card[rand] = self.card[rand], self.card[i]
    
    def draw(self):
        return self.card.pop()

class Player:
    def __init__(self):
        self.hand = []

class Dealer:
    def __init__(self):
        self.hand = []

def main():

    numDecks = int(input("Enter the number of decks you want: "))

    deck = Deck(numDecks)
    deck.shuffle()
    

if __name__ == '__main__':
    main()