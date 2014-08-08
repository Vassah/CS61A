def make_accumulator():
  lz = []
  def accumulus(n=0):
    lz.append(n)
    return sum(lz)
  return accumulus

acc = make_accumulator()
print(acc(15))
print(acc(10))
acc2 = make_accumulator()
print(acc2(7))
acc3 = acc2
print(acc3(6))
print(acc2(5))
print(acc(4))


def make_accumulator_nonlocal():
  v = 0
  def accumulator(n):
    nonlocal v
    v = v + n
    return v
  return accumulator

print("\nNow Nonlocal?")
acc = make_accumulator_nonlocal()
print(acc(15))
print(acc(10))
acc2 = make_accumulator_nonlocal()
print(acc2(7))
acc3 = acc2
print(acc3(6))
print(acc2(5))
print(acc(4))

print("\nNickels and Pennies OOP?")

class Amount(object):
  def __init__(self, nickels, pennies):
    self.nickels = nickels
    self.pennies = pennies
    
    @property
    def value(self):
       return 5*self.nickels + self.pennies

    @value.setter
    def value(self, value):
       self.nickels = value // 5
       self.pennies = value % 5

a = Amount(3, 7)
print(a.nickels)
print(a.pennies)
print(a.value)
a.nickels = 5
print(a.value)

class MinimalAmount(Amount):
  def __init__(self, nickels, pennies):
    self.nickels = nickels + pennies // 5
    self.pennies = pennies % 5
