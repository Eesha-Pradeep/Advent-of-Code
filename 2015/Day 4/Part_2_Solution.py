import hashlib
no = 0
with open("input.txt", "r") as f:
  lines = f.readlines()
input = lines[0]
while True:
  value = input+str(no)
  hash = hashlib.md5(value.encode())
  if (hash.hexdigest()).startswith("0"*6):
    print(no)
    break
  no+=1