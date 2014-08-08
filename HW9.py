#Q1
class Link:
  empty = None
  def __init__(self, first, rest=empty):
    self.first = first
    self.rest = rest

  def __repr__(self):
    if self.rest is Link.empty:
      rest = ''
    else:
      rest = ', ' + repr(self.rest)
      return 'Link({}{})'.format(self.first, rest)

  def __str__(self):
    if self.rest is Link.empty:
      rest = ''
    else:
      rest = ' ' + str(self.rest)[2:-2]
    return '< {}{} >'.format(self.first, rest)

  def __iter__(self):
    return LinkedListIterator(self)

class LinkedListIterator:
  def __init__(self, linkl):
    self.linkl = linkl
  
  def __iter__(self):
    return self
  
  def __next__(self):
    try:
      if self.linkl.first == Link.empty:
        raise StopIteration
      else:
        v = self.linkl.first
        self.linkl = self.linkl.rest
        return v
    except StopIteration:
      pass

def list_to_link(lst):
    """
    Given by prof:
    This is a convenience method which 
    converts a Python list into a linked list.
    DO NOT USE THIS IN ANY OF YOUR SOLUTIONS.
    """
    ll = Link.empty
    for elem in lst[::-1]:
        ll = Link(elem, ll)
    return ll

l = list_to_link([1,2,3,4])
i = iter(l)
print(hasattr(i, '__next__'))
l2 = list_to_link([1,3,2,4])
for m in l2:
	print(m)

#Q2
def list_perms(lz):
  if lz == []:
    return []
  prev_perms = list_perms(lz([1:]))
  result = [prev + i for i in range(0, len(lz)) for prev in prev_perms]
  return result
