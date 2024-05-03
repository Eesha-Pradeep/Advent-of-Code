with open("input.txt", "r") as f:
    lines = f.readlines()

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_rev = [i[::-1] for i in numbers]
nums = []

for j in lines:
  num_start = ""
  d = {}
  d_r = {}

  #finding number at the start (actual numbers)
  for k in j:
    if k.isdigit():
      num_start = k
      start_num_ind = j.find(k)
      break

  #finding number at the end (actual numbers)
  if num_start:
    for k in j[::-1]:
      if k.isdigit():
        num_end = k
        end_num_ind = j[::-1].find(k)
        break

  #finding number at the start (in letters) --> 1
  for i in numbers:
    if i in j:
      d[i] = j.find(i)

  #finding number at the end (in letters) --> 1
  for i in numbers_rev:
    if i in j[::-1]:
      d_r[i] = j[::-1].find(i)

  #getting indices for starting and ending number letters
  if d:
    start_letter_ind = min(d.values())
    end_letter_ind = min(d_r.values())

  #getting values of numbers in letters with the indices
    for i in d:
      if d[i] == start_letter_ind:
        start_letter = i
    for i in d_r:
      if d_r[i] == end_letter_ind:
        end_letter = i[::-1]

  #getting the actual digits for the corresponding letter numbers
    for i in range(10):
      if numbers[i] == start_letter:
        start_letter = str(i)
      if numbers[i] == end_letter:
        end_letter = str(i)

    #getting the starting and ending digits
    if start_num_ind<start_letter_ind:
      start_dig = num_start
    else:
      start_dig = start_letter
    if end_num_ind<end_letter_ind:
      end_dig = num_end
    else:
      end_dig = end_letter

  else:
    start_dig = num_start
    end_dig = num_end

  #final number
  final_num = int(start_dig+end_dig)
  nums.append(final_num)

final_sum = sum(nums)

print("Numbers in the input text are:\n",nums)
print("Sum of those numbers is =",final_sum)