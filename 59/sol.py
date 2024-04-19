import re

FILE = './59/cipher.txt'

with open(FILE) as f:
  text = [*map(int, f.readline().split(','))]

p = re.compile('[A-Za-z\s]*')
p_text = re.compile('[Tt]he')

def encode(key):
  def f(letter):
    return chr(letter ^ key)
  return f

def check(start_index, key):
  letters = text[start_index:50:3]
  encoded = ''.join(map(encode(key), letters))
  return p.fullmatch(encoded)

for x in range(97, 123):
  if not check(0, x):
    continue

  for y in range(97, 123):
    if not check(1, y):
      continue

    for z in range(97, 123):
      if not check(2, z):
        continue

      key = [x, y, z]
      encoded = ''
      s = 0
      for i in range(len(text)):
        xor = text[i] ^ key[i % 3]

        s += xor
        encoded += chr(xor)

      if p_text.search(encoded):
        print(key, encoded)
        print(s)
