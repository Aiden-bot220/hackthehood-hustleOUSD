# Lab 5 Aiden Ye

# Step 1
def cat_greeting(word):
    print(f'Cat says {word}')

cat_greeting("meow")

# Step 2
def generate_superhero_power():
    name = "Po"
    power = "Speed"
    print(f"{name}'s power is {power}")

generate_superhero_power()

#Step 3
def generate_superhero_power():
    power = "Speed"
    return power

print(generate_superhero_power())

#Step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("Staphon", "strength"))

#Step 5
def cat_greetings_loop():
    #for i in range(3):
        #print(f'The cat says {greetings}')

    greetings = ["meow," "purr," "meoeoeow"]

    for i in greetings:
        print('The cat says', i)

cat_greetings_loop()

#Step 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)

powers_test = ["speed","strength","teleportation","X-ray vision"]
generate_multiple_powers(powers_test)