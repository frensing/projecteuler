
FILE = './81-path_sum/matrix.txt'

matrix = []
with open(FILE) as f:
  for line in f.readlines():
    line = [*map(int, line.strip().split(','))]
    matrix.append(line)

width = len(matrix[0])
height = len(matrix)

for x in range(1, width):
  matrix[0][x] += matrix[0][x-1]
for y in range(1, height):
  matrix[y][0] += matrix[y-1][0]

for y in range(1, height):
  for x in range(1, width):
    matrix[y][x] += min(matrix[y-1][x], matrix[y][x-1])

print(matrix[height-1][width-1])