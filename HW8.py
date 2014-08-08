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
q = a.value
print(q)
a.nickels = 5
q = a.value
print(q)

class MinimalAmount(Amount):
  def __init__(self, nickels, pennies):
    self.nickels = nickels + pennies // 5
    self.pennies = pennies % 5

print("\nMinimalAmount?")
a = MinimalAmount(3, 7)
m = a.nickels, a.pennies, a.value
print(m)
a = MinimalAmount(7, 3)
m = a.nickels, a.pennies, a.value
print(m)
a = MinimalAmount(0,50)
m = a.nickels, a.pennies, a.value
print(m)

#Q4
class VendingMachine(object):
  def __init__(self, thing, cost):
     self.cost = cost
     self.thing = thing
     self.balance = 0
     self.stock = 0

  def restock(self, amount):
     self.stock = self.stock + amount
     print('Current {0} stock: {1}'.format(self.thing, self.stock))

  def deposit(self, payment):
     self.balance = self.balance + payment
     print('Current Balance: ${0}'.format(self.balance))

  def vend(self):
    if self.balance == self.cost:
        print('Here is your {0}.'.format(self.thing))
        self.balance = 0
    elif self.balance > self.cost:
        print('Here is your {0} and ${1} change.'.format(self.thing, self.balance - self.cost))
        self.balance = 0
    else:
        print('You must deposit ${0} more.'.format(self.cost - self.balance))

print("\nVendingMachine?")
v = VendingMachine('candy', 10)
v.vend()
v.restock(1)
v.vend()
v.deposit(7)
v.vend()
v.restock(1)
v.deposit(5)
v.vend()
v.deposit(10)
v.vend()
v.deposit(15)
v.vend()
p = VendingMachine('pepsi', 21)
p.restock(100)
p.deposit(100)
p.vend()
p.deposit(21)
p.vend()

#Q5
