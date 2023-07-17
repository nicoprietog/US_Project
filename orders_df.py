import pandas as pd
import datetime
import pymysql
from sqlalchemy import create_engine

# Here comes the dictionary that will became de Data Frame with all the orders information:
orders_dict = {
    "id_buyer": [],
    "date": [],
    "name": [],
    "last_name": [],
    "email": [],
    "city": [],
    "company_type": [],
    "kind": [],
    "type": [],
    "quantity": []}

#This will be the DataFrame that save all orders in time:
orders_df = pd.DataFrame(columns=["id_buyer","date","name","last_name","email","city","company_type","kind","type","quantity"])

#Here i´ll ask what´s the personal user information is:
print("To continue, please provide your personal information next:")
date_today = datetime.date.today()
name_order = input("Please provide your name: ")
last_name = input("Please enter your last name: ")
id_buyer = input("Please provide your Id: ")
email = input("please enter your email: ")
city = input("Please provide your location City")
company_type = input("Please enter the type of company you work for. If you don't belong to any company, enter the word -Self-. ")


#Here I´ll ask information about what the user needs:
active_purchase = True
while active_purchase:
    #Here I ask the information about the product:
    kind_product = int(input("Please insert the code number  corresponding to the type of product you wish to purchase.: Coffee Makers[1], Coffee Pots[2], spare parts[3]"))
    print(("The available products in the store are: "),("Drip Coffee Maker[1], Espresso Machine[2], French Press[3], Single Serve Coffee Maker[4], Pour Over Coffee Maker[5]") if kind_product == 1 else (("Espresso[1], Cappuccino[2], Latte[3], Americano[4], Macchiato[5], Mocha[6], Flat White[7], Affogato[8], Irish Coffee[9]") if kind_product == 2 else ("Filter Basket[1], Water Tank[2], Portafilter[3], Grinder Burrs[4]")))
    type_product = int(input("Please select the code number corresponding the type of product you want to order: "))
    q_product = int(input("How many units do you need?" ))

    #Save the actual order into the DF:
    new_row = { "id_buyer": id_buyer,
                "date": date_today,
                "name": name_order,
                "last_name": last_name,
                "email": email,
                "city": city,
                "company_type": company_type,
                "kind": kind_product,
                "type": type_product,
                "quantity": q_product}

    #Make this new row a DF:
    new_row_df = pd.DataFrame([new_row])

    #Concat both df´s:
    orders_df = pd.concat([orders_df,new_row_df])

    #Ask if the user need another order:
    status_order = int(input("You want to place another order?: Yes[1] No[2]"))
    if status_order == 1:
        continue
    elif status_order == 2:
        active_purchase = False

#Create the variables to conect to SQl:
db_user = "root"
db_password = "Nicoroller123*"
db_host = "127.0.0.1"
db_port = "3306"
db_name = "us_project"
table_name = "orders"

#Conect with Mysql table:
conn = pymysql.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=int(db_port),
    database=db_name)

#Create te engine:
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

#Give the orders_df to my table in SQL:
orders_df.to_sql(table_name, engine, if_exists="append", index=False)

#Close conection:
conn.close()




