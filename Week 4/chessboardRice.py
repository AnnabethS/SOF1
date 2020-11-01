num = 1
letters = "ABCDEFGH"

for i in range(8):
    for j in range(8):
        print(letters[i] + str(j+1) + " : " + str(num*30) + "mg of rice")
        num = num*2
