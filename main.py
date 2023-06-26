import pandas as pd
from location_df import final_locations_df as locations
import random
import functools


# Generate a copy  of Locations:
locations_copy = locations.copy()

# Open the orders history from the CSV file:
orders = pd.read_csv("Orders_history.csv")
# Open the changes history from the CSV file:
changes = pd.read_csv("changes_history.csv")

# Rename the ID column with unique data:
orders_rows = list(range(0, orders.shape[0]))
orders["id"] = orders_rows

# Add a new column for checks
orders["check"] = "n"

# Get an array with the type of products:
type_products = list(orders["type"])

# Generate a list with the quantities of orders:
orders_copy = orders.copy()
orders_quantity = orders_copy["quantity"].tolist()


# Def a function to generate an array with two variables: a random location, and a random aisle. Those depends of the type of product to be storaged:
def gen_random_location(type_products, locations_copy):
    random_locations = []
    for i in type_products:
        # Give me the number of aisle where the product can be saved:
        aisles_available = ((list(range(0, 15)) if i == 1 else (list(range(15, 40)) if i == 2 else (list(range(40, 50)) if i == 3 else print("This kind of product do not exist")))))
        # Bring the whole DF segment of the Locations DF:
        locations_for_search = locations_copy.iloc[:, aisles_available]
        # Create a function to give a random number depends the aisle (the determinate number is because each type of product have a space of X aisles to be allocated):
        rand_aisle = random.randint(1, 15) if locations_for_search.shape[1] == 15 else (random.randint(15, 40) if locations_for_search.shape[1] == 25 else (random.randint(40, 50) if locations_for_search.shape[1] == 10 else print("error")))
        rand_pos = random.randint(0, 19)
        rand_location = (rand_pos, rand_aisle)
        random_locations.append(rand_location)
    return random_locations

#This is a function that brings the free spaces in the random previous locations generated:
def gen_free_spaces(random_locations):
    spaces = []
    for i in random_locations:
        # Here I take the coordinates of each random location, I divided by rows and columns:
        row = i[0]
        col = i[1]
        # Find the total amount of free spaces at the random location (second number minus the first):
        available_spaces = locations_copy.at[row, f"aisle{col}"][1] - locations_copy.at[row, f"aisle{col}"][0]
        spaces.append(available_spaces)
    return(spaces)
def gen_sum_spaces(orders_quantity):
    sum_spaces = functools.reduce(lambda x, y: x + y, orders_quantity)
    return sum_spaces

# Call the functions:
def call_functions():
    random_locations = gen_random_location(type_products, locations_copy)
    spaces = gen_free_spaces(random_locations)
    sum_spaces = gen_sum_spaces(orders_quantity)
    return random_locations, spaces, sum_spaces

#Call function:
random_locations, spaces, sum_spaces = call_functions()

"""
#esto es una prueba:
print("antes",orders_quantity)
print("antes",sum_spaces)
orders_quantity[0] = 0
sum_spaces = gen_sum_spaces(orders_quantity)
print("despues",orders_quantity)
print("despues",sum_spaces)
"""


#create a DF where every changes will be added:
changes_to_location = pd.DataFrame(columns = ["location","aisle","changes"])
#while sum_spaces > 0:
mix_spaces = list(zip(orders_quantity, spaces, random_locations))
#Here I create an count that will be increase one by one to know which iterable number im in:
count = 0
for i in mix_spaces:
    #Here i can check if there are spaces available into the location:
    if i[1] > 0:
        #Here i check if the number of pallets to be allocated its grater than the number of available spaces:
        if i[0] > i[1]:
            random_code = locations_copy.at[i[2][0],f"aisle{i[2][1]}"][3]
            print(f"Please go to location {i[2][0]} in aisle {i[2][1]} to allocate " )
            # This next line of code its really dont necesary becouse in real life the driver need to go to the location and see the code with his own eyes just to confirm he´s doing things right:
            print("The random code is: ",random_code)
            #Ask the code to the driver:
            random_answer_code = input("Please enter the confirmation code of given location:")
            if random_code == random_answer_code:
                #change the main DF to enter de product into the spaces, turn the actual number of pallets into the max allowed:
                locations_copy.at[i[2][0],f"aisle{i[2][1]}"][0] = locations_copy.at[i[2][0],f"aisle{i[2][1]}"][1]
                #Now here the orders quantity decrease in to the number of
                orders_quantity[count] = i[0]-i[1]
                count += 1
                #Running again the function to know the spaces
                sum_spaces = gen_sum_spaces(orders_quantity)
                #Make a resum to show to the driver:
                print(f"You just allocated {i[1]} pallets")
                continue_allocation = input("Press [1] to continue, [2] for stop.")
                # Now I need to append to my DF the changes that i did:
                changes_append = {"location": i[2][0], "aisle": i[2][1], "changes": i[1]}
                changes_to_location = changes_to_location._append(changes_append, ignore_index=True)
                #Ask if the driver wants to continue moving pallets:
                if continue_allocation == 1:
                    continue
                else:
                    break
            else:
                print("The code you provide is not the correct")
    else:
        print("ahi vamos")

#Add the changes to a csv file:
print(changes_to_location)


#Save the history of orders in a new file:
changes_to_location.to_csv("changes_history.csv",mode ="a", header = False , index=False)




