__author__ = 'Builder'
# equals(==) and not equals(!=) work with list,tuples and dictionaries
# example
lista = ["a", 'b', 'c', 'd']
listb = ['a', 'b', 'd', 'c']
listc = ['a', 'b', 'c', 'd']
op1 = lista == listb  # even if same vakues present then too , order should be same in both the lists
op2 = lista == listc
print(op1)
print(op2)
print("pumPKin".lower())  # upper and lower

# >,<,==,!=,>=,<= can be applied and the output will be in the form of boolean values
if (not False):  # not false means true
    print("false")
a = 10
if (not a == 10):  # using not with condition
    print("a not equal to 10")
else:
    print("a is equal to 10")



    # try and except(good concept)

fruits = {'bananas': 23, 'mangoes': 12, 'apples': 10, 'pineapple': 25}
try:  # use of try (means if statements encunter an error then go to except)
    if fruits["oranges"] > 10:
        print("oranges are greater than 23 ")
except (KeyError) as error:  # if try is false then except works(here except works if there
    print("aww.. there are no  %s " % error)  # is keyerror which gets stored in error for further use


#    except:                               #simple except
#   print("there are no oranges")

#    except KeyError:                      #except when there is keyerror
#    print("There are no oranges")


# to bypass the error we use (PASS)
try:
    if (fruits["oranges"] > 10):
        print("there are oranges")
except KeyError as error:
    pass
print("no error means bypassed")

#usinf else after for loop
for food in ["a","b","c","d"]:
    if(food=="e"):
        print("e is present ")
        break
else :
    print("e is not present")