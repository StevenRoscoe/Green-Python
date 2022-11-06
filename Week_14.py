#EC2 Random Name Generator

import random
import string

#User input needed to name their department
dept = set(["finops", "marketing", "accounting"])
names = input("What is the name of your department? ").lower()
if names not in dept:
    print("The department you chose is not available...")
    exit()

#User input needed to tell if they need names for their department    
unique_names = input("Will you need names for your department? Enter yes/no... " ).lower()
if unique_names == "yes":
    print("Continue... ")
elif unique_names == "no":
    print("Exiting... ")
    exit()

#User input needed to tell how many instances they need generated    
instance = int(input("How many EC2 instances do you want generated? "))
for instance in range(instance):
    number = random.randint(0, 500000000000)
    print(names, '...', number)