import sys
sys.path.append("/Users/s42/Documents/CS61A/")
import ucb

def tokenize(s):
    """Splits the provided string into a list of tokens.

    >>> tokenize('(* (+ 12 3) 5)')
    ['(', '*', '(', '+', '12', '3', ')', '5', ')']
    """
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    return s.split()

#Tokenize is given in assignment.
#Onward.
#This is to return a scheme expression for:
# if n == 1 48/(2*(9+3))
# else 48/2)*(9+3)

def scheme_exp(n):
   if n == 1:
       return "(/ 48 (* 2 (+ 9 3)))"
   else:
       return "(* (/48 2) (+ 9 3))"
first = scheme_exp(1)
assert '/' in first and '(' in first and '+' in first
assert '48' in first and '2' in first
assert '9' in first and '3' in first
#eval_sring(first)
second = scheme_exp(2)
assert '/' in second and '*' in second and '+' in second
assert '48' in second and '2' in second
assert '9' in second and '3' in second
#eval_string(second)

