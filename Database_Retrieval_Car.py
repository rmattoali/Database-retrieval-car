# Richard Mattoali


# Used to search matching ID based on user input using def.
def search_car_by_id(car_id):
    for car in cars_data:
        if car[0] == car_id:
            return [car]


# Used to search matching name either full or partial based on user input using def.
def search_car_by_name(car_name):
    matching_cars = [car for car in cars_data if car_name.lower() in car[1].lower()]
    return matching_cars


# Used to filter car using def
def filter_cars(cars, min_price=None, max_price=None, min_year=None, max_year=None, fuel_type=None):
    return [
        car for car in cars
        if (min_price is None or car[3] >= min_price)
        and (max_price is None or car[3] <= max_price)
        and (min_year is None or car[2] >= min_year)
        and (max_year is None or car[2] <= max_year)
        and (fuel_type is None or fuel_type.lower() == "n/a" or car[4].lower() == fuel_type.lower())
    ]


# Used to display car information based on user input using def.
def display_car_info(car_info, sep_line=20):
    if car_info:
        print("\nMatching Car(s) Found!\n")
        for car in car_info:
            id_index = fields.index("ID")
            name_index = fields.index("Name")
            year_index = fields.index("Year")
            price_index = fields.index("Price")
            fuel_index = fields.index("Fuel Type")

            print(f"Item ID: {car[id_index]}")
            print(f"Model Name: {car[name_index]}")
            print(f"Year Released: {car[year_index]}")
            print(f"Price: ${car[price_index]}")
            print(f"Fuel Type: {car[fuel_index]}")
            print("-" * sep_line)
    else:
        print("No Car Found!")


# Used to create table format for 'show_all_main()' for better readability
def table_format(f_fields, f_cars_data, spacing=25, sep="", sep_line="-"):
    # Adjust header using .join() function
    header = sep.join([f"{field:<{spacing}}" for field in f_fields])
    # Create a line separator by utilizing len function to dynamically adjust the length
    line_separator = sep_line * len(header)
    # Adjust rows
    formatted_data = f"{header}\n{line_separator}\n"
    for car_data in f_cars_data:
        formatted_data += sep.join([f"{c_data:<{spacing}}" for c_data in car_data]) + "\n"
    print(formatted_data)


# Used to verify correct input on filter_main() function using def
def get_valid_input(prompt, data_type=int):
    while True:
        user_input = input(prompt)
        try:
            if user_input.lower() == "n/a":
                return None
            return data_type(user_input)
        except ValueError:
            print("Invalid Input. Please Enter a Valid Value.")


# Prompt the user to repeat the process or return to main menu using def
def repeat_process(function):
    while True:
        try:
            repeat = input("Do You Want to Repeat the Process? (Y/N): ").lower()
            # Input 'Y' will repeat the process
            if repeat == 'y':
                function()
            # Input 'N' will break the loop and return to main menu
            elif repeat == 'n':
                print("Returning to Main Menu...\n")
                break
            else:
                print("Invalid Input. Please Enter Either 'Y' or 'N'.")
        except ValueError:
            print("Invalid Input, Please Try Again.\n")


# Main search function using def
def search_main():
    while True:
        try:
            # User input attribute ('ID' or 'Name') and value for search.
            # .lower() ensure that user input is not case-sensitive
            search_attribute = input("Enter search attribute (ID or Name): ").lower()
            if search_attribute == "id":
                search_value = int(input("Enter ID (1-20): "))
                car_info = search_car_by_id(search_value)
                # Exit the loop if valid input is provided.
                break
            elif search_attribute == "name":
                search_value = input("Enter Name: ")
                car_info = search_car_by_name(search_value)
                # Exit the loop if valid input is provided.
                break
            else:
                print("Please Enter Either 'ID' or 'Name'.")
        except ValueError:
            print("Invalid Input, Please Try Again.\n")

    # Call the display_car_info() function
    display_car_info(car_info)


# Main filter function using def
def filter_main():
    while True:
        # Take user input for filter criteria
        print("Please Type Your Preferences (Type 'n/a' If Not Applicable): ")
        min_price = get_valid_input("Enter minimum price: ")
        max_price = get_valid_input("Enter maximum price: ")

        min_year = get_valid_input("Enter minimum year: ")
        max_year = get_valid_input("Enter maximum year: ")

        fuel_type = input("Enter fuel type (Gasoline/Diesel/Hybrid/Electric): ")

        if (
            min_price is not None
            or max_price is not None
            or min_year is not None
            or max_year is not None
            or fuel_type is not None
        ):
            filtered_cars = filter_cars(cars_data, min_price, max_price, min_year, max_year, fuel_type)

            # Display filtered car information
            if filtered_cars:
                display_car_info(filtered_cars)
            else:
                print("No Cars Match the Specified Preferences.")
            break



# Main show all catalogue function using def
def show_all_main():
    print("Showing All Catalogue. . .")
    table_format(fields, cars_data)


# Define the custom fields for the data
fields = ["ID", "Name", "Year", "Price", "Fuel Type"]
# Random generated data.
cars_data = [
    [1, 'Toyota Camry', 2022, 25000, 'Gasoline'],
    [2, 'Honda Civic', 2021, 22000, 'Gasoline'],
    [3, 'Ford Mustang', 2023, 35000, 'Gasoline'],
    [4, 'Chevrolet Silverado', 2022, 40000, 'Hybrid'],
    [5, 'Tesla Model 3', 2022, 45000, 'Electric'],
    [6, 'Nissan Altima', 2022, 24000, 'Gasoline'],
    [7, 'BMW 3 Series', 2023, 40000, 'Hybrid'],
    [8, 'Audi A4', 2022, 38000, 'Diesel'],
    [9, 'Hyundai Sonata', 2021, 23000, 'Gasoline'],
    [10, 'Volkswagen Passat', 2022, 26000, 'Diesel'],
    [11, 'Kia Niro', 2023, 32000, 'Hybrid'],
    [12, 'Mazda MX-5 Miata', 2022, 28000, 'Gasoline'],
    [13, 'Ford Escape', 2021, 28000, 'Hybrid'],
    [14, 'Chevrolet Bolt EV', 2023, 38000, 'Electric'],
    [15, 'Mercedes-Benz E-Class', 2022, 52000, 'Diesel'],
    [16, 'Subaru Outback', 2022, 32000, 'Gasoline'],
    [17, 'Lexus RX', 2023, 48000, 'Hybrid'],
    [18, 'Jaguar I-PACE', 2022, 67000, 'Electric'],
    [19, 'Acura MDX', 2021, 45000, 'Diesel'],
    [20, 'Porsche Taycan', 2023, 95000, 'Electric']
]


# Main Process
print("Welcome to Richard's Car Database!")
while True:
    # Prompt the User to input '1', '2', '3', or '4'.
    menu_input = input(
        "MAIN MENU"
        "\nWhat Would You Like to Do (1/2/3/4)?"
        "\n1. Search Specific Car Model "
        "\n2. Find Recommendation "
        "\n3. Show All Catalogue "
        "\n4. Exit \n"
    )
    # Using 'if' to call specific function based on user input.
    if menu_input == "1":
        search_main()
        repeat_process(search_main)
    elif menu_input == "2":
        filter_main()
        repeat_process(filter_main)
    elif menu_input == "3":
        show_all_main()
        repeat_process(show_all_main)
    elif menu_input == "4":
        print("Exiting Program...")
        break
    # Give notice if user input anything other than '1', '2', '3', or '4'.
    else:
        print("Invalid input. Please Enter Ether '1', '2', '3', or '4'.")
