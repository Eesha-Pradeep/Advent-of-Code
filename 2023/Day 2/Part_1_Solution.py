with open("input.txt", "r") as f:
  lines = f.readlines()

game_sum = 0
coloursd = {"green":13, "red":12, "blue":14}
for i in lines:

  new_con = True

  for k in coloursd:
    ind = 0
    count = i.count(k)
    for j in range(count):
      ind = i.find(k, ind+1)
      if i[ind-3:ind-1].isdigit():
        balls_no = int(i[ind-3:ind-1])
      else:
        balls_no = int(i[ind-2])

      if balls_no>coloursd[k]:
        con = False
        break
    else:
      con = True

    new_con = con and new_con

  if not new_con:
    continue

  if i[5:7].isdigit():
    game_sum+=int(i[5:7])
  else:
    game_sum+=int(i[5])

print(game_sum)