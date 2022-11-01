#A dictionary in Python is a data structure that consists of a collection of key-value pairs that maps the key to its associated value.
#A key has to be an immutable type, and it has to be unique.
#To create a dictionary you would use the character '{}'
#Ex:
#ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
#print(ages)

#You can have the computer read the dictionary:
#print(ages['kevin'])

#The computer will not read an item not in the dictionary:
#print(ages['billy'])

#Dictionaries are mutable types, so you can add items to them:
#ages['kayla'] = 21
#print(ages)

#You can also re-assign values in a dictionary:
#ages['kevin'] = 60
#print(ages)

#You can also delete values in a dictionary:
#del ages['kevin']
#print(ages)

#You have acces to the 'in' and 'not in' operations in a dictionary:
#'kevin' in ages

#If you wanted to create a dictionary, you can do the following:
#weights = dict(kevin=160, steven=205, martha=125)
#print(weights)
#This will translate each parameter into a key-value string.

#Another way you can create one is by using tuples:
#colors = dict([('kevin', 'blue'), ('bob', 'red'), ('martha', 'orange')])
#print(colors)


#Now let's look at the methods that dictionaries to provide to us
#ages = {'kevin': 61, 'bob': 79}
#You can get all they keys in a doctionary by using the .keys() method
#print(ages.keys())

#To get a list back you would do the following:
#print(list(ages.keys()))

#To get the values of the keys:
#print(ages.values())
#print(list(ages.values()))

#Gives a list of tuples:
#print(ages.items())
#print(list(ages.items()))