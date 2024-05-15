with open("input.txt", "r") as f:
  lines = f.readlines()
full = "".join(lines)
houses = [(0,0)]
count = 1
def house_count(start, count):
  i,j = 0,0
  for k in full[start::2]:
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
  return count
count = house_count(0, 1)
count = house_count(1, count)
print(count)