#Q1
def scan(f, lst, start):
  def scaux(f, lz, start, acc):
    if lz == []:
      return acc
    else:
      return scaux(f, lz[1:], start, acc + [f(acc[-1], lz[0])])
  return scaux(f, lst[1:], start, [f(start, lst[0])])

from operator import add, mul
print(scan(add, [1,2,3,4], 0))
#Should be [1,3,6,10]
print(scan(mul, [3,2,1,0], 10))
#Should be [30, 60, 60, 0])

#Q3
class BST:
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right
#MY CODE
    def paths(self):
        if not self.right and not self.left:
            'RESULT'
        if 'CONDITION':
            for VARIABLE in 'ITERABLE':
                'RESULT'
        if 'CONDITION':
            for VARIABLE in 'ITERABLE':
                'RESULT'
#END MY CODE

#Q4
#WE ARE NOT TO CALL THE LINK CONSTRUCTOR
def deal_deck(linked_list, num_of_players):
  for i in range(len(linked_list)//num_of_players):
    for thing in 'ITERABLE':
      linked_list, card = linked_list.rest, linked_list
      'RESULT'
   return 'RESULT
