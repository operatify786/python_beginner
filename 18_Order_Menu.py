Menu = {"Pizza":"3000",
        "Burger":"800",
        "Shawarma":"500",
        "Wings":"1000",
        "Ice cream":"400",
        "Nuggets":"1500",
        "Shakes":"1200",
        "Kabab":"600",
        "Coca cola":"300",
        "Salad":"200",
        "Pasta":"900" }



print("--------Menu----------")
for key,value in Menu.items():
    print(f"{key:12}: Rs {value}/-")
print("----------------------")

cart = []
bill = 0

while True:
    food = input("Enter your food you want to order: ").capitalize()
    if Menu.get(food) is not None:
        cart.append(food)
        bill += int(Menu.get(food))
    elif food == "Q":
        break



print("-----Your Order-------")
for item in cart:
    print(f"{item:12}: Rs {Menu.get(item)}")
print(f"Your total bill is Rs {bill}/-")
print("----------------------")
