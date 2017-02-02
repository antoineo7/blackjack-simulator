from Hand import *


class Person:
    list = []

    def __init__(self, spot, coins, name, strategy):
        self.spot = spot  # number in range(0-7) where 7 is the bank and 0 the first player
        self.coins = coins
        self.hands = [Hand()]
        self.bet = [0]
        self.active_hand=0
        self.name = name
        self.strategy = strategy
        self.insurance = False
        self.abort = False
        self.insuranceBet = 0
        Person.list.append(self)
        Person.list.sort(key=lambda person: person.spot)
        print(self.name+' sits at spot '+str(self.spot)+' with {0} coins'.format(str(self.coins)))

    def remove(self):
        print(self.name+" left the table.")
        Person.list.remove(self)
        del self
        pass

    def get_card(self,display=True):
        new_card = Card.pick()
        self.hands[self.active_hand].add_card(new_card,display=display)
        if display:
            print(self.name+' gets '+new_card.verbose()+"        Score :",[hand.score for hand in self.hands])
            if self.hands[self.active_hand].score >21:
                print("Burned !")

    def decision_naive(self,type):
        if type == 'insurance': return [True,False][rd.randint(0,1)]
        bank_score = Person.list[-1].hands[0].score
        score = self.hands[self.active_hand].score
        if (score<=11) or (score<=16 and bank_score>=7) or(score==12 and (bank_score==2 or bank_score==3)):
            return 'Hit'
        else:
            return 'Stand'

    def decision_basic(self,type):
        if type == 'insurance': return False
        if type == 'card':
            bank_score = Person.list[-1].hands[0].score
            chart = pd.read_csv('basic_strategy.csv',sep=';').set_index('Player')
            hand = self.hands[self.active_hand]
            if len(hand.cards)==2:
                if hand.cards[0].score == hand.cards[1].score:
                    return chart[str(bank_score)][str(hand.cards[0].score)+str(hand.cards[0].score)]
            if hand.ace and hand.light and len(hand.cards)>=2:
                return chart[str(bank_score)]['A'+str(hand.score-11)]
            return chart[str(bank_score)][str(hand.score)]


    def get_decision(self,type,display=True): #type = 'card' or 'insurance'
        if self.strategy == 'input':
            decision = input('Action ({0}): '.format(type))
        if self.strategy == 'naif':
            decision = self.decision_naive(type)
        if self.strategy == 'basic':
            decision = self.decision_basic(type)
        if self.strategy == 'random':
            if type == 'card':
                decision = ['Hit','Stand'][rd.randint(0,1)]
            if type == 'insurance':
                decision = [True,False][rd.randint(0,1)]
        if self.strategy == 'bank':
            if type == 'card':
                if self.hands[0].score>16:
                    decision = 'Stand'
                else:
                    decision = 'Hit'
            if type == 'insurance':
                return False
        if display:
            if type == 'card':
                print(self.name+' decides to '+decision)
            if type == 'insurance' and decision == True:
                print(self.name+' takes insurance.')
        return decision

    def bid(self,display=True):
        if self.name == 'Antoine':
            bet = int(input('Bet : '))
        else :
            if self.coins>=2:
                bet = 2
            else:
                bet = self.coins
        if display:
            print(self.name+' bets $'+str(bet))
        self.coins-=bet
        self.bet = [bet]
