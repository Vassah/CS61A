def if_fun(condition, true_res, false_res):
  truf =  condition and true_res
  failse = condition or false_res
  return truf or failse

print(if_fun(5 < 6, 5, 6))
print(if_fun(6 < 5, 5, 6))
#yay

def c():
  return False

def tr():
  return 1/0

def fa():
  return 1

def with_if_fun(condition, true_res, false_res):
  return if_fun(condition(), true_res(), false_res())

with_if_fun(c(), tr(), fa())
