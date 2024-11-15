# 1A. use a for loop to print a square of size n = 5

n = 5
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

# 1B. use a for loop to print a triangle of size n = 9

n = 10
for i in range(n):
  for j in range(i):
    print("*",end=" ")
  print()

# 1C. use a for loop to print a checkerboard of size n = 8 with white and '*' cells.

n = 8
for i in range(n):
  for j in range(n):
    if (i + j) % 2 == 0:
      print(" ",end=" ")
    else:
      print("*", end=" ")
  print()

# 2A. use a while loop to print a square of size n = 5

i = 0
n = 5
while i < n:
  j = 0
  while j < n:
    print("X",end=" ")
    j = j + 1
  i = i + 1
  print()

# 2B. use a while loop to print a triangle of size n = 9

i = 0
n = 10
while i < n:
  j = 0
  while j < i:
    print("X", end=" ")
    j = j + 1
  i = i + 1
  print()

# 2C. use a while loop to print a checkerboard of size n = 8 with white and '*' cells

i = 0
n = 8
while i <= n:
  j = 0
  while j <= n:
    if (i + j) % 2 == 0:
      print(" ",end=" ")
    else:
      print("*", end=" ")
    j = j + 1
  i = i + 1
  print()

# 3. print a square of size n = 20
#    for vertical boundaries use '|'
#    for horizontal boundaries use '-'
#    for corners use '*'

n = 20
for i in range(n): # row
  for j in range(n): # column
    if j == 0 and i == 0 or j == (n-1) and i == (n-1) or j == 0 and i == (n-1) or j == (n-1) and i == 0:
      print("*", end=" ")
    elif i == 0 or i == (n - 1):
      print("-", end=" ")
    elif j == 0 or j == (n - 1):
      print("|", end=" ")
    else:
      print(" ", end=" ")
  print()

