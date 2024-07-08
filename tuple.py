# l1 = () ##empty tuple..
# print(type(l1))
#
# l1 = (1) #wont consider this as a tuple for single element, you need to add a comma
# print(type(l1))
#
# l1=(1,) #now its a tuple
# print(type(l1))
#
# l1 =(1,33, "Sunayana", "anita",33)  #tuple - collection of elements of different data type, bt its immutable just like strings, it cant be changed after creation.
# print(type(l1))
#
# # l1[2] = "Grapes" #cant change in tuple.
# # print(l1)
#
# print(l1.count(33))
# print(l1.index(33))
#
# print(len(l1))
#
# l2= l1*3 #it will print the tuple 3 times
# print(l2)
#
# l2= l1+l1
# print(l2)


# #write a program to display 3 fruits
# fruits = []
# f1 = input("Enter the name of the fruit :")
# fruits.append(f1)
#
# f2 = input("Enter the name of the fruit :")
# fruits.append(f2)
#
# f3 = input("Enter the name of the fruit :")
# fruits.append(f3)
#
# print(fruits)


#Write a prog to accept marks of 3 students an sort them
#
# marks = []
#
# m1 = int(input("Enter marks of student 1 :"))
# marks.append(m1)
#
# m2 = int(input("Enter the marks of student 2 :"))
# marks.append(m2)
#
# m3 = int(input("Enter the marks of student 3 :"))
# marks.append(m3)
#
# print(marks)
# marks.sort()
# print(marks)

#Write a program to show the sum of 3 nos

# l = [1,2,3,4]
# print(sum(l))

#count the number of zero's

l = (2,0,5,6,0,0,4)
l2= l.count(0)
print(l2)