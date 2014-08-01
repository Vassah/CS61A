empty = cons(None, None)

def cons(a, b):
  def list(message):
    if message =='car':
      return a
    else:
      return b

def car(pair):
  return pair('car')

def cdr(pair):
  return pair('cdr')

#I assume the last cell of any linked list is cons(a, empty).
def len(linklist):
  if cdr(linklist) == empty:
    return 1 #base case is to add 1 since there's still the car of this last cell to be counted.
  else:
    return 1 + len(cdr(linklist))

def print_linked_list(lz):
  print('<')
  def aux(lizt):
    print(car(lz))
    if cdr(lizt) == None:
      print('>')
      return
    else:
      aux(cdr(lizt))
  aux(lz)

def starts_with(L, sL):
  if len(L) < len(sL):
    return False
  def g(listic, sublistic):
    if car(listic) != car(sublistic):
      return False
    elif cdr(sublistic) == empty:
      return True
    else:
      return g(cdr(listic), cdr(sublistic))
  return g(L, sL)

empty = cons(None, None)
x = cons(3, cons('foo', cons(6, cons(7, empty))))
print_linked_list(x)
starts_with(x, empty)
#should be True
starts_with(x, cons(3, empty))
#should be True
starts_with(x, cons(6, empty))
#should be False
starts_with(x, x)
#should be True
starts_with(cons(2, empty), cons(2, cons(3, empty)))
#should be False

def has_sublist(lz, slz):
  if len(L) < len(sL):
    return False
  def aux(listic, sublistic, posis):
    if car(listic) != car(sublistic):
      return coaux(listic, posis)
    elif cdr(sublistic) == empty
      return True
    else:
      return aux(cdr(listic), cdr(sublistic), posis)
  def coaux(listic, sublistic):
    if car(listic) == car(sublistic):
      return aux(listic, sublistic)
    elif cdr(listic) == empty
      return False
    else:
      return coaux(cdr(listic), sublistic)
  return coaux(lz, slz)

has_sublist(empty, empty)
#should be True
has_sublist(x, empty)
#should be True
has_sublist(x, cons(2, cons(3, empty)))
#should be False
has_sublist(x, cons('A', cons('T', empty)))
#should be False
has_sublist(x, cons('G', cons('T', cons('T', empty))))
#should be True
has_sublist(cons(1, cons(2, cons(3, empty))), cons(2, empty))
#should be True
has_sublist(x, cons('A', x))
#should be False

def has_jhh(lz):
  jhh = cons('C', cons('A', cons('T', cons('C', cons('A', cons('T', None))))))
  return has_sublist(lz, jhh)

dna = cons('C', cons('A', cons('T', empty)))
dna = cons('C', cons('A', cons('T', cons('G', empty))))
has_jhh(dna)
#should be False
dna = cons('T', cons('C', cons('A', cons('T', cons('G', empty)))))
dna = cons('G', cons('T', cons('A', cons('C', cons('A', dna)))))
has_jhh(dna)
#should be True
