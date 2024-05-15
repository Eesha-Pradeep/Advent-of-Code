with open("input.txt", "r") as f:
  lines = f.readlines()
full = "".join(lines)
i, j = 0, 0
houses = [(0,0)]
count = 1
for k in full:
  if k == "^":
    j+=1
  elif k == "v":
    j-=1
  elif k == ">":
    i+=1
  else:
    i-=1
  if (i,j) not in houses:
    houses.append((i,j))
    count+=1
print(count)