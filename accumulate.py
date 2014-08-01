def accumulate(combiner, start, n, term):
  acc, i = start, 1
  while i<= n:
    acc = combiner(term(i), acc)
    i += 1
  return acc

print(accumulate(lambda a, b: a + b, 0, 5, lambda x: x))
#should be 15
print(accumulate(pow, 2, 3, lambda x: 2))
#should be 65536
print(accumulate(lambda x, y: x * y, 1, 4, lambda k: 3))
#should be 81
                                                                 
def summation_using_accumulate(n, term):
    return accumulate(lambda a, b: a + b, 0, n, term)
print(summation_using_accumulate(4, lambda x: x*x))                                   #should be 30 
print(summation_using_accumulate(4, lambda x: 2**x))
#should be 30

def product_using_accumulate(n, term):
  return accumulate(lambda a, b: a*b, 1, n, term)
print(product_using_accumulate(4, lambda x: x*x))
#should be 576
print(product_using_accumulate(6, lambda x: 3))
#should be 729
