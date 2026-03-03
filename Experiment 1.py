# Grocery Billing System

prices = [50, 30, 20, 100]
quantities = [2, 3, 1, 4]

discount_rate = 10   # 10%
tax_rate = 5         # 5%

subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount_amount = subtotal * (discount_rate / 100)

amount_after_discount = subtotal - discount_amount

tax_amount = amount_after_discount * (tax_rate / 100)

total_cost = amount_after_discount + tax_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Amount after Discount:", amount_after_discount)
print("Tax Amount:", tax_amount)
print("Final Total Cost:", total_cost)
