def calc_pennies(digit):
    print(f"{digit} pennie[s],")
    #for x in range(int(digit)):
    #    print(f"plus {x}")

def calc_nickles(digit):
    #print(f"n{digit}")
    differece_nickles = (float(digit) // 5)
    print(f"{differece_nickles} nickles[s],")
    if (float(digit)/ 5) > 1:
        num_pennies = calc_pennies(float(digit) % 5)
    else:
        calc_pennies(float(digit) % 5)
    #    for decimal_place, digit in enumerate(str(differece_nickles).split(".")[0]):
    #        if decimal_place == 0:
    #            num_dimes = calc_pennies(digit)
    #            print(f"{num_dimes}dimes,")

def calc_dimes(digit):
    print(f"{digit} dime[s],")
    #for x in range(int(digit)):
        #print(f"plus")



def calc_quarters(digit):
    #print(f"q{digit}")
    differece_quarter = (float(digit) // 5)

    print(f"{differece_quarter} quarter[s],")
    if (float(digit)/ 5) > 1:
        num_dimes = calc_dimes(float(digit) % 5)
    else:
        calc_dimes(float(digit) % 5)
        #for decimal_place, digit in enumerate(str(differece_quarter).split(".")[0]):
        #    if decimal_place == 0:
        #        num_dimes = calc_dimes(digit)

        #print("1 quarter")
        #return ("1")


def main():
    money_due = float(input("How much do you owe?: "))
    money_given = float(input("How much did you give to the clerk?: "))
    #money_due = float(3.69)
    #money_given = float(10)
    cost_difference = money_given - money_due
    
    print(f"the clerk owes you ${str(cost_difference)[0:4]}")

    for decimal_place, digit in enumerate(str(cost_difference).split(".")[1]):
        if decimal_place == 0:
            quarters_number = calc_quarters(digit)
            #print(quarters_number)
        if decimal_place == 1:
            num_dimes = calc_nickles(digit)
        #print(digit,decimal_place)
        #if decimal_place == 1:

        #print(quarters_number)


if __name__ == "__main__":
    main()