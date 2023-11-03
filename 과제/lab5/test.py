lst0 = ['a', 'b']
lst1 = [lst0, 1,2]
lst2 = lst1.copy()

lst2[0][1] = 'c'
print(lst0)
print(lst1)
print(lst2)

print(id(lst0))
print(id(lst1[0]))
print(id(lst2[0]))

a = 1
b = a

print(id(a))
print(id(b))

a = 3

print(a,b)
print(id(a))
print(id(b))
