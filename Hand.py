import numpy as np
from Card import *

def custom_sum_2(e1,e2):
    tab2 = []
    if min(len(e1),len(e2))>1:
        for elem1 in e1:
            for elem2 in e2:
                tab2.append(elem1 + elem2)
        return np.array(tab2)
    else:
        return np.array(e1 + e2)

def custom_sum(tab):
    sum = np.array([0])
    for k in range(len(tab)):
        sum = custom_sum_2(sum,tab[k])
    return sum


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.ace = False
        self.BJ = False
        self.light = False

    def add_card(self,card,display=True):
        self.cards.append(card)
        if card.value == 'Ace':
            self.ace = True
        self.calc_score(display=display)

    def calc_score(self,display=True):
        self.light = False
        self.BJ = False
        self.ace = False
        val = {'Ace':[1,11],'King':[10],'Queen':[10],'Jack':[10],'10':[10],'9':[9],'8':[8],'7':[7],'6':[6],
               '5':[5],'4':[4],'3':[3],'2':[2]}
        liste = custom_sum([np.array(val[card.value]) for card in self.cards])
        if len(liste)>1:
            self.ace = True
            if liste.min()>21:
                self.score= liste.min()
            else:
                condList = [liste<=21]
                choiceList = [liste]
                self.score = np.select(condList,choiceList).max()
                if self.score>liste.min():
                    self.light = True
        else:
            self.score = liste[0]
        if self.score == 21 and len(self.cards)==2:
            self.BJ=True
            if display:
                print("Blackjack !")

