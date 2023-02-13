import input_ecc as ecc

price = ecc.try_in("Input a price as a whole integer:\n>| ", "int")

change = [0, 0, 0]

while price > 0:
    if price - 5 >= 0:
        change[0] += 1
        price -= 5
    elif price - 2 >= 0:
        change[1] += 1
        price -= 2
    elif price - 1 >= 0:
        change[2] += 1
        price -= 1

print(str(change[0]) + " 5 dollar bill(s), " + str(change[1]) + " 2 dollar coin(s), " + str(change[2]), + " 1 dollar coin(s).")
