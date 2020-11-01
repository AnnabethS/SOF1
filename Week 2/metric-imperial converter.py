conversionDirection = input("Do you wish to convert to [M]etric or [I]mperial: ").upper()
conversionType = input("Do you wish to convert [W]eight, [L]iquid or, [D]istance: ").upper()
if conversionDirection=="M":
    #Imperial to Metric Conversions.
    if conversionType=="W":
        #Stones and Pounds to Kg
        stones = int(input("Enter amount of stones: "))
        pounds = int(input("Enter amount of pounds: "))
        kg = (stones*6.3502932) + (pounds*0.4535924)
        print(stones, "st and", pounds, "lb is", kg, "kilograms.")
    elif conversionType=="L":
        #Pints to Litres
        pints = int(input("Enter amount of pints: "))
        litres = pints*0.4731765
        print(pints, "pints is", litres, "litres.")
    elif conversionType=="D":
        #Feet and Inches to Litres
        feet = int(input("Enter amount of feet: "))
        inches = int(input("Enter amount of inches: "))
        metres = (feet*0.3048) + (inches*0.0254)
        print(feet, "ft and", inches, "in is", metres, "m")
    else:
        print("invalid Weight / Liquid / Distance Selection, type letter indicated in []. Exiting...")
elif conversionDirection=="I":
    #Metric to Imperial Conversions.
    if conversionType=="W":
        kg = float(input("Enter amount of kg: "))
        stones = kg // 6.3502932
        pounds = (kg % 6.3502932) / 0.4535924
        print(kg, "kg is", stones, "st and", pounds,"lb.")
    elif conversionType=="L":
        litres = float(input("Enter amount of litres: "))
        pints = litres/0.4731765
        print(litres, "L is", pints, "pints.")
    elif conversionType=="D":
        metres = float(input("Enter the amount of metres: "))
        feet = metres // 0.3048
        inches = (metres % 0.3048) / 0.0254
        print(metres, "m is", feet, "ft and", inches, "in.")
    else:
        print("invalid Weight / Liquid / Distance Selection, type letter indicated in []. Exiting...")
else:
    #Invalid Selection Handling
    print("Invalid Metric / Imperial Selection, type letter indicated in []. Exiting...")
    input()
