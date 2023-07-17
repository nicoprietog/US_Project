# Introduction
As mentioned in the "About me" section, I had the opportunity to go through various jobs, each very different from the others. They didn't happen in an ascending order implying "improvement" or "career growth". Coincidentally, operating a forklift was my last responsibility, following my experience teaching macroeconomics and international economics at the university.

I ventured to work in other countries, which was a great experience that I cherish with valuable lessons, Well, from every situation, there is some detail to learn.

To operate the forklift, I had to use software installed on a screen inside the vehicle. The program could receive the product, organize it within the warehouse, and remove it from the warehouse when a sale was completed. Most of the time I spent behind the wheel, I listened to podcasts or structured the necessary logic to carry out the process that occurred inside that computer in front of me. Being there, using the program, experiencing the situation firsthand, helped me understand the business needs. Therefore, I hope to meet all of them in the development of my application.

# Development
## 1. Initial File: Location_df
To start the project, I found it logical to begin by structuring the physical space available in my warehouse for storing products. I tried to create the space similar to my experience, where there were around 50 aisles, and each aisle had approximately 20 locations within it.
The idea its to create a Data Frame, where each column represent an aisle, and the rows represent the location inside each asile. The data its a tuple that contains 4 items:
1) The actual quiantity of pallets inside: Initially set to zero as the warehouse starts empty. This number will be updated as spaces are occupied.
2) The max number of pallet allowed inside the location: Will vary according to the aisle, as there will be exclusive aisles for certain types of products.
3) The max height of stacked pallets: The maximum number of accepted pallets in each location will vary according to the aisle, as there will be exclusive aisles for certain types of products.
4) A random code that should be located at the physical position inside the warehouse. The driver should enter this code into the software when placing the pallet in position.

To obtain this DataFrame in my code, I followed the following steps:

1) I generated a list called "column_names" with the names of the aisles from 1 to 50. This will serve as the column names for my DataFrame. I did this through a for loop.
2) I created a list called "list_data" composed of other lists, where each sublist contains the four variables mentioned above. Here, I also defined these variables:
  2.1) The maximum number of pallets will be 20 for aisles 1 to 15, 40 for aisles 16 to 40, and 48 for aisles 41 to 50.
  2.2) Regarding the maximum number of stacked pallets, it will be 2 for aisles 1 to 15 and 41 to 50, and 4 for aisles 16 to 40.
  2.3) A random code that will be created later.
3) I create my DataFrame "initial_locations_df," where I store the information from "list_data" and set the column names using the "column_names" list.
4) I add the additional rows to "initial_locations_df," referring to the locations each aisle will have. In total, each aisle should have a total of 20 locations. I proceed to create "final_locations_df" using the <pd.concat> function and multiplying my initial list by 20.
Finally, I create a function that will add the random code to the last data point of each list within my DataFrame. I obtain this function through Chat GPT.

Having the structure of how the space is distributed in the warehouse and having created the DataFrame with the information, I can move on to the next step, where I interact with the created space by adding and removing products.

## 2. Second File to Create: Orders_df
This file essentially consists of two sequences. The first one involves obtaining information through inputs about the type and quantity of products to enter the warehouse. The second sequence focuses on how this information is stored in another DataFrame.

This DataFrame interacts with the previously created DataFrame in the Location_df file to fill those empty spaces.

Feel free to add more visual arrangements or make any necessary modifications to suit your needs.

