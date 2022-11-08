#Lists are used to store multiple items in a single variable.
#my_list = [1, 2, 3, 4, 5]
#print(my_list)

#other_list = ['a', 1, 1.0, False]
#print(other_list)

#You can use indexing to get pull an item from the list:
#print(my_list[3])

#You cn use the 'len' function to see how long your list is:
#print(len(my_list))

#You can use slicing to get a portion of a list:
#print(my_list[0:2])
#print(my_list[0:])

#Step values also work:
#print(my_list[0::2])

#Lists are mutable, so you can modify them by assigning items to a different position:
#my_list[0] = 'a'            #moves 'a' to the first position in the list
#print(my_list)

#You can also concatenate (link) other items to a previous list:
#print(my_list + [8, 9, 10])

#You can even assign new items to a list with slicing:
#my_list[1:3] = ['b', 'c']
#print(my_list)

#You can also delete items out of a list:
#my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
#my_list[4:] = []
#print(my_list)

#Another way is to use the statement 'del':
#del my_list[0]
#print(my_list)


#You can use the append method to add items to a list:
#my_list.append(4)           #adds a 4 on the end of the list
#print(my_list)

#The insert method allows you to add an item to a certain position within the list:
#my_list.insert(0, 'a')      #the 'a' character will go into the first position within the list and moves everything else over
#print(my_list)

#If we want to know the position of an item in a list we can use the 'index' method:
#my_list.index(2)
#print(my_list)

#We can use the 'in' and 'not in' functions to tell if something is in or not in the list, and give back boolean values
#my_list = [1, 2, 3]
#print(4 in my_list)
#print(4 not in my_list)

#You can use the 'sorted' method to sort a list that is mixed up:
my_list = [1, 3, 9, 2, 15, 6, 0]
print(sorted(my_list))

#You can print a list in reverse with the 'reverse' method:
print(list(reversed(my_list)))
print(list(reversed(sorted(my_list))))