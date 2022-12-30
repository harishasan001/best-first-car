# EDA Final Plan

This is where we will be documenting what our plan is and what we have done as we do it.

(This is an example of a markdown file which is something you'll see alot in the Data Science world! Here is more info if you want to look at it: https://docs.fileformat.com/word-processing/md/#:~:text=MARKDOWN%20file%20extension.,with%20a%20program%20called%20Markdown.)

Our dataset: https://www.kaggle.com/datasets/rakkesharv/used-cars-detailed-dataset

### 1. Understanding the data

**Car_Name:** The full name of the car which is displayed in the ad\
**Make:** Maker of the Car\
**Model :** Model of the Car\
**Make Year:** Year of Manufacturing\
**Color :** Color of the Car\
**Body Type :** Body type of the car\
**Mileage Run:** Total KMs the car run\
**No of Owners:** Number of Previous Owners\
**Seating Capacity:** Total Seating Capacity Available\
**Fuel Type:** Fuel Type used by the car\
**Fuel Tank Capacity(L) :** Total Fuel Capacity of the car\
**Engine Type :** Engine Name, Model and Type\
**CC Displacement:** Total Cubic Displacement (Way to measure the size of the engine)\
**Transmission :** Transmission of power from the engine to the wheels, amount of speeds\
**Transmission Type:** Type of Transmission (Either manual or automatic, could we make this a boolean?)\
**Power(BHP) :** Total Max Power\
**Torque(Nm) :** Total Max Torque\
**Mileage(kmpl) :** Average Mileage of the Car\
**Emission:** Emission Norms of the Car\
**Price:** Selling Price (USD)

### 2. Cleaning Data

Converted Price column to USD And removed commas - Haris

##### Goals:

[x]Convert num owners from string to numerical val  
[ ]Convert transmission type and fuel type from string to boolean \(if there's only 2 types\)

  + there are 3 types of fuel, only two types of transmission!

[x]Convert mileage to mpg

[x]Convert fuel tank capacity to gallons

+ kmpl to mpg is about *= 2.352

### 3. Overall Goals

How can we assess the price of a used car?\
What affects it?\
What affects it most?\
What kind of characteristics do used cars tend to have?\
How do they differ by price?
What characteristics do the top half of cars have? - Teddy\
What are the main differences between Makes?

### 4. Planning Visualizations and Analysis

Use scatter plot to figure out relationships\
histograms between appropriate relationships - odin\
pie plots for make

Final inclusions:\
pie charts\
histograms

### 5. Insights found

 Mean price range: 5000 - 5999 - 120 cars in that range

###### Analysis on relationship between Power & Torque





1. Chevrolet shows much more rapid growth but only appears in year range of 2013 to 2015 and 2022\

2. On the other hand, Maruti shows almost no improvements in power(BHP) over the course of make years but they are shown to be recorded each year and currently its starting to go down from it's peak which was around the year-range 2014 - 2016\

3. The highest power & torque reached in a year was achieved by the Skoda, for 2012, 2014, 2019, and 2022\

4. Currently, the highest point reached in both torque and power(250 Nm and 177 BHP) was achieved by the Skoda brand\

5. Torque and power are both dependant on the engine speed and are indicators, thus creating a linear relationship(more linear at the start of the making years compared to the end)\

##### For used cars with an above average price:

1. They mostly have only one previous owner\
  1b. They also sometimes have two previous owners
2. They tend to have a manual transmission\
  2b. It is not uncommon for them to have an automatic transmission
3. They tend to run on petrol as opposed to diesel\
  3b. It is not uncommon for them to run on diesel
4. They overwhelmingly have a seating capacity of 5\
  4b. They also occasionally have a seating capacity of 7
  





  /

    A used car with only one previous owner, a manual transmission, which runs on petrol, and has a seating capacity of 5 would be the most expensive. 
    If a shopper's needs can be met without these attributes, they should  be avoided to keep costs down
    



[COMMENT]: <> 'to check boxes, add x withing "[ ]" or just click in right column'
