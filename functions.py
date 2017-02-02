from Person import *

def bet(display=True):
    if display:
        print("--------------Bets--------------------")
    for player in Person.list[:-1]: #appart from the bank
        player.bid(display=display)
    
def distribution(display=True):
    if len(Card.deck)<=len(Card.list)*Card.penetration_rate:
        Card.shuffle(display=display)
    if display:
        print("-------------Distribution-------------")
    for player in Person.list[:-1]:
        assert isinstance(player, Person)
        player.get_card(display=display)
    c1 = Card('Ace','Spades')
    h1 = Hand()
    h1.add_card(c1)
    Person.list[-1].hands = [h1]
    for player in Person.list[:-1]:
        player.get_card(display=display)
    if display:
        print("RC : {0}  TC : {1}".format(round(Card.real_count,1),round(Card.true_count,1)))

def game(display=True):
    if display:
        print("-------------game-------------")
    if Person.list[-1].hands[0].ace == True:
        if display:
            print("Insurances available.")
        for player in Person.list[:-1]:
            player.insurance = player.get_decision('insurance',display=False)
            if display and player.insurance:
                player.insuranceBet = player.bet[0]//2
                if display:
                    print(player.name+" takes insurance for $"+str(player.insuranceBet))
            player.coins-=player.insuranceBet

    for player in Person.list[:-1]:
        notEndTurn=True
        while notEndTurn:
            decision = player.get_decision('card',display=display)
            if decision == 'Double' :
                player.get_card(display=display)
                b = player.bet[player.active_hand]
                player.coins-=b
                player.bet[player.active_hand]+=b
                notEndTurn = False
            if decision == 'Hit' :
                player.get_card(display=display)
            if decision == 'Stand' :
                notEndTurn = False
            if decision == 'Split' :
                h1 = Hand()
                h1.add_card(player.hands[player.active_hand].cards[0])
                h2 = Hand()
                h2.add_card(player.hands[player.active_hand].cards[1])
                player.hands.pop(player.active_hand)
                player.hands.insert(player.active_hand,h1)
                player.hands.insert(player.active_hand+1, h2)
                b = player.bet[player.active_hand]
                player.bet.insert(player.active_hand,b)
                player.coins-=b
            if player.hands[player.active_hand].score>20:
                notEndTurn = False
            if (notEndTurn == False) and player.active_hand<len(player.hands)-1:
                notEndTurn = True
                player.active_hand+=1
        player.active_hand=0
        if display:
            print(player.bet,player.coins)

def end(display=True):
    bank = Person.list[-1]
    while bank.hands[0].score<17:
        bank.get_card(display=display)
        if bank.hands[0].BJ and display:
            print("BlackJack for the bank !")

def pay(display=True):
    bank_hand = Person.list[-1].hands[0]
    for player in Person.list[:-1]:
        if Person.list[-1].hands[0].BJ and player.insurance:
            player.insurance = False
            player.coins += 3*player.insuranceBet  #pay 2:1
            player.insuranceBet = 0
        for k in range(len(player.bet)):

            hand = player.hands[k]
            bet = player.bet[k]
            player.bet[k]=0
            if hand.score>21:
                pass
            else:
                if bank_hand.BJ:
                    if hand.BJ:
                        player.coins+=bet
                    else:
                        pass
                else :
                    if hand.BJ:
                        player.coins+=(bet*5/2)
                    else:
                        if hand.score>bank_hand.score or bank_hand.score>21:
                            player.coins += (bet * 4 / 2)
                        if hand.score==bank_hand.score:
                            player.coins += (bet)
        if display:
            print(player.coins)
    for player in Person.list:  #Free Hands
        player.hands = [Hand()]
        player.abort = False


def play_1_turn(display=True):
    bet(display=display)
    distribution(display=display)
    game(display=display)
    end(display=display)
    pay(display=display)



