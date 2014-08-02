#We are asked to implement a 'word' abstract data type.
#Basically, it's an OCaml type of form [Char, [Char]]

def make_word_from_string(s):
  #Creates an instance of the word ADT from the string s.
  return [s, s.split()]

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
print(get_string(make_word_from_list(['w', 'o', 'r', 'l', 'd']))))
#Should be 'world'

def get_list(word):
  #Returns the list of characters representation of word.
  return word[1]

print(get_list(make_word_from_string('hello')))
#Should be ['h', 'e', 'l', 'l', 'o']
print(get_list(make_word_from_list(['w', 'o', 'r', 'l', 'd'])))
#Should be ['w', 'o', 'r', 'l', 'd']
