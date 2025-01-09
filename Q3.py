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










