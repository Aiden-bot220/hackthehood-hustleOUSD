# Lab 6 - Aiden Ye
import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        print(f"{self.name} battles {opponent.name}!")
        # Randomly choose winner
        winner = random.choice([self, opponent])
        print(f"{winner.name} wins the battle!")

    def add_ability(self, ability):
        '''Adds an ability to the existing abilities list'''
        self.abilities.append(ability)
        print(f"{ability.name} has been added to {self.name}'s list.")

    def sum_of_attacks(self):
        '''Loops through abilities list and sums up all '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Adds an armor to the armor list.'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s list")

    def defend(self):
        '''Loops through armors list and sums up all of block values.'''
        total_block = 0
        for armor in self.armors:
            total_block =+ armor.block()
        return total_block

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200

    my_hero1 = Hero("IronMan", 200)
    print (my_hero1.name)
    print (my_hero1.current_health)

    my_hero1.battle(my_hero)
    fireball = Ability("Fireball", 50)
    void = Ability("Void", 40)
    poison = Ability("Poison", 55)
    my_hero.add_ability(fireball)
    my_hero.add_ability(void)
    my_hero.add_ability(poison)
    print(my_hero.sum_of_attacks())
    shield = Armor("Shield", 40)
    helmet = Armor("Helemet", 25)
    boots = Armor("Boots", 15)
    my_hero.add_armor(shield)
    my_hero.add_armor(helmet)
    my_hero.add_armor(boots)
    print(my_hero.defend())

