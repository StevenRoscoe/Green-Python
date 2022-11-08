#Functions allow you to group chunks of code together into reusable blocks for parameters that can be defined.
#Functions are written out using the 'def' keyword:
#def print_something(something):
    #pass

#def print_name(name):
    #print(f"Name is {name}")
                                    #Make sure to leave a space in-between the function to call the function
#print_name("Steven")


#To be able to call a function and have that value saved to a variable, we need to return a value:
#def add_two(num):
    #return num + 2
                        
#result = add_two(2)
#print(result)


#Parameters are variables that are defined within a function.
#Arguments are th values that you pass in for parameters when you call a function.

#def contact_card(name, age, car_model):
    #return f"{name} is {age} and drives a {car_model}"

#contact_card(name="Steven" , age=25, car_model="Mustang")
#print(contact_card)


#Recursion is the act of calling a function within itself:
#Fibonnaci Calculation:
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
        
    return fib(n - 2) + fib(n - 1)
    
item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))
print(fib(item_to_calculate))