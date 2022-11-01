#A 'while' loop is a loop that allows you to go through a block of code with a condition to see if it returns True or constantly repeats, then stops.
#For this, you would use a 'while' statement followed by a CONDITION, then go from there.
#Ex:
#while CONDITION:
    #print("Something")
    
#while 1 < 2:
    #print("Something")  #This will create an infinite loop
    
#Adding variables in a while' loop can create a fix for the infinite loop problem:
#count = 1
#while count <= 4:
    #print("looping")
    #count += 1
#The 'while' loop is great if you want to potentially iterate an unknown number of times or a specific number of times, or if you do want to have an infinite loop.


#A 'for' loop is used to iterate over a sequence, which is either a list, tuple, dictionary, set, or string.
#Ex:
#for TEMP_VARIABLE in SEQUENCE:
    #pass

###The name you give to the TEMP VARIABLE doesn't matter

#Let's try it with a list:
#colors = ['blue', 'green', 'red', 'purple']
#for color in colors:
    #print(color)
    
#Tuple:
#point = (1, 2, 3)
#for value in point:
    #print(value)
    
#Dictionary:
#ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
#for key in ages:
    #print(key)
    
#Going back to what we learned about dictionaries, you can get the key and values of those keys with the .items() method. Using for key, value it will unpack the dictionary:
#for key, value in ages.items():
    #print(key, value)
    
#String:
#for letter in 'my_string':
    #print(letter)
    

#You can create loops and conditionals inside of other loops and coniditionals as well:
#counter = 1
#while counter <= 25:
    #if counter % 4 == 0:
        #print(counter)
    #counter += 1            #The counter will go from the number 1 to 25 to see which numbers are divisible by 4 evenly, then print them

#You can also use conditionals inside of a loop to stop the execution and either go back to move on to the next iteration, or completely cancel out of a loop before it would have stopped itself.
#We do this by using the 'continue' and 'break' statements. If we only want to print out odd numbers we can do something like this:
#count = 0
#while count < 10:
    #if count % 2 == 0:
        #count += 1
        #continue             #Every single line after the continue statement won't be executed at all, so it will go up to the next iteration of the loop.
    #print(f"We're counting odd numbers: {count}")           #The 'f' is shorthand for a format string
    #count += 1
    
#count = 1
#while count < 10:
    #if count % 2 == 0:
        #break                #Stops the execution entirely and continues with whichever the next line of code is
    #print(f"We're counting odd numbers: {count}")
    #count += 1
    
#Let's try it with a for loop:
#colors = ['blue', 'green', 'red', 'purple']
#for color in colors:
    #if color == 'blue':
        #continue             #When the statement hits blue it will not print it and go to green
    #elif color == 'red':
        #break                #If the statement hits red, it will stop the execution entirely and not print purple
    #print(color)
    

#You can also add the 'else' statement into your 'while' and 'for' loops as well:
#count = 1
#while count <= 4:
    #print(count)
    #count += 1
#else:
    #print("While loop completed")
    
#The power of the 'else' statement comes from when we want to break out of a loop
#Ex:
#colors = ['red', 'pink', 'blue', 'orange', 'green']
#for color in colors:
    #if color == 'orange':
        #print('Orange is in the list')
        #break
#else:
    #print("Orange is not in the list")
    

#If you want to iterate a certain number of times in a loop, you can use the 'range' function:
#my_range = range(10)
#print(my_range)              #Creates a range from 0 to 10
#print(list(my_range))        #Prints a list from a range of 0 to 10

#print(list(range(1, 14, 2)))    #Prints a list within a range from 1 to 14 that counts up by 2

#count = 1
#while count <= 4:
    #print("looping")
    #count += 1

#The range function can do the same:
#for _ in range(4):            #The _ variable is another way of saying I don't need this variable
    #print("looping")