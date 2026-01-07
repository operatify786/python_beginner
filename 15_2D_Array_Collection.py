fruits = ["apple", "Mango", "Orange"]
meats = ["Chicken", "Beef", "Mutton"]
veg = ["Ginger", "Garlic", "Tomato"]

grocries = [fruits, meats, veg]

for grocry in grocries:
    for food in grocry:
        print(food, end="")
    print(" ")