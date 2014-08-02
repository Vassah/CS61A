def cons(a, b):
  def cell(message):
    if message == 'car':
      return a
    else:
      return b
  return cell

empty = cons(None, None)

def car(pair):
  return pair('car')

def cdr(pair):
  return pair('cdr')

#I assume the last cell of any linked list is cons(a, empty).
def len(linklist):
  if cdr(linklist) == empty or linklist == empty:
    return 1 #base case is to add 1 since there's still the car of this last cell to be counted.
  else:
    return 1 + len(cdr(linklist))

def print_linked_list(lz):
  print('<')
  def aux(lizt):
    print(car(lizt))
    if lizt == empty or lizt == None:
      print('>')
      return
    else:
      aux(cdr(lizt))
  aux(lz)
#more elegant might to be to accumulate across a string, appending characters and then printing the whole so that it comes out on one line instead of however many.

def starts_with(lz, slz):
  if slz == empty or slz == None:
    return True
  elif len(lz) < len(slz):
    return False
  def g(listic, sublistic):
    if car(listic) != car(sublistic):
      return False
    elif cdr(sublistic) == empty:
      return True
    else:
      return g(cdr(listic), cdr(sublistic))
  return g(lz, slz)

print("\n Starts With and Print Linked List? \n")
empty = cons(None, None)
x = cons(3, cons('foo', cons(6, cons(7, empty))))
print_linked_list(x)
print(starts_with(x, empty))
#should be True
print(starts_with(x, cons(3, empty)))
#should be True
print(starts_with(x, cons(6, empty)))
#should be False
print(starts_with(x, x))
#should be True
print(starts_with(cons(2, empty), cons(2, cons(3, empty))))
#should be False

def has_sublist(lz, slz):
  if lz == slz or slz == empty or slz == None:
    return True
  elif len(lz) < len(slz):
    return False
  def aux(listic, sublistic, posis):
    if car(listic) != car(sublistic):
      return coaux(listic, posis)
    elif cdr(sublistic) == empty:
      return True
    else:
      return aux(cdr(listic), cdr(sublistic), posis)
  def coaux(listic, sublistic):
    if car(listic) == car(sublistic):
      return aux(listic, sublistic, sublistic)
    elif cdr(listic) == empty:
      return False
    else:
      return coaux(cdr(listic), sublistic)
  return coaux(lz, slz)

x = cons('A', cons('G', cons('T', cons('T', cons('G', cons('C', empty))))))
print("\n Has Sublist? \n")
print(has_sublist(empty, empty))
#should be True
print(has_sublist(x, empty))
#should be True
print(has_sublist(x, cons(2, cons(3, empty))))
#should be False
print(has_sublist(x, cons('A', cons('T', empty))))
#should be False
print(has_sublist(x, cons('G', cons('T', cons('T', empty)))))
#should be True
print(has_sublist(cons(1, cons(2, cons(3, empty))), cons(2, empty)))
#should be True
print(has_sublist(x, cons('A', x)))
#should be False

def has_jhh(lz):
  jhh = cons('C', cons('A', cons('T', cons('C', cons('A', cons('T', empty))))))
  return has_sublist(lz, jhh)

print("\n Has JHH? \n")
dna = cons('C', cons('A', cons('T', empty)))
dna = cons('C', cons('A', cons('T', cons('G', empty))))
print(has_jhh(dna))
#should be False
dna = cons('T', cons('C', cons('A', cons('T', cons('G', empty)))))
dna = cons('G', cons('T', cons('A', cons('C', cons('A', dna)))))
print(has_jhh(dna))
#should be True
