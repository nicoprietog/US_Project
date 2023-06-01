import pandas as pd
import random
import string

#Generate columns names:
aisle_num = 50
columns_names = ['Aisle ' + str(i) for i in range(1,aisle_num+1)]

# Generate data for the lists:
list_data = []
for i in range(1, aisle_num + 1):
    #Actual number of pallets:
    actual_number_pallets = 0
    #Max number of pallets in a location, depends the aisle:
    max_pallets = (20 if i <= 15 else (40 if i > 15 and i <= 40 else 48))
    #Max number of pallets stacked, depends of the aisle:
    max_height = (2 if i <= 15 else (4 if i > 15 and i <= 40 else 2))
    #Random code:
    random_confirmation_code = 0
    #Create a list with the last 4 data:
    list_data.append([actual_number_pallets,max_pallets,max_height,random_confirmation_code])
# Create de DataFrame from the tuple_data:
initial_locations_df = pd.DataFrame([list_data], columns=columns_names)
#Add the extra locations per aisle:
num_of_locations_per_aisle = 20
final_locations_df = pd.concat([initial_locations_df] * (num_of_locations_per_aisle), ignore_index=True)

#Create a function to give a random code to every location available:
def random_code(lst):
    #Create the random letters and numbers, then shuffle them:
    random_letters = random.sample(string.ascii_letters, 3)
    random_numbers = [random.randint(0, 9) for _ in range(3)]
    random_code = random_numbers + random_letters
    random.shuffle(random_code)
    random_confirmation_code = ''.join(str(elem) for elem in random_code)
    return lst[:-1] + [random_confirmation_code]

#Apply the function to every
final_locations_df = final_locations_df.applymap(lambda x: random_code(x))
print(final_locations_df)
