#clearly we want a recursive solution...
#I assume denoms is given as a linked list of values of denominations
def cons(a, b):
  def cell(message):
    if message == 'car':
      return a
    else:
      return b
  return cell

empty = cons(None, None)

def car(pair):
  return pair('car')

def cdr(pair):
  return pair('cdr')

def sum_of_list(link_list):
  if cdr(link_list) == empty:
    return 1
  else return 1 + sum_of_list(cdr(link_list))

def count_change(amount, denoms):
  if car(denoms) > amount:
    count_change(cdr(denoms) #if the value of a denomination is greater than the amount, it contributes no counts
  elif car(denoms) == 1:
    return 1 #There is only one way to count using pennies
  elif: sum_of_list(denoms) > amount:
   
    
