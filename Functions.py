

menu = {'Pizza': 2.99,
        'Burger': 3.99,
        'Hot dog': 1.99,
         'Cheese': 0.59,
        'Ice cream': 1.49,
         'Churro': 0.79,
        'Soda': 0.89}

category = {"mains":['Burger', 'Hot dog', 'Pizza'],
            "sides":['Churro', 'Cheese', 'Ice cream'],
            "drink":['Soda']}

def display_menu(menu, category):
    categorized_menu = {
        "mains":{},
        "sides":{},
        "drink":{}
    }
    for category, items in category.items():
        for item in items:
            categorized_menu[category][item] = menu[item]
    return categorized_menu
organized_menu = display_menu(menu, category)
print(organized_menu)

def total_price(item1,item2):
    
    
    return menu[item1]+ menu[item2]

print(total_price('Soda','Burger')) 
def price_difference(item1,item2):
    return abs(menu[item1]- menu[item2])
print(price_difference('Hot dog', 'Ice cream'))
def price_inflation(item,menu,multiplier):
    menu[item] = menu[item] * multiplier
    return menu
updated_menu = price_inflation('Soda', menu, 2)
print(updated_menu)
def price_deflation (item,menu,multiplier):
    menu[item] = menu[item] * multiplier
    return menu
updated_menu2 = price_deflation('Cheese', menu, .1)
print(updated_menu2)