#Define apply_discount function

def apply_discount(price, discount = 0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

#Define apply_tax function 
def apply_tax(price, tax = 0.07):
    price *= (1 + tax)
    return price

#Define total function using default values
def calculate_total(price, discount = 0.05, tax = 0.07):
    total = price * (1 + tax) * (1 - discount)
    return total 

#Call the function using keyword arguments
total_cost_default = calculate_total(price = 120, tax = 0.07, discount = 0.05)
print(f"Total cost with default discount and tax: ${total_cost_default}")

#Call the function using keyword arguments with custom values
total_cost_custom = calculate_total(price = 100, discount = 0.10, tax = 0.08)
print(f"Total cost with custom discount and tax: ${total_cost_custom}")








