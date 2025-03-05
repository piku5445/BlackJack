import random
suits=["Clubs","Diamonds","Hearts","Spades"]
ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cards=[]
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)
def deal(n):
    card_dealt=[]
    for i in range (n):
       card=cards.pop()
       card_dealt.append(card)
    return card_dealt
shuffle()
card_dealt=deal(10)
card=card_dealt[0]
rank=card[1]
if(rank=="A"):
    value=11
elif rank =="J" or rank=="Q" or rank=="K":
    value=10
else:
    value=rank
rank_dict={"rank":rank,"value":value}
print(rank,value)