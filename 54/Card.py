import functools

ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

@functools.total_ordering
class Card:
  def __init__(self, code) -> None:
    self.val = code[0]
    self.suit = code[1]

  def get_order_index(self):
    return ORDER.index(self.val)

  def __eq__(self, other) -> bool:
    return self.val == other.val

  def __lt__(self, other):
    return ORDER.index(self.val) < ORDER.index(other.val)
  
  def __hash__(self) -> int:
    return ORDER.index(self.val)

  def __repr__(self) -> str:
    return self.__str__()
  
  def __str__(self) -> str:
    return self.val + self.suit
