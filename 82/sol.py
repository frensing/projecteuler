import queue

FILE = './82/matrix.txt'

matrix = []
with open(FILE) as f:
  for line in f.readlines():
    line = [*map(int, line.strip().split(','))]
    matrix.append(line)

width = len(matrix[0])
height = len(matrix)

min_path_len = 0

q = queue.PriorityQueue()
for y in range(height):
  q.put((matrix[y][0], (0, y)))
visited = {}

while not q.empty():
  s, p = q.get()
  x, y = p
  if p in visited:
    continue

  visited[p] = True
  if x == width - 1:
    min_path_len = s
    break

  if x < width - 1:
    q.put((s + matrix[y][x+1], (x+1, y)))
  if y > 0:
    q.put((s + matrix[y-1][x], (x, y-1)))
  if y < height - 1:
    q.put((s + matrix[y+1][x], (x, y+1)))

print(min_path_len)