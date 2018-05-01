"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
from random import randint

list_len = randint(1,75)
rand_list = []

for i in range(0,list_len):
    rand_list += [randint(1,1000)]

print("List: ", rand_list)
print([element for element in rand_list if element%2 == 0])

"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([element for element in a if element%2 == 0])
"""
