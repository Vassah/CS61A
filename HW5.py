#We are asked to reverse a list in place and return None
#We are not to use list methods or slicing, only index assignment
#So as to not use the __len__ list method...
def lengther(lz):
  vz = 0
  for i in lz:
    vz += 1
  return vz
#and the meat

def reverse_list(lz):
  n = lengther(lz) - 1
  i = 0
  while i<n:
  	lz[i], lz[n] = lz[n], lz[i]
  	i,n = i+1, n-1
  return None

listic = [5,4,3,2,1]
lzz = [4,3,2,1]
reverse_list(listic)
print(listic)
reverse_list(listic)
print(listic)
reverse_list(lzz)
print(lzz)
reverse_list(lzz)
print(lzz)

#Now Question 2
def card(n):
  assert type(n) == int and n > 0 and n <= 13, "Bad card n"
  specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
  return specials.get(n, str(n))

#That was given by professor.
#Now we have to interleave the two halves of the deck.

def shuffle(cards):
  assert len(cards) % 2 == 0, 'len(cards) must be even'
  i,lent = 0,len(cards)// 2
  shffled = []
  for i in range(lent):
    shffled.append(cards[i])
    shffled.append(cards[lent + i])
    i += 1
  return shffled

suits = ['♡', '♢', '♤', '♧']
cards = [card(n) + suit for n in range(1,14) for suit in suits]
print(cards[:12])
#['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
print(cards[26:30])
#['7♤', '7♧', '8♡', '8♢']
print(shuffle(cards)[:12])
#['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
print(shuffle(shuffle(cards))[:12])
#['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
print(cards[:12])  # Should not be changed
#['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']

#On to question 3. But later.

def is_circular(G):
  for v in G:
    if reaches_circularity(g, V):
      return True
  return False

def reaches_circularity(G, v0):
  def is_path_to_cycle(v1):
    for w in G[v1]:
      if v0 == w:
        return True
      if is_path_to_cycle(w):
        return True
    return False
  return is_path_to_cycle(v0)

