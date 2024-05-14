with open("input.txt", "r") as f:
  lines = f.readlines()
full = "".join(lines)
floor = 0
a=-1
for i in full:
  a+=1
  if floor==-1:
    break
  if i=="(":
    floor+=1
  else:
    floor-=1
print(a)