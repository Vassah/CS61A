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
      if self.rest.first == empty:
        raise StopIteration
      else:
        
      
