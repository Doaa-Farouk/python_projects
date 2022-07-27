import keyword
import collections
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
# 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
# 'raise', 'return', 'try', 'while', 'with', 'yield']
# c = None
# print(type(c))
# a = b = 2
# print(a,b)
# if 3> 4:
#     pass

# print('h\tf')
# print('h    f')
# print(2>4)
# # print(2+4j>2+3j)
# v = (2,3)
# x = (2,3)
# print(v.__hash__())
# print(x.__hash__())
# a = '23.4'
# a = float(a)
# print(type(a))
# a = int(a)
# print(type(a))
# l= ['x','s','d']
# print(l.index('s'))
# dictionary = {'Yemen':'Sanaa','US':'Newyourk'}
# # print(dictionary.keys())
# # print(dictionary.values())
# print(dictionary['US']) # getting the value by its key name
# for k  in dictionary.keys():
#     print(f"the capital of {k} is {dictionary[k]}")
# k = {'s', 'D', 'R'}
# print(k)
# l = {2, 1, 5, 2}
# print(l)

# s = [2,9,4,1,4]
# print(s)
# print(set(s))
# d= set(s)
# print(d)


# 
dictionary = collections.defaultdict(lambda:'Not Found') # used when the key does not exist
# dictionary = {'Yemen':'Sanaa','US':'NewYork'}
dictionary['US']= "NewYork"
dictionary['Yemen']= "Sanaa"
print(dictionary['US'])
print(dictionary['U'])


# print(collections.defaultdict.__doc__)


# user input are always of type string str
# a = input("ENter a number:")
# print(int(a)+2)
