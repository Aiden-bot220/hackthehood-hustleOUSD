

menu = {'Pizza': 2.99,
        'Burger': 3.99,
        'Hot dog': 1.99,
         'Cheese': 0.59,
        'Ice cream': 1.49,
         'Churro': 0.79,
        'Soda': 0.89}
def display_menu():
    for item, price in menu.items():
        print(f"{item}: {price:.2f}")

display_menu()
def total_price(item1,item2):
    
    
    return menu[item1]+ menu[item2]

print(total_price('Soda','Burger')) 
def price_difference(item1,item2):
    return abs(menu[item1]- menu[item2])
print(price_difference('Hot dog', 'Ice cream'))
def price_inflation(item,multiplier):
    return (menu[item]*multiplier)
print(price_inflation('Churro',2))
def price_deflation (item,multiplier):
    return (menu[item]*multiplier)
print(price_deflation('Churro',0.5))