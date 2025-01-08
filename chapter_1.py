# 1. DATA TYPES
# this is a number data type
5384787

# This is a string data type (a string of characters - alphanumeric)
"my name is Oliver"

'hello world'

# sub-objective (print out the string hello world)
print('hello world')

# This is the list / array data type, contains a series or sequence of values that can be of any data type themselves
shopping_list = ['eggs', 'bananas', 'milk', 4, []]

# this is an object data type / dictionary
person = {
    "name": "Oliver",
    "age": 29
}

# boolean - true or false value
True
False

# None - absence of information
None

# A data type is a type of data that is friendly to python

#2.0 Variables - a variable is a label from some data
number_of_eggs = 5
#python 'case' uses _ for spaces 

my_string = 'hello world'

print(number_of_eggs * 2)

# 3.0 Logic and Operations
# if block - if condition is true, execute this code otherwise skip it
if number_of_eggs > 5:
    print(f'You have more than 5 eggs. You currently have {number_of_eggs} eggs!') #template literals with f in front of string
else:
    print('You have 5 or fewer eggs')

print ('We passed the if block')

if 'name' in person: 
    print(person['name'])  # return value associated with object / dictionary key
else:
    print('The key \'name\' is not available within the person dictionary')

if 'bananas' in shopping_list:
    print('Need to get bananas')
else: 
    print('Don\'t need bananas')

# Logical operators - and / or

if number_of_eggs > 5 and number_of_eggs < 20:
    print('we have more than 5 eggs and we also have less than 20!')

if number_of_eggs < 6 or number_of_eggs >= 20:
    print('Okay, the number of the eggs is outside the ideal range which is 5 - 20')

# operators
x = 3
y = 4
print(x * y + x - y / x)

#remainder operator / modulus (%)
remainder = y % x

#equality operator == (checks if the left is equal to the right)
print(remainder == 10 % 3)
x == y #this would be false because x is 3 and y is 4 and therefore not equal

# not (! or not)
x != y # this would be true because x is not equal to y

if not number_of_eggs == 4:
    print(f'The number of eggs is not equal to four, but instead: {number_of_eggs}')

# Loops (while / for)
count = 0
while count < number_of_eggs:
    print('hello world')
    count = count + 1
    if count == 3:
        break

for x in shopping_list:
    print(x)
    
for i in range(10):
    print(i)

length_of_my_array = len(shopping_list)

for j in range(length_of_my_array):
    current_index = j
    current_value = shopping_list[current_index]
    print(f'The current index is {current_index} and the value at that index in the list/array is {current_value}')

# Functions
# def for define to define functions in python

def print_funny_word(funny_word):
    # this function takes an argument and prints out the word provided as an argument in the following formatted string...
    # '''text in here''' triple quotation marks for multi-line strings
    print(f'{funny_word} is a funny word!')

print_funny_word('Schnee') # German for Snow

for k in range(3):
    print_funny_word('Gesundheit')

def multiply_two_numbers(a, b):
    return a * b

product = multiply_two_numbers(8, 7)
print(product)

#Class / Classes