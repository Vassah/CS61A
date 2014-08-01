def accumulate(combiner, start, n, term):
    while start == n:
        return ?
    return combiner(term(n), accumulate(combiner, (start + 1), n, term))

print(accumulate(lambda a, b: a + b, 0, 5, lambda x: x))
#should be 15
print(accumulate(pow, 2, 3, lambda x: 2))
#should be 65536
print(accumulate(lambda x, y: x * y, 1, 4, lambda k: 3))
#should be 81
'''                                                                  
def summation_using_accumulate(n, term):
    return None
print(summation_using_accumulate(4, square))                                   #should be 30                                                                  print(summation_using_accumulate(4, lambda x: 2**x))
#should be 30
print(summation_using_accumulate(4, square))
#should be 576
print(summation_using_accumulate(6, lambda x: 3))
#should be 729
'''
