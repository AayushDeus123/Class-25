num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

odd1 = list(range(1, num, 2))  
odd2 = list(range(1, num2, 2)) 

print("\nOdd numbers from 1st Input:", odd1)
print("\nOdd numbers from 2nd Input:", odd2)


fruits = ["apple", "banana", "cherry", "date"]
capfruits = list(map(str.capitalize, fruits))

print("\nCapitalized fruits:", capfruits)