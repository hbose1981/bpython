a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))

print("Value of a and b before swap = ",a,b)

a = a + b
b = a - b
a = a - b

print("Value of a and b after swap = ",a,b)