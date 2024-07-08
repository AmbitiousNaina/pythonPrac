# name = input("Enter your name :")
# # print("Good Afternoon",name)
# print(f"Good Afternoon {name}")


# letter = '''Dear <|name|> you are selected <|Date|>'''
# print(letter.replace("<|name|>","Sunayana").replace("<|Date|>","24th Aug"))


# detect double spaces
# sentence = "Sunayana is a good   girl"
#
# print(sentence.find("  "))

# replace double spaces
sentence = "Sunayana is a good   girl"

print(sentence.replace("  ", "")) #strings are immutable that means you cannot change them after creation,new string create hogi
print(sentence) #it will show you the og string only.
