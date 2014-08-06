#We are asked to reverse a list in place and return None
#We are not to use list methods or slicing, only index assignment
#So as to not use the __len__ list method...
def lengther(lz):
  vz = 0
  for i in lz:
    vz += 1
  return vz
#and the meat

def reverse_list(lz):
  n = lengther(lz) - 1
  i = 0
  while i<n:
  	lz[i], lz[n] = lz[n], lz[i]
  	i,n = i+1, n-1
  return None

listic = [5,4,3,2,1]
lzz = [4,3,2,1]
reverse_list(listic)
print(listic)
reverse_list(listic)
print(listic)
reverse_list(lzz)
print(lzz)
reverse_list(lzz)
print(lzz)
