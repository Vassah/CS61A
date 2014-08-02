def composer(f, g):
  def h(x):
    return f(g(x))
  return h

def accumulate(combiner, start, n, term):
  acc, i = start, 0
  while i <= n:
    acc = combiner(term(i), acc)
    i += 1
  return acc

def f_to_n(f, n):
  return accumulate(composer, f, n-1, lambda x: f)

def zero(f):
  return lambda x: x
  
def successor(n):
  def h(f):
    return lambda x: f_to_n(f, n(lambda x: x + 1)(0) + 1)
  return h

def one(f):
  return lambda x: f(x)

def two(f):
  return lambda x: f(f(x))

def two_prime(f):
  return lambda x: f(one(f)) (x)

def church_to_int(f):
  successor = lambda x: x + 1
  return f(successor)(0)

def church_add(f, g):
  def adeed(x):
    return f(g(x))
  return adeed

def church_mul(f, g):
  return

print(church_to_int(successor(zero)))
#should be 1
print(church_to_int(successor(successor(zero))))
# should be 2
print(church_to_int(successor(one)))
#should be 2
print(church_to_int(successor(two)))
#should be 3
print(church_to_int(two))
#should be 2
print(church_to_int(two))
#should be 2
print(church_to_int(zero))
#should be 0
print(church_to_int(one))
#should be 1
print(church_to_int(church_add(two, two)))
#should be 4
print(church_to_int(church_add(one, one)))
#should be 2 but I keep getting 1 
print(church_to_int(church_add(one, two)))
#should be 3 but I keep getting 2
