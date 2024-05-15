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

def ribbon(lbh):
  l = lbh[0]
  b = lbh[1]
  h = lbh[2]
  return l*b*h + min([2*(l+b),2*(b+h),2*(l+h)])

total = 0
for i in lines:
  total += ribbon(i)
print(total)