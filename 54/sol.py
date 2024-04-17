from Card import Card
from Hand import Hand

FILE = './54/poker.txt'

rounds = []
with open(FILE) as f:
  for line in f.readlines():
    line = line.strip().split()
    p1 = Hand([Card(c) for c in line[:5]])
    p2 = Hand([Card(c) for c in line[5:]])
    rounds.append((p1, p2))

s = 0
for rounds in rounds:
  p1, p2 = rounds

  s += int(p1 > p2)

print(s)
