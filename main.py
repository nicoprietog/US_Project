import pandas as pd
from location_df import final_locations_df as locations
import random

# Generate a copy  of Locations:
locations_copy = locations.copy()

# Open the orders history from the CSV file:
orders = pd.read_csv("Orders_history.csv")

# Rename the ID column with unique data:
orders_rows = list(range(0, orders.shape[0]))
orders["id"] = orders_rows

# Add a new column for checks
orders["check"] = "n"

# Get an array with the type of products:
type_products = list(orders["type"])


# Def a function to generate an array with two variables: a random location, and a random aisle. Those depends of the type of product to be storaged:
def gen_random_location(type_products, locations_copy):
    random_locations = []
    for i in type_products:
        # Give me the number of aisle where the product can be saved:
        aisles_available = ((list(range(0, 15)) if i == 1 else (list(range(15, 40)) if i == 2 else (
            list(range(40, 50)) if i == 3 else print("This kind of product do not exist")))))
        # Bring the whole DF segment of the Locations DF:
        locations_for_search = locations_copy.iloc[:, aisles_available]
        # Create a function to give a random number depends the aisle (the determinate number is because each type of product have a space of X aisles to be allocated):
        rand_aisle = random.randint(1, 15) if locations_for_search.shape[1] == 15 else (
            random.randint(15, 40) if locations_for_search.shape[1] == 25 else (
                random.randint(40, 50) if locations_for_search.shape[1] == 10 else print("error")))
        rand_pos = random.randint(0, 19)
        rand_location = (rand_pos, rand_aisle)
        random_locations.append(rand_location)
    return random_locations


# Call the function to generate random coordinates:
random_locations = gen_random_location(type_products, locations_copy)

# Generate a list with the quantities of orders:
orders_quantity = orders["quantity"].tolist()

print(random_locations)

for i in random_locations:

    row = random_locations[i][0]
    col = random_locations[i][1]
    available_spaces_location = locations_copy.at[row, f"aisle{col}"][1] - locations_copy.at[row, f"aisle{col}"][0]
    pallets_to_allocate = orders_quantity[i]
    if available_spaces_location > 0:
        if pallets_to_allocate > available_spaces_location:
            pallets_to_allocate -= available_spaces_location
            available_spaces_location == 0

        random_locations = gen_random_location(type_products, locations_copy)
    else pallets_to_allocate == 0:
        break

    # if orders_quantity[i]:

    print(available_spaces_location)

# x = locations_copy.at[2,"aisle3"][3]
# print(x)

"""







 


