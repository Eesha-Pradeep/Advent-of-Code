with open("input.txt", "r") as f:
  lines = f.readlines()
a=0
for i in lines:
  if "\n" in i:
    lines[a] = i[:-1]
  a+=1
count = 0
for i in lines:
  n = False
  for j in ["ab", "cd", "pq", "xy"]:
    if j in i:
      n = True
      break
  ind = 1
  while ind!=len(i):
    if i[ind]==i[ind-1]:
      break
    ind+=1
  else:
    n = True
  vowel_count = 0
  for j in "aeiou":
    vowel_count+= i.count(j)
  if vowel_count<3:
    n = True
  if n:
    continue
  count +=1
print(count)