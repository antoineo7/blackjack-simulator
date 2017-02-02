from functions import *

decks = 1
penetration = 0.5


#Creating Bank
Person(7, np.inf,"Georges",'bank')

#ini cards
Card.deck_init(decks,penetration)

p1 = Person(2,1000,"Pierre",'naif')
p2 = Person(3,1000,"Marc",'basic')
p3 = Person(4,1000,"André",'bank')
p4 = Person(5,1000,"Franck",'bank')

play_1_turn()