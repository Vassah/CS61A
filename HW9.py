import random
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
    if self.linkl == Link.empty or self.linkl.first == None or self.linkl == None:
      raise StopIteration
    else:
      v = self.linkl.first
      self.linkl = self.linkl.rest
      return v

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
def list_perms(lst):
  if lst == []:
    return [[]]
  result = []
  for i in range(len(lst)):
    result += [[lst[i]] + perm for perm in list_perms(lst[:i] + lst[i+1:])]
  return result


print(str(list_perms([1,2,3])))
print(list_perms([2,1,3]))

def interleave(seq, other):
    #DO NOT USE IN SOLUTION Given by professor
    result = list(seq)
    for i, el in enumerate(other):
        result.insert(2 * i + 1, el)
    return result

class MathPuzzle:
  #Given by professor
  ops = ['+', '*', '-', '//']

  def __init__(self, rng):
    self.range = rng
    self.puzzle = [random.choice(MathPuzzle.ops) for _ in range(self.range - 1)] # a random list of operators ('+', '-', '*', and '//')
    self.expression = [str(el) for el in interleave(random_permutation(range(1, rng + 1)), self.puzzle)] # operators interwoven with numbers
    self.value = eval(''.join(self.expression)) # the result of evaluating self.expression in Python

  def __str__(self):
    return ' '.join([el if el in MathPuzzle.ops else "___" for el in self.expression]) + " = " + str(self.value)

  def check_solution(self, inputs):
    guessed_exp = [str(el) for el in interleave(inputs, self.puzzle)]
    return eval(''.join(guessed_exp)) == self.value


def solve_list_perms(puzzle):
  #Q3 Main Function
  possibilus = list_perms(puzzle.range) #Not actually the right entity to loop over
  for poss in possibilus:
    if puzzle.check_solution(poss):
      return poss
  return None


#Q3
def generate_perms(lst):
  if lst == []:
  	yield []
  else:
    for i in range(len(lst)):
      for perm in generate_perms(lst[:i]+lst[i+1:]):
      	yield [lst[i]] + perm

perms = generate_perms([1,2,3])
print(hasattr(perms, '__next__'))
p = list(perms)
p.sort()
print(p)

def solve_gen_perms(puzzle):
  for possible in generate_perms(puzzle.range): #Not actually right entity to loop over
    if puzzle.check_solution(poss):
    	return poss
  return None

class TestPuzzle(MathPuzzle):
    """
    Creates a MathPuzzle out of the given expression.
    >>> test = TestPuzzle([1, '+', 2, '*', 3])
    >>> print(test)
    ___ + ___ * ___ = 7
    >>> test.check_solution([1, 2, 3])
    True
    >>> test.check_solution([1, 3, 2])
    True
    >>> test.check_solution([2, 3, 1])
    False
    """
    def __init__(self, expression):
        self.expression = [str(el) for el in expression]
        self.puzzle = [el for el in expression if el in MathPuzzle.ops]
        self.value = eval(''.join(self.expression))
        self.range = len(self.puzzle) + 1



##############
# Remainders #
##############

def remainders_generator(m):
  def multiples(n):
    prev = n
    while True:
    	yield	prev
    	prev = prev + m
  for i in range(m):
    yield multiples(i)

rem_group = remainders_generator(4)
for rem in rem_group:
  for i in range(3):
    print(next(rem))
