import random


names = ["John", "Mike", "Ali", "Tyson"]

num_items = len(names)

random_choice = random.randint(0, num_items -1)

who_is_paying = names[random_choice]

print(who_is_paying + " is going to buy a meal.")
