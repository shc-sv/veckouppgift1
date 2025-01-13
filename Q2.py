# Vecouppgift 1
# Q2: I fixed the errors with adding a plus and converting numbers to string

def left_money():
    ticket_price = 100  # biljettpris
    money_I_have = 200  # pengar på fickan
    print("Det blir " + str(money_I_have - ticket_price) + " kronor över.")

    half_of_money_left = (money_I_have - ticket_price) / 2
    print("Jag tror att det saknas parenteser i denna rad: z = 200 - 100 / 2. Därför ändrar jag koden till: z = (200 - 100) / 2.")
    print("Hälften av pengar som är kvar är: " + str(half_of_money_left))

# Bra variabelnamn:
# - uttrycksfulla (beskriver vad de är till för)
# - inga förkortning
# - lagom långa
# - använd engelska konsekvent


