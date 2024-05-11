with open("input.txt", "r") as f:
  lines = f.readlines()

gamed = {}

for i in lines:
  j = i[10:-1].partition("|")
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

for i in range(len(wins)):
  for j in my_cards[i]:
    if j in wins[i]:
      wins[i].remove(j)


for i in wins:
  if len(i)!=10:
    pointl.append(2**((10-len(i))-1))


print(sum(pointl))
