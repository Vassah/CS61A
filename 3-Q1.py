def has_seven(n):
  if n == '':
    return False
  elif (str(n)[0] == '7'):
    return True
  else:
    return has_seven(str(n)[1:])
    
print(has_seven(3))
#should be False
print(has_seven(7))
#should be True
print(has_seven(376))
#should be True
print(has_seven(4556))
#should be False
print(has_seven(7789))
#should be True
print(has_seven(3775))
#should be True
