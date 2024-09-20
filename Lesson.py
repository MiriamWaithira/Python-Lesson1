Favourite_Number = 77
print(f'My favourite number is {Favourite_Number}')
# String
greeting = 'Hello World'
print(greeting)
# Booloean
is_python_fun = True
is_python_boring = False
print(f'Is python fun? {is_python_fun}')
print(f'Is python boring? {is_python_boring}')

# CONTROL FLOWS- Allow you to make decisions in your coding
# if, elif, else statements
speed = 40
if speed > 70:
    print('Fast')
else:
    if speed > 50:
        print('Safe Driving')
    else:
        print('Slow')

# LOOPS For & while- used for iterations
# for- used when you have a definite number of loops
# while- used until a condition is met
for i in range(3):
    print(f'I love cars {i}')

# for while loop
Count_Down = 10
while Count_Down > 0:
    print(f'The count is {Count_Down}')
    Count_Down -= 1
print(f'The Count Down is Successful!!!')


# Functions- Reusable blocks of code
def greet(person):
    return f'Hello, How are you?, {person}'
# appply the function
print(greet('James'))
print(greet('Jane'))

# LISTS AND DICTIONARIES
fruits_list = ['Apple', 'Mango', 'Banana', 'Oranges']
fruits_tuple = ('Cherry', 'Pineapple', 'Strawberry')
print(fruits_list)
print(fruits_tuple)

# Dictionary
Contacts = {
    'Alice': '123456',
    'John': '789123',
    'Mark': '456789'
}
print(f'You can reach Mark here: {Contacts['Mark']}')


# # MODULES IN PYTHON- files that contain codes
# import inbuilt module
import math
kanamba = 49
# use a function from module math
result = math.sqrt(kanamba)
print(f'The square root of {kanamba} is: {result}')

# CREATING YOUR OWN MODULE
# import customized module
import greet_module
print(greet_module.greet('John'))


