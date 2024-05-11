with open("input.txt", "r") as f:
  lines = f.readlines()

def num_in_list(line):
  lst = []
  char = ""
  z = -1
  for i in line:
    z+=1
    if i.isdigit():
      char+=i
      if z==len(line)-1:
        lst.append(int(char))
    else:
      if char:
        lst.append(int(char))
        char = ""
  return lst

# getting the time and distances 
time = num_in_list(lines[0])
dist = num_in_list(lines[1])

output = 1
for i in range(len(time)):
  t = time[i]
  d = dist[i]
  ways = 0
  for j in range(t+1):
    if j*(t-j) > d:
      ways+=1
  output*=ways

print(output)