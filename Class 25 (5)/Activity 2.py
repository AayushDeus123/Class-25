#Zip function using loop, reverse and dictionary
list1 = ['Aayush','John','Peter','Harry']
list2 = [14,15,18,13]

print(list1)
print(list2)

a = list(zip(list1,list2))
print('\nThe ages of the people are')
print(a)


small = [10,20,30,40]
big = [100,200,300,400]

print(small)
print(big)

print('The reverse of Big is printed according to Small')
for i,j in zip(small,big[::-1]):
    print(i,j)
    
    
name = ['Infosys','Tcs','Reliance']
stock = [2794, 1594, 2345]

print(name)
print(stock)

dict = {name:stock for name,stock in zip(name,stock)}
print('The stock according to the name is')
print(dict)