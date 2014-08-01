def accumulate(combiner, start, n, term):
  acc, i = start, 1
  while i<= n:
    acc = combiner(term(i), acc)
    i += 1
  return acc

square = lambda x: x*x

def composer(f, g):
  def h(x):
    return f(g(x))
  return h

def f_to_n(f, n):
  funcy = f
  while n > 1:
    funcy, n = composer(f, funcy), n - 1
  return funcy


def f_to_n_(f, n):
  def composite(x):
    acc = x
    i = 0
    while i < n:
      acc = f(acc)
      i += 1
    return acc
  return composite

def f_to_n__(f, n):
  return accumulate(composer, f, n-1, (lambda k: f))

print(f_to_n(square, 2)(5))
#should be 625
print(f_to_n(square, 4)(5))
#should be 152587890625
print(f_to_n(lambda x: x + 1, 5)(309))
#should be 314
print(f_to_n(lambda x: 2**x, 3)(2))
#should be 65536

print(f_to_n_(square, 2)(5))
#should be 625                                                                
print(f_to_n_(square, 4)(5))
#should be 152587890625                                                       
print(f_to_n_(lambda x: x + 1, 5)(309))
#should be 314                                                                
print(f_to_n_(lambda x: 2**x, 3)(2))
#should be 65536

print(f_to_n__(square, 2)(5))
#should be 625                                                                
print(f_to_n__(square, 4)(5))
#should be 152587890625                                                       
print(f_to_n__(lambda x: x + 1, 5)(309))
#should be 314                                                                
print(f_to_n__(lambda x: 2**x, 3)(2))
#should be 65536

def double(f):
  return f_to_n(f, 2)
