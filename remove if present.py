'''
Write a Python program to remove an item from a set if it is present in the set.
'''
s={1,6,3,4,4,5}
if 4 in s:
    s.remove(4)
print(s)