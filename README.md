# Introduction
As mentioned in the "About me" section, I had the opportunity to go through various jobs, each very different from the others. They didn't happen in an ascending order implying "improvement" or "career growth". Coincidentally, operating a forklift was my last responsibility, following my experience teaching macroeconomics and international economics at the university.

I didn't take on the forklift job out of necessity or because my situation worsened. I wanted to explore new places and routines. I ventured to work in other countries, which was a great experience that I cherish with valuable lessons and memories that will last a lifetime.

To operate the forklift, I had to use software installed on a screen inside the vehicle. The program could receive the product, organize it within the warehouse, and remove it from the warehouse when a sale was completed. Most of the time I spent behind the wheel, I listened to podcasts or structured the necessary logic to carry out the process that occurred inside that computer in front of me. Being there, using the program, experiencing the situation firsthand, helped me understand the business needs. Therefore, I hope to meet all of them in the development of my application.

# Development
## 1. Initial File: Location_df
To start the project, I found it logical to begin by structuring the physical space available in my warehouse for storing products. Would it have hundreds or thousands of spaces? I tried to create the space similar to my experience, where there were around 50 aisles, and each aisle had approximately 20 locations within it.

These individual locations had their own characteristics, such as the maximum quantity of products they could store, the product category, and the allowed stacked pallet height.

To achieve this, I created a Pandas DataFrame to collect the information. My DataFrame would have 50 columns representing the 50 existing aisles. The rows of the DataFrame would represent the positions of the locations within each aisle. Therefore, my information matrix would have a size of 20x50.

The data included in the DataFrame would be a list of four variables:
- Actual number of pallets in the location: Initially set to zero as the warehouse starts empty. This number will be updated as spaces are occupied.
- Maximum number of pallets: Varies depending on the aisle.
- Allowed height: Represents the maximum number of stacked pallets for safety reasons.
- Confirmation code: A randomly generated alphanumeric code of three letters and three numbers. The operator driver will enter this code into the system to verify that they are placing the pallet in the correct location, helping to prevent product loss.

Having the structure of how the space is distributed in the warehouse and having created the DataFrame with the information, I can move on to the next step, where I interact with the created space by adding and removing products.

## 2. Second File to Create: Orders_df
This file essentially consists of two sequences. The first one involves obtaining information through inputs about the type and quantity of products to enter the warehouse. The second sequence focuses on how this information is stored in another DataFrame.

This DataFrame interacts with the previously created DataFrame in the Location_df file to fill those empty spaces.

Feel free to add more visual arrangements or make any necessary modifications to suit your needs.

