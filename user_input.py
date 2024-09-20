name = input('Enter your name: ')
age = input('Enter your age: ')
# Convert age to integer as input() returns a string
age = int(age)
location = input('Enter your location: ')

# Print personalized message
print(f'Hello {name}, you are {age} years old and live in {location}.') 
