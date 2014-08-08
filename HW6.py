import sys
sys.path.append("/Users/s42/Documents/CS61A/")
import ucb

def cons(a, b):
  def cell(message):
    if message == 'car':
      return a
    else:
      return b
  return cell

def is_linked_list(lst):
    """
    >>> is_linked_list(empty)
    True
    >>> is_linked_list(link(1, link(4, link(7, empty))))
    True
    >>> is_linked_list(link(1, link(4, 7)))
    False
    >>> is_linked_list(link(link(2, empty), empty))
    True
    """
    return lst == empty or (is_pair(lst) and is_linked_list(rest(lst)))

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_linked_list(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))
def tokenize(s):
    """Splits the provided string into a list of tokens.

    >>> tokenize('(* (+ 12 3) 5)')
    ['(', '*', '(', '+', '12', '3', ')', '5', ')']
    """
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    return s.split()

#Tokenize is given in assignment, as are the linked list functions.
#These however are mine:
def car(cell):
  return cell('car')

def cdr(cell):
  return cell('cdr')

empty = cons(None, None)

def make_link_list(lz):
  if lz == []:
      return empty
  return cons(lz[0], make_link_list(lz[1:]))

#I assume the last cell of any linked list is cons(a, empty).                               
def len(linklist):
  if cdr(linklist) == empty or linklist == empty:
    return 1 #base case is to add 1 since there's still the car of this last cell to be counted.                                                                                       
  else:
    return 1 + len(cdr(linklist))

#Onward.
#This is to return a scheme expression for:
# if n == 1 48/(2*(9+3))
# else 48/2)*(9+3)

def scheme_exp(n):
   if n == 1:
       return "(/ 48 (* 2 (+ 9 3)))"
   else:
       return "(* (/48 2) (+ 9 3))"
first = scheme_exp(1)
assert '/' in first and '(' in first and '+' in first
assert '48' in first and '2' in first
assert '9' in first and '3' in first
#eval_sring(first)
second = scheme_exp(2)
assert '/' in second and '*' in second and '+' in second
assert '48' in second and '2' in second
assert '9' in second and '3' in second
#eval_string(second)

#Converts to number if possible, else does nothing
def numberize(atomic_exp):
  try:
    try:
      return int(atomic_exp)
    except ValueError:
      return float(atomic_exp)
  except ValueError:
    return atomic_exp

print(numberize('123'))
#Should be 123
print(numberize('3.14159'))
#Should be 3.14159
print(numberize('+'))
#Should be '+'

def read_exp(token_lz):
  if token_lz == []:
    raise SyntaxError('unexpected end of input')
  token, rest = token_lz[0], token_lz[1:]
  if token == ')':
    raise SyntaxError('unexpected )')
  elif token == '(':
    if rest == []:
      raise SyntaxError('mismatched parentheses')
    elif rest[0] == ')':
      raise SyntaxError('empty combination')
    else:
      return read_until_close(rest)
  else:
    return read_exp(rest)

def reverse_linked_list(lz):
  acc = empty
  while cdr(lz) != empty:
    acc = cons(car(lz), acc)
    lz = cdr(lz)
  acc = cons(car(lz), acc)
  return acc

def read_until_close(open_expr):
  def aux(oped,acc):
    if oped == None or oped == []:
      raise SyntaxError('No Closure')
    token,rest = oped[0], oped[1:]
    if token == '(':
      acc = cons(read_exp(oped), acc)
      return aux(rest, acc)
    elif token == ')':
      return reverse_linked_list(acc), rest
    else:
      acc = cons(numberize(token), acc)
      return aux(rest, acc)
  return aux(open_expr, empty)

exp, unevaled = read_exp(['(', '+', '1', '3', '6', ')'])
print_linked_list(exp)
#Should be < '+' 2 3 6 >
print(unevaled)
#Should be []
exp, unevaled = read_exp(['2', '3'])
print(exp)
#Should be 2
print(unevaled)
#Should be ['3']
exp, unevaled = read_exp(['(', '/', '6', '2', ')', '(', '-', '2', ')'])
print_linked_list(exp)
#Should be < '/' 6 2>
print(unevaled)
#Should be ['(', '-', '2', ')']
exp, unevaled = read_exp(['(', '*', '4', '(', '-', '12', '8', ')', ')', '3','2'])
print_linked_list(exp)
#Should be < '*' 4 <'-' 12 8 > >
print(unevaled)
#['3', '2']
exp, unevaled = read_until_close(['+', '2', '3', ')', '4', ')'])
print_linked_list(exp)
#Should be < '+' 2 3 >
print(unevaled)
#Should be ['4', ')']
exp, unevaled = read_until_close(['+', '(', '-', '2', ')', '3', ')', ')'])
print_linked_list(exp)
#Should be < '+' < '-' 2 > 3 > NOPE DOESN'T WORK
print(unevaled)
#Should be [')'] NOPE DOESN'T WORK
