#Functions allow you to group chunks of code together into reusable blocks for parameteres that can be defined.
#Functions are written out using the 'def' keyword:
#def print_something(something):
    #pass

def print_name(name):
    print(f"Name is {name}")
    
print_name("Steven")


#To be able to call a function and have that value saved to a variable, we need to return a value:
def add_two(num):
    return num + 2
    
result = add_two(2)
print(result)