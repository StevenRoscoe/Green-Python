#UTF = Unicode Transformation Format

#print(ord(''))
#Prints the number that represents the unicode format of a string

#print(chr())
#Prints the unicode character of the specified number

#A string has a lot of methods that can be called on it.
#A method is a function that is tied to the item and can provide functionality within the state of the object.
#.lower() = prints the string in lowercase
#Ex:
#print("This".lower())
#my_str = 'tEsTinG'
#print(my_str.lower())

#.upper() = prints the string in uppercase
#print(my_str.upper())

#.capitalize() = capitalizes the first word in a string and leaves everything else lowercase
#print(my_str.capitalize())

#.title() = capitalizes the first letter in each word in a multi-word string
#print("This is a multiword sTRing".title())

#For email addresses, you can use these methods to see if they match up:
#print("Kevin@example.com" == "kevin@example.com")
#This returns False

#print("Kevin@example.com".lower() == "kevin@example.com")
#This returns True

#There are other methods that can be used with strings as well:
#print(my_str.isascii())

#.isascii() checks to see if the string can be represented in the ascii format
#.isalpha() checks to see if the object is a character or made up of characters
#.isalnum() checks to see if the object is made up of characters and/or numbers

#Another thing you can do with strings is work with them as tokens.
#You can use the .split() method to split a function
#Ex:
#phrase = "This is a simple phrase"
#words = phrase.split()
#print(words)

#You can use the .join() method to join a function that was split:
#print(", ".join(words))

#Another ex:
#lines = ['First line', 'Second line', 'Third line']
#output = '\n'.join(lines)   #The '\n' method creates a new line in the code
#print(output)

#You can use the .format() method to insert a character, or characters, into a string:
#template = "Hello, my name is {}, and I really enjoy {}. Have a nice day!"
#print(template.format('Steven', 'Python'))

#You can also do this another way using indexing:
#template = "Hello, my name is {0}, and I really enjoy {1}! Have a nice day! - {0}"
#print(template.format('Steven', 'Python'))
