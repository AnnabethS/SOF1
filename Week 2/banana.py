pricePerKG = 3
postAndPack = 4.99
discount = 1.50
orderAmount = float(input("Enter amount of bananas required in KG: "))
price = orderAmount*pricePerKG
if price>50:
    price = price - discount
print("The price of the order is:", price, "pounds")

