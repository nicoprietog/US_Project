import pandas as pd
import datetime

# Here comes the dictionary that will became de Data Frame with all the orders information:
orders_dict = {
    "id": [],
    "date": [],
    "name": [],
    "last_name": [],
    "email": [],
    "city": [],
    "Company_type": [],
    "kind": [],
    "type": [],
    "product": [],
    "quantity": []}

#This will be the DataFrame that save all orders in time:
orders_df_history = pd.DataFrame(columns=["id","date""name","last_name","email","city","kind","type","product","quantity","Company_type"])

#Here i´ll ask what´s the personal user information is:
print("To continue, please provide your personal information.")
date_today = datetime.date.today()
name_order = input("Please provide your name: ")
last_name = input("Please enter your last name: ")
id = input("Please provide your Id: ")
email = input("please enter your email: ")
city = input("Please provide your location City")
company_type = input("Please enter the type of company you work for. If you don't belong to any company, enter the word -Self-. ")




#Here I´ll ask information about what the user needs:
active_purchase = True
while active_purchase:
    #Here I ask the information about the product:
    kind_product = int(input("Please insert the code number  corresponding to the type of product you wish to purchase.: Coffee Makers[1], Coffee Pots[2], spare parts[3]"))
    print(("The available products in the store are: "),("Drip Coffee Maker[1], Espresso Machine[2], French Press[3], Single Serve Coffee Maker[4], Pour Over Coffee Maker[5]") if type_product == 1 else (("Espresso[1], Cappuccino[2], Latte[3], Americano[4], Macchiato[5], Mocha[6], Flat White[7], Affogato[8], Irish Coffee[9]") if type_product == 2 else ("Filter Basket[1], Water Tank[2], Portafilter[3], Grinder Burrs[4]")))
    type_product = int(input("Please select the code number corresponding the type of product you want to buy: "))
    q_product = int(input("How many units do you need?" ))



    #Save the actual order into the DF:
    orders_dict["id"].append(id)
    orders_dict["date"].append(date_today)
    orders_dict["name"].append(name_order)
    orders_dict["last_name"].append(last_name)
    orders_dict["email"].append(email)
    orders_dict["city"].append(city)
    orders_dict["kind"].append(kind_product)
    orders_dict["type"].append(type_product)
    orders_dict["product"] =
    orders_dict["quantity"] =







    status_order = input("You want to place another order?: Yes[1] No[2]")
    if status_order == 1:
        continue
    elif status_order == 2:
        active_purchase = False






#Here are gonna be saved the answers of the user:
    orders_dict["id"] = id_dict
    orders_dict["date"] = date_dict
    orders_dict["name"] = name_dict
    orders_dict["last_name"] = last_name_dict
    orders_dict["email"] = email_dict
    orders_dict["city"] = city_dict
    orders_dict["type"] = type_dict
    orders_dict["product"] = products_ordered_dict
    orders_dict["quantity"] = quantity_ordered_dict




def info():
    print("Welcome,to continue please enter your information:")
    #This shows the different type of product in the warehouse:
    type_product = int(input("Select the number: Coffee Makers[1], Coffee Pots[2], spare parts[3]"))
    print(("The available products are: "),("Drip Coffee Maker[1], Espresso Machine[2], French Press[3], Single Serve Coffee Maker[4], Pour Over Coffee Maker[5]") if type_product == 1 else (("Espresso[1], Cappuccino[2], Latte[3], Americano[4], Macchiato[5], Mocha[6], Flat White[7], Affogato[8], Irish Coffee[9]") if type_product == 2 else ("Filter Basket[1], Water Tank[2], Portafilter[3], Grinder Burrs[4]")))
    num_products = int(input("How many diferent products you want to order?: "))
    # Number of iterations:
    iterations_num = range(0, num_products)
    #Name who order and dictionary:
    name_order = input("Please provide yor name: ")
    name_dict = [name_order for i in iterations_num]
    #Dictionary for type:
    type_dict = [type_product for i in iterations_num]
    #Dictionary of ordered products:
    products_ordered_dict = [input(f"Product {i+1}: ") for i in iterations_num]
    #Dicttionary of Quantity of products:
    quantity_ordered_dict = [int(input(f"Quantity of Product {i+1}: ")) for i in iterations_num]
    #Create id dictionary:
    id_dict = 0
    #Create date dictionary:
    date_today = datetime.date.today()
    formatted_date = date_today.strftime("%m-%d-%Y")
    date_dict = [formatted_date for i in iterations_num]
    return name_dict,type_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict

def save(name_dict,type_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict,orders_dict,orders_df_history):
    #Append the dicts to the main dict:
    orders_dict["id"] = id_dict
    orders_dict["date"] = date_dict
    orders_dict["type"] = type_dict
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
name_dict,type_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict = info()
orders_df = save(name_dict,type_dict,products_ordered_dict,quantity_ordered_dict,id_dict,date_dict,orders_dict,orders_df_history)
#Concatenate the actual order to the history of orders:
orders_df_history = pd.concat([orders_df_history,orders_df],ignore_index=True)
print("Your order looks like this so far:  ")
print(orders_df)

more_orders_state = True
while more_orders_state:
    more_orders = int(input("Press [1] if you want to make another order, to continue without any order press [2]"))
    if more_orders == 1:
        # Call the functions one by one:
        name_dict,type_dict,products_ordered_dict, quantity_ordered_dict, id_dict, date_dict = info()
        orders_df = save(name_dict,type_dict ,products_ordered_dict, quantity_ordered_dict, id_dict, date_dict, orders_dict, orders_df_history)
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


#Save the history of orders in a new file:
orders_df_history.to_csv("Orders_history.csv",mode ="a", header = False , index=False)
