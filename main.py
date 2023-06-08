import pandas as pd
from location_df import final_locations_df as locations
import random

#Generate a copy  of Locations:
locations_copy = locations.copy()
#Change the rows of the locations DF, now it shows the number of spaces in each location:
for i in range(1,51):
    locations_copy[f"aisle {i}"] = locations_copy[f"aisle {i}"].apply(lambda x:x[1]-x[0])
#Open the orders history from the CSV file:
orders = pd.read_csv("Orders_history.csv")
#Rename the ID column with unique data:
orders_rows = list(range(0,orders.shape[0]))
orders["id"] = orders_rows
#Add a new column for checks
orders["check"] = "n"
#Generate a list with the quantitys orders:
orders_quantity = orders["quantity"].tolist()
#Get an array with the type of products:
type_products = list(orders["type"])
print("La lista de tipos es:",type_products) #ESTE LO PUEDO BORRAR LUEGO, NO ES IMPORTANTE


#Def a function to generate an array with the spaces of one random aisle in which the product could be saved:
def gen_random_location(type_products,locations_copy):
    random_aisles_array = []
    locations_array = []
    for i in type_products:
        #Give me the number of aisle where the product can be saved:
        aisles_available = ((list(range(0, 15)) if i == 1 else (list(range(15, 40)) if i == 2 else (list(range(40, 50)) if i == 3 else print("This kind of product do not exist")))))
        #Bring the whole DF segment of the Locations DF:
        locations_for_search = locations_copy.iloc[:,aisles_available]
        #Create a function to give a random number depends the aisle:
        rand_aisle = random.randint(1, 15) if locations_for_search.shape[1] == 15 else (random.randint(15, 40) if locations_for_search.shape[1] == 25 else (random.randint(40, 50) if locations_for_search.shape[1] == 10 else print("error")))
        random_aisles_array.append(rand_aisle)
        #Get a list of the spaces in the random aisle where the product can be saved:
        list_location = locations_for_search[f"aisle {rand_aisle}"].tolist()
        locations_array.append(list_location)
    print("random aisles: ", random_aisles_array)
    print(locations_array)


gen_random_location(type_products,locations_copy)



 


