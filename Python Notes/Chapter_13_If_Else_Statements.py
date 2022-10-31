#Conditionals allow us to take comparison operations, such as 'a' < 'b' returning True, and do something based off this value.
#To perform a conditional, you use the 'if' statement.
#Ex:
#if 'a' < 'b': 
    #print("CONDITION was true")
    
#if False:
    #print("Was true")
#else:                       #The 'else' statement is the companion to the 'if' statement
    #print("Was false")
    
#You can also use the 'elif' statement for even more powerful coding.
#Ex:
#if 'b' < 'a':
    #print("This is true")
#elif 'c' < 'd':
    #print("Second condition is true")   #This function will print this line of code as being True because 'c' is less than 'd' 
#else:
    #print("no condition is true")
    
#Lets now try it with inputs
#name = input("What is your name? ")

#if len(name) >= 6:              # The '>=' character means greater than or equal to, and vice versa 
    #print("Your name is long")
#elif len(name) == 5:            # The '==' character means exactly
    #print("Your name is 5 characters")
#elif len(name) >= 4:
    #print("Your name is 4 or more characters")
#else:
    #print("Your name is short.")
#Whichever conditional is hit first will be the one to run

#You can use the 'pass' statement if you don't want to add anything to your conditional
#Ex:
#name = "Steven"
#if name == "Kevin":
    #print("Hello Kevin")
#else:
    #pass