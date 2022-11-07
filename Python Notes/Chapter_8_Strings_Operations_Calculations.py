#Immutability means something cannot be changed.
#If something is mutable it can be changed.


#The 'len' function lets you know how long a string is:
my_str = 'testing'
print(len(my_str))      #length of testing is 7 characters


#You can interact with individual items in a string, known as indexing:
test_str = 'testing'
print(test_str[0])      #with indexing, the string starts off with 0 and goes up from there
print(test_str[3])

print(test_str[len(test_str) - 1])      #prints the length of the string minus 1
print(test_str[-1])

#With slicing we can get every other item or a certain group of items in a string:
print(test_str[0:2])        #prints from first character to the second then stops at the 3 character in the string
print(test_str[3:5])
print(test_str[2:len(test_str)])        #prints from the third character to the end of the string
print(test_str[2: ])                    #prints the same as before and is easier
print(test_str[1:5:2])                  #prints the characters in the string from position 1 to 4 while stepping two spaces at a time
print(test_str[::-1])                   #prints the entire string backwards
