
# a = int(input("Enter your age :"))
#
# if(a >= 18):
#     print("Yes")
# elif(a<0):
#     print("invalid age")
# elif(a==0):
#     print("age is zero")
# else:
#     print("No")
#
# print("end of prog")

#Print greatest of all 4 nos

# a1 = int(input("Enter a no:"))
# a2 = int(input("Enter a no:"))
# a3 = int(input("Enter a no:"))
# a4 = int(input("Enter a no:"))
#
# if(a1>a2 and a1>a3 and a1>a4):
#     print("A1 is greatest!",a1)
#
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("A2 is greatest!",a2)
#
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("A3 is greatest!",a3)
#
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("A4 is greatest!",a4)

#marks shud be greater than 33 and total % must be greater than 40..

# marks1 = int(input("Enter marks 1 :"))
# marks2 = int(input("Enter marks 2 :"))
# marks3 = int(input("Enter marks 3 :"))
#
# total_percent = ((marks1+marks2+marks3)/300)*100
#
# if(total_percent > 40 and marks1 > 33 and marks2 > 33 and marks3 > 33):
#     print("You passed!",total_percent)
# else:
#     print("Failed",total_percent)

#program for spam filter

# p1 = "Click this"
# p2 = "buy now"
# p3 = "For a very limited time"
# p4 = "Dont miss this chance"
#
# message = input("Enter your message :")
#
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This is a spam message!!")
# else:
#     print("Not a spam msg")

#Detect if a username has less than 10 char

# username = input(("Enter a username :"))
#
# if(len(username) < 10):
#     print("Heh! username is less than 10 char")
# else:
#     print("Perfect!")

#print if ur name is in the list

# lis = ["Sunayana", "Gaurav", "Ajay", "Biju"]
#
# name = input("Enter a name :")
#
# if(name in lis):
#     print("Name hai!")
# else:
#     print("Print name nhi h")


#print grades

marks  = int(input("Enter the marks"))

if(marks <= 100 and marks >=90):
    print("Grade : EX")

elif(marks < 90 and marks >=80):
    print("Grade : A")

elif(marks < 80 and marks >=70):
    print("Grade : B")

elif(marks < 70 and marks >=60):
    print("Grade : C")

elif(marks < 60 and marks >=50):
    print("Grade : D")

elif(marks < 50 ):
    print("Grade : F")