import pandas as pd

#Generate columns names:
aisle_num = 50
columns_names = ['Aisle ' + str(i) for i in range(1,aisle_num+1)]
# Generate data for tuples:
tuple_data = []
for i in range(1, aisle_num + 1):
    #Max boxes in a tower, depends the aisle:
    a = (20 if i <= 15 else (40 if i > 15 and i <= 40 else 48))
    #Max height of boxes one over the other, also depends of the aisle:
    b = (2 if i <= 15 else (4 if i > 15 and i <= 40 else 2))
    #Create a tuple with the last two data, and the cero thats works as the actual number of boxes (everything its empty):
    tuple_data.append((0,a,b))
# Create de DataFrame from the tuple_data:
initial_locations_df = pd.DataFrame([tuple_data], columns=columns_names)
#Add the extra locations per aisle:
num_of_locations_per_aisle = 20
final_locations_df = pd.concat([initial_locations_df] * (num_of_locations_per_aisle), ignore_index=True)
print(final_locations_df)
