def statement_generator(statement, decor):
    print(f"\n{decor * 5} {statement} {decor * 5} \n")


def instructions():
    statement_generator("Instructions", "-")
    print(f'''
    
    **** Instructions ****
    
    To begin choose a category {valid_categories}
    Type 'xxx' when you want to stop
    Then...
    - Put in the amount that you have
    - State what unit you have
    - Stat what unit you want

    
    The program will do the conversion for you :)
    
''')


def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = float(response)

            if 0 < response:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def unit_check(question, valid_units):
    unit_list = list(valid_units.keys())

    while True:

        # ask the user for a unit
        response = input(question)

        if response in valid_units:
            return response

        else:
            print(f"Sorry, the unit is not valid, please choose from {unit_list}")


def category_check(question, valid_responses):
    error = "Please enter a valid category\n"
    while True:

        response = input(question).lower()

        # Checks response is either in the list or the first letter of a list item
        for item in valid_responses:
            if response == item or response == item[0]:
                return item

        print(error)


# Get amount and units (assume they are valid)
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

time_dict = {
    "ms": 3600000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "days": 0.04166666666,
    "years": 0.00011407711
}

mass_dict = {
    "mg": 1000000,
    "g": 1000,
    "kg": 1,
    "t": 0.001

}

valid_categories = [
    "distance",
    "time",
    "mass", "xxx"
]

statement_generator("Conversion calculator", "-")
want_instructions = input("Press <enter> to read or any key to continue: ")

if want_instructions == "":
    instructions()

while True:
    # input
    category = category_check("Which category? ", valid_categories)

    if category == "xxx":
        break

    print(f"Your category is {category}")
    amount = num_check("How much?")
    # if amount == "xxx":
    #     break

    # set up correct dictionary to be used
    if category == "distance":
        # print(distance_print())
        find_unit = distance_dict

    elif category == "time":
        # print(time_print())
        find_unit = time_dict

    elif category == "mass":
        # print(mass_print())
        find_unit = mass_dict

    # get units and check they are in the same domain
    from_unit = unit_check("From unit? ", find_unit)
    to_unit = unit_check("To unit? ", find_unit)

    # do conversion and show user result
    multiply_by = find_unit[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = find_unit[from_unit]
    answer = standard / divide_by

    print(f"There are {answer:.2f} {to_unit} in {amount} {from_unit} ")

print("Thank you for using the conversion calculator")
