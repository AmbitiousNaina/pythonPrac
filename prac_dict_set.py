# Write a program to create a dictionary of hindi words, provide values as its english translation.

# words = {
#     "Tufan" : "Storm",
#     "Billi" : "Cat",
#     "Darwaza": "Door"
# }
#
# word = input("Enter the word :")
#
# print(words[word])

# ====================
# Enter 5 nos from the user, display all the unique values
# nos = set()
# n = int(input("Enter the number :"))
# nos.add(n)
#
# n = int(input("Enter the num :"))
# nos.add(n)
#
# n = int(input("Enter the num :"))
# nos.add(n)
#
# n = int(input("Enter the num :"))
# nos.add(n)
# n = int(input("Enter the num :"))
# nos.add(n)
# print(nos)

#Enter & display: int,float & string value .. what will be the len of this?

# s = set()
# s.add(20)
# s.add(20.0) #pythons compares & considers 20 == 20.0 as same values & returns true
# s.add("20")
# print(s)
# print(len(s))

# Write a prog wherein u create an empty dict, adding 4 friends as keys, their fav lang as values

# friends = {
#     "Rohan" : "C++",
#     "Gaurav" : "Python",
#     "Sunay"  : "C",
#     "Vinay"  : "Java"
# }
# print(friends)

# friends = {}
#
# names = input("Enter the name :")
# lang = input("Enter their fav prog lang :")
# friends.update({names:lang})
#
# names = input("Enter the name :")
# lang = input("Enter their fav prog lang :")
# friends.update({names:lang})
#
# names = input("Enter the name :")
# lang = input("Enter their fav prog lang :")
# friends.update({names:lang})
#
# names = input("Enter the name :")
# lang = input("Enter their fav prog lang :")
# friends.update({names:lang})  #Values can be same, but keys cant, only unique keys will be considered
#
# print(friends)

# Can you change values inside a list contained in a set? No u cant

 s = {1,2,3, [1,2]} #You cant have a list inside a set, you cant index a set, (sets- immutable,hashable)
 print(s)