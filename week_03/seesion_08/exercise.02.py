# random number буюу дурын утга

import random

roll_dice = random.randint(1, 6)
print(roll_dice)

is_heads = random.choice([True, False])
print("you flipped heads: " + str(is_heads))

# 4 shirheg hoolnii tsugluulga list uusgeed tvvniigee random oor hewleh

food_list = ['tsuvan','tahia shol', 'huushuur']
food_list = random.choice(food_list)
print("Your food:" + str(food_list))