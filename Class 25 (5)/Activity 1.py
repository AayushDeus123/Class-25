#Map Function and Lambda keyword (inline function)
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)

print(tup1)
print(tup2)

a = map(lambda x,y : x+y , tup1,tup2)
print('The sum of Tuple 1 and Tuple 2 is :')
print(list(a))

def sqr(x):
    return x*x

b = map(sqr,tup1)
print('\nThe square of Tuple 1 is')
print(list(b))

c = map(sqr,tup2)
print('\nThe square of Tuple 2 is')
print(list(tup2))