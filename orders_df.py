import pandas as pd
import datetime

# Here comes the dictionary that will became de Data Frame with all the orders information:
orders_dict = {
    "id": [],
    "date": [],
    "name": [],
    "product": [],
    "quantity": []}
#This will be the DataFrame that save all orders in time:
orders_df_history = pd.DataFrame(columns=["id", "date", "name", "product", "quantity"])

#Function to ask information to the user:
def info():
    print("Welcome,to continue with your order, notice our available products:")
    print("Espresso, Cappuccino, Latte, Americano, Macchiato, Mocha, Flat White, Affogato, Irish Coffee, Frappuccino")
    num_products = int(input("How many diferent products you want to order? (Max 10): "))
    # Number of iterations:
    iterations_num = range(0, num_products)
    #Name who order and dictionary:
    name_order = input("Please provide yor name: ")
    name_dict = [name_order for i in iterations_num]
    #Dictionary of ordered products:
    products_ordered_dict = [input(f"Product {i+1}: ") for i in iterations_num]
    #Quantity of products:
    quantity_ordered_dict = [int(input(f"Quantity of Product {i+1}: ")) for i in iterations_num]
    #Create id dictionary:
    id_dict = [i + 1 for i in iterations_num]
    #Create date dictionary:
    date_today = datetime.date.today()
    formatted_date = date_today.strftime("%m-%d-%Y")
    date_dict = [formatted_date for i in iterations_num]
    return name_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict

def save(name_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict,orders_dict,orders_df_history):
    #Append the dicts to the main dict:
    orders_dict["id"] = id_dict
    orders_dict["date"] = date_dict
    orders_dict["name"] = name_dict
    orders_dict["product"] = products_ordered_dict
    orders_dict["quantity"] = quantity_ordered_dict
    #Create de DataFrame from the main dict:
    orders_df = pd.DataFrame(orders_dict)
    #Make a little resume:
    len_iterations = len(products_ordered_dict)
    quantity_sum = sum(quantity_ordered_dict)
    print(f"In summary, the user has ordered {len_iterations} products, for a total of {quantity_sum} different products.")
    return orders_df

#Call the functions one by one:
name_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict = info()
orders_df = save(name_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict,orders_dict,orders_df_history)
#Concatenate the actual order to the history of orders:
orders_df_history = pd.concat([orders_df_history,orders_df],ignore_index=True)
print("Your order looks like this so far:  ")
print(orders_df)

more_orders_state = True
while more_orders_state:
    more_orders = int(input("Press [1] if you want to make another order, to continue without any order press [2]"))
    if more_orders == 1:
        # Call the functions one by one:
        name_dict, products_ordered_dict, quantity_ordered_dict, id_dict, date_dict = info()
        orders_df = save(name_dict, products_ordered_dict, quantity_ordered_dict, id_dict, date_dict, orders_dict, orders_df_history)
        # Concatenate the actual order to the history of orders:
        orders_df_history = pd.concat([orders_df_history, orders_df], ignore_index=True)
        print("Your order looks like this so far: ")
        print(orders_df_history)
        continue_process = input("You want to place another order? [1]:Yes [2]:No :" )
        if  continue_process == 2:
            more_orders_state = False
    elif more_orders == 2:
        print("Thanks for your order, your products will arrive soon to the Wharehouse. ")
        more_orders_state = False