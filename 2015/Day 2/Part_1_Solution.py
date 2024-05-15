with open("input.txt", "r") as f:
  lines = f.readlines()
a=0
for i in lines:
  if "\n" in i:
    lines[a] = i[:-1]
  a+=1
a=0
for i in lines:
  lines[a] = [int(k) for k in i.split("x")]
  a+=1

def surfaces(lbh):
  l = lbh[0]
  b = lbh[1]
  h = lbh[2]
  return 2*(l*b+b*h+l*h) + min([l*b,b*h,l*h])

total = 0
for i in lines:
  total += surfaces(i)
print(total)