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
  i,lent = 0,len(cards) + 1 // 2
  shffled = []
  while i <= lent:
    shffled.append(cards[i])
    shffled.append(cards[lent+i])
  return shffled

#On to question 3. But later.
