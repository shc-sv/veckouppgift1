# Vecouppgift 1
# Q3:

def q3_1a_1b():
    # Try to convert the input to an integer
    try:
        number1 = input("Mata in ett heltal här: ")
        error_number = number1
        number1 = int(number1)
        number2 = input("Mata in ett annat heltal här: ")
        error_number = number2
        number2 = int(number2)
        sum = number1 + number2
        print(f"Summan av {number1} och {number2} är {sum}. Det blir rätt! :) ")
    except ValueError:
        print(f"{error_number} är inte ett heltal.")


def q3_2a():
    jacket_price = 2000
    discount = 50
    print(f"Jackan kostar {jacket_price} kr. Nu är den på rea, {discount}%. ")
    cost = jacket_price * discount / 100
    print(f"Du ska betala {cost} kr.")

def q3_2b():
    jacket_price = 2000
    print(f"Jackan kostar {jacket_price} kr.")
    try:
        discount = input("Hur stor procent är det på rean? Ange procentsats här: ")
        discount = int (discount)
        print(f"Procentsatsen är {discount}%.")
        discount_price = jacket_price * discount / 100
        print(f"Du får rabbatt på {discount_price} kr.")
        final_price = jacket_price-(jacket_price * discount / 100)
        print(f"Då betalar du {final_price} kr nu.")
    except ValueError:
        print(f"{discount} är inte ett heltal.")





