with open("input.txt", "r") as f:
  lines = f.readlines()

values = {"2":"A", "3":"B", "4":"C", "5":"D", "6":"E", "7":"F", "8":"G", "9":"H", "T":"I", "J":"J", "Q":"K", "K":"L", "A":"M"}

#cleaning input data
bids = []
hands = []
for i in lines:
  hand = ""
  for j in range(5):
    hand += values[i[j]]
  bids.append(int(i[6:]))
  hands.append(hand)

#assigning bids to new hand values
hand_to_bid = {}
for i,j in zip(hands, range(len(bids))):
  hand_to_bid[i] = bids[j]

# initialising 7 types:
# 1) five of a kind
five_oak = []
# 2) four of a kind
four_oak = []
# 3) full house
full_house = []
# 4) three of a kind
three_oak = []
# 5) two pair
two_pair = []
# 6) one pair
one_pair = []
# 7) high card
high_card = []

for i in hands:
  if len(set(i))==5:
    high_card.append(i)
  elif len(set(i))==4:
    one_pair.append(i)
  elif len(set(i))==3:
    for j in i:
      if i.count(j)==3:
        three_oak.append(i)
        break
    else:
      two_pair.append(i)
  elif len(set(i))==2:
    z = list(set(i))
    if i.count(z[0])==3 or i.count(z[0])==2:
      full_house.append(i)
    else:
      four_oak.append(i)
  else:
    five_oak.append(i)


# getting order of hands
order = []
for i in [five_oak, four_oak, full_house, three_oak, two_pair, one_pair, high_card]:
  c = sorted(i, reverse=True)
  order.extend(c)

# getting order of bids
order_bid = []
for i in order:
  order_bid.append(hand_to_bid[i])


# getting final winnings
winnings = []
for i in order_bid:
  winnings.append(i*(len(order_bid)-order_bid.index(i)))


# final output
print(sum(winnings))
