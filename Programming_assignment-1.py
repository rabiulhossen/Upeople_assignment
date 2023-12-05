# Task-01

#  prints the circle's circumference. 
print("task-01")  # just for sophisticate output
def print_circum (radius):
    circumference = 2* 3.14159* radius
    return circumference

# print three times
print("circumference of a circle1:",print_circum(3))
print("circumference of a circle2:",print_circum(4))
print("circumference of a circle3:",print_circum(5.5))






# Task-02

print("task-02")  # just for sophisticate output

def calculate_total_price(item1_price, item2_price, item3_price, items):
    total_price = 0

    # each items price
    if "item1" in items:
        total_price += item1_price
    if "item2" in items:
        total_price += item2_price
    if "item3" in items:
        total_price += item3_price

    # Apply a 10% discount if the customer buys a combo pack.
    if len(items) == 2:
        total_price *= 0.9

    # Apply a 25% discount if the customer buys a gift pack.
    if "item1" in items and "item2" in items and "item3" in items:
        total_price *= 0.75

    return total_price

# Example usage:

# Purchase individual items ("item1" "item2" and "item3") and calculate the total price.
total_price_individual = calculate_total_price(200, 400, 600, ["item1"])
print(f"Total price for individual items: ${total_price_individual}")

total_price_individual = calculate_total_price(200, 400, 600, ["item2"])
print(f"Total price for individual items: ${total_price_individual}")

total_price_individual = calculate_total_price(200, 400, 600, ["item3"])
print(f"Total price for individual items: ${total_price_individual}")



# Purchase a combo pack and calculate the total price.
total_price_combo = calculate_total_price(200, 400, 600, ["item1", "item2"])
print(f"Total price for combo pack: ${total_price_combo}")

total_price_combo = calculate_total_price(200, 400, 600, ["item1", "item3"])
print(f"Total price for combo pack: ${total_price_combo}")

total_price_combo = calculate_total_price(200, 400, 600, ["item2", "item3"])
print(f"Total price for combo pack: ${total_price_combo}")

# Purchase a gift pack ("item1", "item2", and "item3") and calculate the total price.
total_price_gift_pack = calculate_total_price(200, 400, 600, ["item1", "item2", "item3"])
print(f"Total price for gift pack: ${total_price_gift_pack}")
