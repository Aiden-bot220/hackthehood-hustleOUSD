# Lab 3

# Task 1: Working with Strings
food = 'shin ramen'
print(food[:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# Task 2: Working with Lists
number_list = [1, 8, 32, -5, 0]
number_list.append(67)
print(number_list)
number_list.insert(3, 69)
print(number_list)
number_list.pop()
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(1)
print(number_list)

# Task 3: Working With Dictionaries
books = {'Leigh Bardugo': 'Six of Crows', 'Scott Lynch': 'Lies of Locke Lamora', 'J.K. Rowling': 'Harry Potter', 'Camu': 'The Stranger'}
print(books.keys())
print(books.values())
print(books.get('Scott Lynch'))
books.pop('Leigh Bardugo')
print(books)
del books['J.K. Rowling']
print(books)

for x in books:
    print(x)