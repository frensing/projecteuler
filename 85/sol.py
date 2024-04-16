goal = 2000000

cache = {(1,1): 1}
sum_cache = {1: 1}

def get_sum(x):
  if x in sum_cache:
    return sum_cache[x]
  return get_sum(x-1) + x

def calc(p):
  if p in cache:
    return cache[p]
  
  x, y = min(*p), max(*p)
  q = min(x, y), max(x, y) - 1
  cache[p] = calc(q) + y * get_sum(x)
  return cache[p]

y = 1
while True:
  r = calc((1, y))
  if r > goal:
    break
  y += 1
max_y = y

lower = 0
lower_p = None
upper = goal * 2
upper_p = None

for y in range(1, max_y):
  for x in range(1, y+1):
    p = (x, y)
    r = calc(p)
    if r <= goal and r > lower:
      lower = r
      lower_p = p

    if r >= goal:
      if r < upper:
        upper = r
        upper_p = p
      else:
        break

p = lower_p if abs(lower - goal) < abs(upper - goal) else upper_p
print(p[0] * p[1])
