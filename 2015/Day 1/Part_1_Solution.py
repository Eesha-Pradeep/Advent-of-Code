with open("input.txt", "r") as f:
  lines = f.readlines()
full = "".join(lines)
floor = 0
for i in full:
  if i=="(":
    floor+=1
  else:
    floor-=1
print(floor)