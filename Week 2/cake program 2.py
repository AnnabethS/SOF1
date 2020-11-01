number_cakes = int(input("Enter the number of cake(s) you want to buy: "))
cake_price = 2.50
bill = cake_price * number_cakes
if number_cakes==1:
    print("The price of a cake is:", cake_price)
elif number_cakes>1:
    print("The price of", number_cakes, "is", bill, "pounds.")
else: #number of cakes entered is less than or equal to 0
    print("Error: Invalid number of cakes")
