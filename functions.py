__author__ = 'Builder'


def start():
    """
    this is a simple start function which actually does nothing but adds a and b
    """
    a = 10
    b = 20
    c = a + b
    print(c)


print(start.__doc__)  # prints the commented discription of the function start using (_doc_)
print(dir())  # shows all the internal functions of python

# in diffeent functions , same name can be used and both are considered as seperate entities
# data changed to local scope and global scope are totally diffrent no matter it is refered by same name
sauce = ['sauce1', 'sauce2', 'sauce3']  # list outside and inside function having same name diffeent data


def new_sauce():
    # this function creates new sauces
    sauce = ['sauce4', 'sauce5', 'sauce6']
    return sauce


print("normal sauce is %s" % sauce)  # both are diffrent
temp = new_sauce()
print("New sauce data is %s" % temp)



# ------------------------------------------------------------------------------------------------------------------------"
# 2 diffrent methods to check the given input present in the dictionary

# method 1
"""
def checking(alpha,to_check):
    for i in alpha:
        if i==to_check:
            print("value of %s is %s" %(to_check,alpha[i]))
            break;
        else:
            print("not got")
"""


# method 2, using try and except
def checking(alpha, to_check='d'):  # default parameters
    try:
        count = alpha[to_check]
    except:
        count = 0
    return count


alpha = {'a': 1, 'b': 2, 'c': 5, 'd': 4}
to_check = 'c'
count = checking(alpha, to_check)
print("value of the given value is %s" % count)


# using generic programming to find whether it is list or tuple or dictionary
def generic_use(tuple):
    if type(tuple) == type([]):  # if type ==[] then list
        print("It is a list")
    elif type(tuple) == type(()):  # it type ==() then tuple like that
        print("it is tuple")
    else:
        raise TypeError("TypeError is occured")    #raises an Error if it goes to else


list = ['list1', 'list2', 'list3']
tuple = ('tu1', 'tu2', 'tu3')
dictionary = {'dict1': 4, 'dict2': 5, 'dict3': 6}
string = "hello python"

generic_use(list)
