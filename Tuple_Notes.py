#Tuple- an immutable(non-changeable) sequence type with a fixed length.
#A point will always have two items in it, an x-coordinate and a y-coordinate.
#Ex:
#point = (2.0, 3.0)

#You can't modify point once it's already been set.
#point[0] = 1
#It doesn't work because the tuple cannot be modified.

#You can however modify the tuple if its in 3d space with the following:
#point_3d = point + (4.0,)
#print(point_3d)
#This will concatenate the added one-tuple(4.0) with the point, just make sure you add the comma at the end to state that it is a tuple.

#You can use a tuple in very specific situations.
#One situation is when you need to unpack them into separate variables:
#Ex: 
#x, y, z = point_3d
#print(x)
#print(y)
#print(z)
#This will set the coordinates in the tuple to the variables specified.

#You can also add a tuple into a list and vice-versa:
#my_list = [1, 2, 3]
#my_tuple = (my_list, 1)
#print(my_tuple)
#other_list = [1, 2, my_tuple]
#print(other_list)

#Since the tuple has a character that can be modified inside of it, you can use the .append method to add a character:
#Ex:
#my_list.append(1)
#print(my_tuple)

#This will also cascade down into our other list:
#print(other_list)
