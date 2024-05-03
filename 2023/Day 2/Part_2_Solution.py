with open("input.txt", "r") as f:
  lines = f.readlines()

power_sum = 0
coloursd = {"green":13, "red":12, "blue":14}

for i in lines:

  power = 1

  for k in coloursd:

    count = i.count(k)
    ind = 0
    balls_min = 0

    for j in range(count):
      ind = i.find(k, ind+1)
      if i[ind-3:ind-1].isdigit():
        balls_no = int(i[ind-3:ind-1])
      else:
        balls_no = int(i[ind-2])

      if balls_no>balls_min:
        balls_min = balls_no

    power*=balls_min

  power_sum+=power
print(power_sum)