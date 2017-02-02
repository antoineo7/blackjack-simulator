from functions import *

decks = 6
penetration = 0.5


#Creating Bank
Person(7, np.inf,"Georges",'bank')

#ini cards
Card.deck_init(decks,penetration)

p1 = Person(2,1000,"Pierre",'naif')
p2 = Person(3,1000,"Marc",'basic')
p3 = Person(4,1000,"André",'bank')
p4 = Person(5,1000,"Franck",'bank')

x1 = [1000]
x2 = [1000]
x3 = [1000]
x4 = [1000]

for k in range(200):
    play_1_turn()
    x1.append(p1.coins)
    x2.append(p2.coins)
    x3.append(p3.coins)
    x4.append(p4.coins)

x = [k for k in range(len(x1))]
plt.plot(x,x1,color='black')
plt.plot(x,x2,color='blue')
plt.plot(x,x3,color='red')
plt.plot(x,x4,color='green')
plt.show()


