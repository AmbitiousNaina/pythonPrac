d = {}  #empty dict
print(d,type(d))
marks = {
    "Anshu" : 100,
    "Biju" : 40,
    "Viju" :30
}
# print(marks, type(marks))
# #print(marks[0]) #you cant access it like this, instead do the foll
# print(marks["Anshu"]) #use the [] and insert the key
#
# k=marks.items() #returns the dict in the for of a tuple
# print(k, type(k))
# j=marks.keys()
# print(j, type(j))
# p=marks.values()
# print(p, type(p))


# l = ['anshu','viji']
# print(l)
# print(type(l))

# marks.update({"Anshu" : 99, "Shinoy" : 100})
# print(marks)

# print(marks.get("Anshu")) #returns none
# print(marks["Anshu"]) #returns error

print(marks.pop("Anshu"))
print(marks)
print(marks.popitem())
print(marks)