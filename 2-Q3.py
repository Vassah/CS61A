square = lambda x: x*x
'''
def f_to_n(f, n):
  funcy, i = f, 0
  while i <= n:
    funcy = lambda x: f(funcy(x))
    i += 1
  return funcy

def f_to_n(f, n):
  def composite(x):
    acc, i = x,1
    while i<n:
      acc = f(acc)
      i += 1
    return acc
  return composite
'''
composes(f, g) = lambda x: f(g(x))
def f_to_n(f, n):
  return accumulate(compose(f, f), 0, n, lambda k: f)

f_to_n(square, 2)(5)
#should be 625
f_to_n(square, 4)(5)
#should be 152587890625
f_to_n(lambda x: x + 1, 5)(309)
#should be 314
f_to_n(lambda x: 2**x, 3)(2)
#should be 65536

def double(f):
  return f_to_n(f, 2)
