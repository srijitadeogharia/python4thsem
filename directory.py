# A dictionary in Python is a collection of data values,
# used to store data values like a map, unlike other Python Data 
# Types that hold only a single value as an element, a Dictionary 
# holds a key: value pair. Key-value is provided in the dictionary 
# to make it more optimized. Each key-value pair in a Dictionary is 
# separated by a colon : , whereas each key is separated by a ‘comma’.

# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)


#Accessing Key-value in Dictionary
#In order to access the items of a dictionary refer to its key name.
#  Key can be used inside square brackets. Using get() method we can 
# access the dictionary elements.

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))
