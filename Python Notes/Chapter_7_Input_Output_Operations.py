#Typecasting is how we move an object from one type to another.
#Ex:
print(float(1))     #turns the integer 1 into a float of 1.0
print(int(1.3))     #doesn't round, only truncates the number
print(str(1))       #returns a string of '1'
print(str(False))   #returns a strinf of 'False'
print(int('1'))     #returns integer of 1

#Everything in Python has a True and False value:
print(bool(1))      #returns True
print(bool(95.56))
#Anything that has a 0 or nothing value if for the most part False:
print(bool(0.0))
print(bool(''))


#The 'input' function is used to get user information for programs we write.
name = input("What is your name? ")     #put a space after the end of the sentence otherwise the user will type directly after the string
color = input("What is you favorite color? ")
age = int(input("How old are you? "))


#You can do a lot with the print function as shown below:
print(name)
print("is " + str(age) + " years old")      #you can add words together and make age into a string along with the sentence
print("and loves the color " + color + ".")

#Using the end function allows the code block to print in one line:
print(name, end=" ")
print("is " + str(age) + " years old", end=" ")      
print("and loves the color " + color + ".", end=" ")