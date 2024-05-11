with open("input.txt", "r") as f:
  lines = f.readlines()

# getting the special character set
import string
b = (string.punctuation).partition(".")
b = b[0]+b[2]

#getting the indices of the special characters
char_ind = []
for i in lines:
  jind = -1
  inds = []
  for j in i:
    jind+=1
    if j in b:
      inds.append(jind)
  char_ind.append(inds)

# function to check if digit is next to special character
def check_pos(i, j):
  # i = line index
  # j = character index
  fal = False
  indl = [j]
  if j!=len(lines[i])-1:
    indl.append(j+1)
  if j!=0:
    indl.insert(0, j-1)

  # for lines other than first and last line
  if i not in [0, len(lines)-1]:
    char_lines = char_ind[i-1:i+2]
  # for the first line
  elif i == 0:
    char_lines = char_ind[i:i+2]
  # for the last line
  else:
    char_lines = char_ind[i-1:i+1]

  for k in char_lines:
    for l in indl:
      if l in k:
        fal = True
        break
    if fal==True:
      break
  return fal

# function to add numbers to the list
def add_num_to_list(input_list, x, line):
  #x = index of character
  back = line[x::-1]
  nob = ""
  for i in back:
    if i.isdigit():
      nob+=i
    else:
      break
  nob = nob[::-1]
  front = line[x+1:]
  nof = ""
  for i in front:
    if i.isdigit():
      nof+=i
    else:
      break
  x+=len(nof)
  no = nob+nof
  input_list.append(int(no))
  return x

# the working
num_list = []
lcount = -1
for i in lines:
  lcount+=1
  x = 0
  while x!=len(i)-1:
    j = i[x]
    if j.isdigit():
      next_to_char = check_pos(lcount, x)
      if next_to_char:
        x = add_num_to_list(num_list, x, i)
    x+=1

# the output
print(sum(num_list))