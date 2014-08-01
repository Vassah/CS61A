def two_of_three(a,b,c):
    if a < min(b, c):
        return b*b + c*c
    elif b < min(a, c):
        return a*a + c*c
    elif c < min(a, b):
        return a*a + b*b
    return  a*a + b*b

#all equal should be 25 + 25 = 50
print(two_of_three(5,5,5))
#c<min(a,b) should be 25 + 36 = 61
print(two_of_three(5,6,4))
#a<min(b,c) should be 16 + 36 = 52
print(two_of_three(3,4,6))
#b<min(a,c) should be 25 _ 36 = 61
print(two_of_three(5,4,6))

#course tests
print(two_of_three(1,2,3))
print(two_of_three(5,3,1))
print(two_of_three(10,2,8))
print(two_of_three(5,5,5))
