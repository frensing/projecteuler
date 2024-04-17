import functools

@functools.total_ordering
class Hand:
  def __init__(self, hand) -> None:
    self.cards = sorted(hand)
    self.rank = self.get_rank()


  def get_rank(self):
    self.best = self.get_high_card()
    
    # royal flush 10
    if self.is_royal():
      return 10
    
    # staight flush 9
    flush = self.is_flush()
    straight = self.is_straight()
    if flush and straight:
      return 9

    # four of a kind 8
    if self.get_quadruple():
      self.best = self.get_quadruple()
      return 8
    
    # full house 7
    pair = self.get_pair()
    triplet = self.get_triplet()
    if pair and triplet:
      self.best = pair + triplet
      return 7

    # flush 6
    if flush:
      return 6

    # straight 5
    if straight:
      return 5

    # triplet 4
    if triplet:
      self.best = triplet
      return 4

    # two pairs 3
    if self.get_two_pairs():
      self.best = self.get_two_pairs()
      return 3

    # pair 2
    if pair:
      self.best = pair
      return 2
    
    # high card 1
    return 1

  def get_high_card(self, id=0):
    return [sorted(self.cards)[-1 - id]]
  
  def is_flush(self):
    cards = {}
    for card in self.cards:
      cards[card.suit] = cards.get(card.suit, 0) + 1
    return max(cards.values()) == 5
  
  def is_straight(self, royal=False):
    indices = [c.get_order_index() for c in sorted(self.cards)]
    if royal:
      return indices == [*range(8, 13)]
    return indices == [*range(indices[0], indices[0] + 5)]
  
  def is_royal(self):
    return self.is_flush() and self.is_straight(royal=True)
  
  def get_multiple(self, n):
    cards = [k for k,_ in filter(lambda x: x[1] == n, self.count_card_values().items())]
    return cards
  
  def count_card_values(self):
    cards = {}
    for card in self.cards:
      cards[card] = cards.get(card, 0) + 1
    return cards
  
  def get_one_multiple(self, n):
    mult = self.get_multiple(n)
    if mult:
      return [max(mult)]
    return False
  
  def get_quadruple(self):
    return self.get_one_multiple(4)
  
  def get_triplet(self):
    return self.get_one_multiple(3)
  
  def get_pair(self):
    return self.get_one_multiple(2)
  
  def get_two_pairs(self):
    pairs = self.get_multiple(2)
    if len(pairs) == 2:
      return pairs
    return False
  
  
  def __eq__(self, other) -> bool:
    # should never be equal
    return False
  
  def __lt__(self, other):
    if self.rank != other.rank:
      return self.rank < other.rank
    
    # same rank, check rank cards
    for i in range(len(self.best) -1, -1, -1):
      if self.best[i] != other.best[i]:
        return self.best[i] < other.best[i]
    
    # same rank with same cards
    # check highest cards
    for i in range(5):
      if self.get_high_card(i) != other.get_high_card(i):
        return self.get_high_card(i) < other.get_high_card(i)
    
    print('err', self, other)
    raise Exception('why are the cards the same?')
  
  def __str__(self):
    return str(self.cards)