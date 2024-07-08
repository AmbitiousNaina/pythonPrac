friends = ['Grapes','Sunayana', 'Apple', 5, 35.3]
print(friends)
friends[0] = "Gauri" #unlike strings ,lists are mutable, they can be changed after creation
print(friends)

friends.append("Heena")
print(friends)

print(friends[1:3])

l1= [1,5,8,3,23,11,78,14]
# l1.sort()
# l1.reverse()
l1.insert(3,3333)
print(l1)
l1.pop()
print(l1)
l1.pop(3) #delete the value from the list based on index
print(l1)
l1.remove(1) #remove removes the value from the list
print(l1)

friends = []
print(type(friends))