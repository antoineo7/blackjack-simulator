import random as rd
import pandas as pd
import matplotlib.pyplot as plt

class Card:
    number = 0
    list = [] #save all Card instances
    deck = []
    penetration_rate = 0
    true_count = 0
    real_count = 0

    @staticmethod
    def deck_init(number_of_decks,penetration):
        Card.penetration_rate = penetration
        values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        colors = ['Spades', 'Diamonds', 'Heart', 'Clubs']
        for n in range(number_of_decks):
            for val in values:
                for col in colors:
                    Card(val, col)
        print("Cards inititialised.")
        Card.shuffle()
        return

    @staticmethod
    def shuffle(display=True):
        if display:
            print('Cards shuffled !')
        Card.deck = rd.sample(Card.list, Card.number)
        Card.true_count = 0
        Card.real_count = 0

    @staticmethod
    def pick(): #return first deck's card and remove it from the deck
        if len(Card.deck)>0:
            picked_card =  Card.deck.pop()
            Card.true_count+=picked_card.count
            if len(Card.deck)>0:
                Card.real_count = 52*Card.true_count/len(Card.deck)
            return picked_card
        else:
            print("Can't pick card from empty deck")
            pass
        
    def reset_deck(self):
        Card.number = 0
        Card.list = []
        Card.deck = []
        Card.penetration_rate = 0
        Card.true_count = 0
        Card.real_count = 0
        pass

    def __init__(self, value, color):
        self.value = value
        self.color = color
        Card.list.append(self)
        Card.number += 1
        self.score = {'Ace':[11],'King':[10],'Queen':[10],'Jack':[10],'10':[10],'9':[9],'8':[8],'7':[7],'6':[6],
               '5':[5],'4':[4],'3':[3],'2':[2]}[self.value][0]
        self.count=[self.score>9,abs(self.score-8)<2,self.score<7].index(True)-1

    def verbose(self):
        return "{0} of {1}".format(self.value, self.color)

