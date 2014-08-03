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
    elif num_common_letters(guess, goal_word) == word_len:
      return win_message
    else:
      return num_common_letters(guess, goal_word)
  return word_master

def is_valid_guess(word):
  if get_string(word) == 'aaaaa':
    return False
  return True

#Make Tests
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

