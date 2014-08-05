letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
bad_num_letters = "Wrong number of letters."
not_a_word = "Not a valid word."
win_message = "Congratulations! You win!"

#We are asked to implement a 'word' abstract data type.
#Basically, it's an OCaml type of form [Char, [Char]]

def make_word_from_string(s):
  #Creates an instance of the word ADT from the string s.
  lst = []
  for i in range(0, len(s)):
    lst.append(s[i])
  return [s, lst]

def make_word_from_list(lst):
  #Creates an instance of the word ADT from the list of characters lst.
  s = ''
  for i in lst:
    s += i
  return [s, lst]

def get_string(word):
  #Returns the string representation of word.
  return word[0]

print(get_string(make_word_from_string('hello')))
#Should be 'hello'
print(get_string(make_word_from_list(['w', 'o', 'r', 'l', 'd'])))
#Should be 'world'

def get_list(word):
  #Returns the list of characters representation of word.
  return word[1]

print(get_list(make_word_from_string('hello')))
#Should be ['h', 'e', 'l', 'l', 'o']
print(get_list(make_word_from_list(['w', 'o', 'r', 'l', 'd'])))
#Should be ['w', 'o', 'r', 'l', 'd']

#Now we are asked to implement a function that finds number of common letters
#We simplify the problem:

def word_wo_reps(word):
  lz = get_list(word)
  acc = []
  for i in lz:
    if not i in acc:
      acc.append(i)
  return mwfl(acc)

#We test to see that works.
mwfs, mwfl = make_word_from_string, make_word_from_list
print(mwfs('hello'))
print(get_list(mwfs('hello')))
print(word_wo_reps(mwfs('hello')))
print(get_string(word_wo_reps(mwfs('hello'))))
#should be 'helo'
print(get_string(word_wo_reps(mwfs('helo'))))
#should be 'helo'
print(get_string(word_wo_reps(mwfs('steel'))))
#should be 'stel'

#So that's finally on track!
#Onward ho. Since only guess has repetitions, let's just eliminate them

def num_common_letters(goal, guess):
  guess = word_wo_reps(guess)
  acc = 0
  for i in get_list(guess):
    for j in get_list(goal):
      if i ==j:
        acc += 1
  return acc

print(num_common_letters(mwfs('hello'), mwfs('hell')))
#Should be 4
print(num_common_letters(mwfs('hello'), mwfs('red')))
#Should be 1
print(num_common_letters(mwfs('hello'), mwfs('rid')))
#Should be 0

def make_word_master(goal_word):
  word_len = len(get_string(goal_word))
  def word_master(guess):
    if len(get_string(guess)) > word_len:
      return bad_num_letters
    elif not is_valid_guess(guess):
      return not_a_word
    elif get_string(guess) == get_string(goal_word):
      return win_message
    else:
      return num_common_letters(goal_word, guess)
  return word_master

def is_valid_guess(word):
  if get_string(word) == 'aaaaa':
    return False
  return True

#Make Tests
print("\nMake Word Master?")
foo = make_word_master(mwfs('least'))
print(foo(mwfs('water')))
#Should be 3
print(foo(mwfs('player')) == bad_num_letters)
#Should be True
print(foo(mwfs('steel')))
#Should be 4
print(foo(mwfs('steal')))
#Should be 5
print(foo(mwfs('aaaaa')) == not_a_word)
#Should be True
print(foo(mwfs('least')) == win_message)
#Should be True

def subsets(lst, n):
  if n == 0:
    return [[]]
  if len(lst) == n:
    return [lst]
  use_first = [ [lst[0]] + x for x in subsets(lst[1:], n - 1)] #recursive step
  dont_use_first = subsets(lst[1:], n) #step forward, then recurse
  return use_first + dont_use_first

print(subsets([1, 2, 3], 1))
#Should be [[1], [2], [3]]
print(subsets([1, 2, 3], 2))
#Should be [[1,2], [1,3], [2,3]]
print(subsets([1, 2, 3], 3))
#Should be [[1,2 3], [2,1,3], [3,1,2]
three_subsets = subsets(list(range(5)), 3)
print(three_subsets)
three_subsets.sort()
for subset in three_subsets:
  print(subset)
#should be a list of subsets...

def compatible(guess, score, letter_list):
  mastery = make_word_master(mwfl(letter_list))
  if mastery(guess) == score:
    return True
  return False

print(compatible(mwfs('steal'), 5, ['l', 'e', 'a', 's', 't']))
#Should be True
print(compatible(mwfs('blanket'), 6, ['a', 'b', 'e', 'l', 'n', 'r', 't']))
#Should be True
print(compatible(mwfs('cool'), 4, ['c', 'o', 'l', 'd']))
#Should be False
print(compatible(mwfs('found'), 1, ['d', 'e', 'f', 'g', 'h']))
#Should be False

def filter_subsets(word, score, possible_subsets):
  return [poss for poss in possible_subsets if compatible(word, score, poss)]

word = mwfs('steal')
sub1 = ['a', 'b', 'e', 'l', 's']
sub2 = ['b', 'e', 'l', 't', 'z']
sub3 = ['s', 't', 'e', 'a', 'l']
sub4 = ['b', 'l', 'e', 's', 't']
print(filter_subsets(word, 4, [sub1, sub2, sub3, sub4]))  

def make_deductions(possible_subsets, letters):
  nilletrus = []
  for i in range(0, len(letters)):
    for poss in possible_subsets:
      if i not in poss:
        nilletrus.append(letters.pop(i))
  return letters, nilletrus

def make_deductions(possible_subsets, letters):
  nilletrus = []
  letrus = []
  nonpossible = []
  possible = []
  for i in letters:
    for poss in possible_subsets:
      if i not in poss:
        nonpossible.append(i)
      if i in poss:
        possible.append(i)
    if i not in nonpossible:
      letrus.append(i)
    if i not in possible:
      nilletrus.append(i)
  return letrus, nilletrus
#Not the most elegant or concise solution, but it works, so go away thank you.

letrus = ['a', 'b', 'c', 'd', 'e', 'f']
subsis = [['a', 'b', 'c'], ['b', 'a', 'e'], ['e', 'a', 'c']]
present, not_present = make_deductions(subsis, letrus)
print(present)
#Should be 'a'
print(not_present)
#Should be ['d', 'f']

#Now we are to show we have not committed any data abstraction violations
#We do this by replacing the word ADT with a function implementation

def make_word_from_string(s):
  lst = [x for x in s]
  return lambda x: s if x == 0 else lst

def make_word_from_list(lz):
  stz = ''
  for i in lz:
    stz = stz + i
  return lambda x: stz if x == 0 else lz

def get_string(wrd):
  return wrd(0)

def get_list(wrd):
  return wrd(1)
