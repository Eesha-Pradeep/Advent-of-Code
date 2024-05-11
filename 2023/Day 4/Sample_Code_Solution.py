with open("input.txt", "r") as f:
  lines = f.readlines()

gamed = {}

for i in lines:
  j = i[8:-1].partition("|")
  gamed[j[0]] = j[2]

ngamed = {}
wins = []
win_cards = []
my_cards = []

for i in gamed:
  gamel = []
  num = ""
  for j in gamed[i]:
    if j.isdigit():
      num+=j
    else:
      if num:
        gamel.append(int(num))
        num = ""
  if num:
    gamel.append(int(num))
  my_cards.append(gamel)
  num = ""
  winl = []
  for j in i:
    if j.isdigit():
      num+=j
    else:
      if num:
        winl.append(int(num))
        num = ""
  win_cards.append(winl)
  wins.append(winl.copy())

pointl = []
print(wins)

for i in range(len(wins)):
  for j in my_cards[i]:
    if j in wins[i]:
      wins[i].remove(j)

print(wins)

for i in wins:
  if len(i)!=5:
    print("len = ", len(i))
    pointl.append(2**(4-len(i)))
    print("points =",2**(4-len(i)))


print(sum(pointl))