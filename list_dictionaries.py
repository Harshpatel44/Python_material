__author__ = 'Builder'

# String addition and copying
print("add1" + " " + "add2")  # addition
add3 = '5'
add4 = add3  # copying
print(add4)

# tuples and lists and dictionaries

tuple1 = ("a", "b", "c", "d", "e")  # tuples have ()
tuple2 = (tuple1, "others")  # copying tuple
print(tuple2)
print(tuple2[0])  # accessing tuple1 from tuple2
print(tuple2[0][1])  # accesing tuple1 elements from tuple 2

# in tuples editing not possible, in lists possible


a = ["harsh", "parth", "nidhi", "prachi"]  # list have []#
print(a)
print(a[0])
print(a[0][0])  # listing alphabets in list #
print(a[2][2])

a[2] = "nidhi2"  # modifying list
print(a)

a.append("patels")  # appending
print(a)

a.extend(["all", "new", "members"])  # extending by adding new entities
print(a)

c = ["these", "is", "something", "new"]
a.extend(c)  # extending by adding list c to it
print(a)

d = ["somethig", "really", "greaat"]
a.extend([d, "end"])  # extending by adding list which contain entity and list d (see ouput....it differs)
print(a)

print(len(a))  # finding length of lists

print(a[-1])  # finding the last element of list
print(a[-2])  # finding the second last element of the list and so on

b = {}  # making dictionaries have {}#
b[a[0]] = a[0][0]  # linking first letter with the first name stored in list a #
print(b)
print(b['harsh'])  # accesing it

# b[a[0][0]]=a[0]    #vice versa #
# print(b)

# print(b['h'])


# using values and keys function #
bcd = {"roll1": "127", "roll2": "128", "roll3": "129", "roll4": "130"}
print(bcd)
print("the rollno 1 is %s " % (bcd["roll1"]))
list1 = bcd.keys()
list2 = bcd.values()
print("all keys present are ")
print(list1)
print("all values present are ")
print(list2)

print(len(bcd))  # finding length of dictionaries

# slicing
x = ("this", "is", "called", "as", "tuples")  # tuples
x2 = x[2:5]
print(x2)
y = ["this", "is", "called", "as", "list"]
y2 = y[0:3]
print(y2)
z = "dont ever mess with me is a final warning"
z2 = z[9:25]
print(z2)


# popping (works with list and tuples)
list3 = [12, 13, 14, 15, 16]
okay = list3.pop(0)  # popping 0th element
print(okay)
okay2 = list3.pop(0)  # popping 1st element
print(okay2)
print(list3)  # print list
okay3 = list3.pop()  # popping last element when no index specified
print("the removed element is stored in okay3 is  %s" % (okay3))
print(list3)
list3.pop()  # just popped , stored nowhere
print(list3)

# sets(which contain no duplicate values)
alpha = ['a', 'b', 'c', 'd', 'b', 'a', 'd', 'c']
alpha2 = set(alpha)  # 1.using of set function by storing in alpha2
print(alpha2)
print(set(alpha))  # 2.using of set function directly


# using objects in lists
day = 10
month = 11
year = 2014
expiry = [day, month, year]
print("The expiry date is on %s-%s-%s" % (expiry[0], expiry[1], expiry[2]))

# practice
milk_carton = {"expiration": expiry, "f1_oz": 100, "cost": 1000, "brand": "amul"}
total_cost = milk_carton["cost"] * 6  # cost of six cartons
print("total cost is %s" % (total_cost))
