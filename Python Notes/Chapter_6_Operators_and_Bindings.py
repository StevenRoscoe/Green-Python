#Boolean Operators:
print(not True)         #False
print(not False)        #True

print(True or True)     #True
print(True or False)    #True
print(False or False)   #False
print(False or True)    #True

print(True and True)    #True
print(True and False)   #False
print(False and False)  #False
print(False and True)   #False


#Comparison Operators
print(1 < 2)            #returns True
print(2 < 1)            #returns False
print(1 <= 1)           #returns True
print(2.0 >= 3)         #returns False
print('a' > 'b')        #returns False
print('bb' >= 'ba')     #returns True

#Use the 'ord' function to tell the numerical value of the character:
print(ord('A'))
print(ord('Z'))

print(1 == 1)           #Prints True as the '==' sign means exactly the same
print('a' == 2)         #Prints False

print(1 != 1)           #Prints False as the '!=' sign means does not equal
print(2 != 1.0)         #returns True

#The identity ('is') operator says that it has to eb the exact same:
print(1 is 1)           #returns True
print(1.0 is 1)         #returns False as they are two distinct objects
print('s' is 's')       #returns True
print('a' is not 'a')   #returns False


#Having operations inside of parenthesis () tells Python to handle them first.