with open("input.txt", "r") as f:
  lines = f.readlines()

def num_in_list(line):
  char = ""
  z = -1
  for i in line:
    z+=1
    if i.isdigit():
      char+=i
      if z==len(line)-1 or line[z+1]=="\n":
        num = int(char)
  return num

time = num_in_list(lines[0])
dist = num_in_list(lines[1])

ways = 0
for j in range(time+1):
  if j*(time-j) > dist:
    ways+=1

print(ways)