#Comments in Python can be initiated with the '#' symbol. Anything after that symbol will not be executed by Python. They can be put anywhere in your code.
#You can't write block comments in Python.


#A variable is a pointer to an object. They are used to store information that can be used at a later time.
#Variables normally start off with a lowercase letter or underscore (_).
#Ex:
my_str = "This is a simple string"      #my_str is the varibale and it was assigned the string wrapped in quotations
print(my_str)               #prints the string

#You can also reassign values to a previous string:
my_str = "This is a different string"
print(my_str)

#The += allows you to add something onto the end of your string:
my_str += " for a different program!"                               #Notice the space before starting the string. This adds a space for the next work you will be using in your string
print(my_str)

#You can even assign variables to integers
#Ex:
my_str = 19
print(my_str)


#A \n in Python is known as an escape sequence. It is used to create a new line.
print("This is a new line.\nAnd this is a new line!")

#Operators are special symbols in Python that carry out arithmetic or logical computation:
print("pass" + "word")
print("He" * 10)
print(4 * "Ha")

#A method is a function that belongs to an object in Python. You would use a period (.) right after an objec to call the object.
#Ex:
print("my_string".find('t'))            #Putting a period gives you access to all methods. The 'find' method finds the position where the letter is in the string. The 't' is in the 4th position in the string.
print("my_string".find('in'))           #The 'i' in the string is in the 6th position, so we just want to make sure it's in the string.

print("TesTInG".lower())                #Prints the entire string in lowercase format. Also make sure you have parenthesis after your method as this calls the function.
print("PassWord123".lower())
print("i love python!".upper())         #Prints the entire string in uppercase format. 

#There are more escape sequences when it comes to Python.
#One example is the tab escape sequence:
print("He's\toutside!")                #The '\t' escape sequence allows you to make a tab in between a string.
print("New\nLine")                     #The '\n' escape sequence creates a new line

#You can use single quotes inside double quotes and vice versa.
#Ex:
print("'Single' in Double")
print('"Double" in Single')


#Booleans represent whether or not something is true or false.
#The values for Booleans are 'True' and 'False'


#Integers:
print(2 + 2)

#Floats (Decimal):
print(5.0 + 9.6)

#Scientific Notation:
print(4.5e9)            #4.5e9 == 4.5 * (10 ** 9). Can also use a capital E as well.
print(4.5e-2)           #4.5 times 2 to the negative power.