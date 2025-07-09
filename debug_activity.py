#Debugging activity 

#Snippet 1

x = 10
y = 2
result = x / y #There would be a zerodivision error, because 10 cannot be multiplied by 0 or it would give us just 0.
print("Result:", result)

#Snippet 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i+0]) #The index has to be + 0 because it begins at 0.

#Snippet 3

def calculate_area(radius):#There needs to be a colon after defining something.
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#Snippet 4

def is_even(number):
    if number %2 == 0:#There needed to be a colon after thte 0.
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

#Snippet 5

for i in range(5):#There needs to be a colon after the parenthesis. 
    print(i)

#Snippet 6

def greet(name):
    return "Hello, " +name  #missing the +, if it doesn't have it, it won't join together

print(greet("Alice"))

#Snippet 7

numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number #There needs to be an indent after using a for loop
print("Sum of numbers:", sum)

#Snipper 8

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) #It needs to be n-1 not n+1 or else it would constantly keep adding, and it will never reach 0
    
print(factorial(5))

#Snippet 9

name = input("Enter your name: ")
if name == "Alice" or name == "Bob": #always evaluated to True, needs to have name == to also refer to bob
    print("Hello, " + name)
else:
    print("Hello, stranger!")

#Snippet 10

def divide_numbers (x, y):
    if y == 0:
        return "Can't divide by zero!"
    else:
        result = x / y
        return result

num1 = 10
num2 = 2 #can't divide by zero
print(divide_numbers(num1, num2))