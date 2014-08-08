import random as rando

def build_successors_table(tokens):
  table = {}
  prev = '.'
  for word in tokens:
    if prev in table:
      table[prev].append(word)
    else:
      table[prev] = [word]
    prev = word
  return table

text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
table = build_successors_table(text)
print(table)
expected = {'and': ['to'], 'We': ['came'], 'bad': ['guys'], 'pie': ['.'], ',': ['catch'], '.': ['We'], 'to': ['investigate', 'eat'], 'investigate': [','], 'catch': ['bad'], 'guys': ['and'], 'eat': ['pie'], 'came': ['to']}
print(table == expected)


def construct_sent(word, tablus):
  result = ' '
  while word not in ['.', '!', '?']:
    result += word + ' '
    word = rando.choice(table[word])
  return result + word

print(construct_sent('and', table))
print(construct_sent('and', table))

#Until I read this function it actually didn't occur to me you could import modules in a scope!
def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://goo.gl/SztLfX'):
  import os
  from urllib.request import urlopen
  if os.path.exists(path):
    return open('shakespeare.text', encoding = 'ascii').read().split()
  else:
    shakespeare = urlopen(url)
    return shakespeare.read().decode(encoding='ascii').split()

tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def sent():
  return construct_sent('The', table)

print(sent())
print(sent())
print(sent())

def random_sent():
  return construct_sent(rando.choice(table['.'], table))

print(random_sent())
print(random_sent())
print(random_sent())

