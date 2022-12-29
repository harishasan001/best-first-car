#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

'''
Accessing your dashboard: after running "streamlit run streamlit_app.py", you'll want to access your website!
If your URL looks like this: https://coding.ai-camp.dev/projects/ad938e8d-2c1b-480b-b393-94673d3d4628/files/WC22-Data-Science/.....
Your dashboard will be at: https://coding.ai-camp.dev/ad938e8d-2c1b-480b-b393-94673d3d4628/port/8501
Notice how there is no more "/projects/" and no more "files/...". Make those changes to get your site running!

Instructors: if you are having issues, go to /examples/ and copy the contents of the config.toml file to a new file in the location "~/.streamlit/config.toml"
'''


#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Data Science Example EDA')
st.write('You should add your plots and code to this page, using the code we have as inspiration to get started. I created a sample dataset below using numpy and pandas to show you how to display tables and graphs.')
st.markdown("""---""")
#generate random data for my example dataframe -- howto: https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
df = pd.read_csv("FINAL_SPINNY_900.csv")

#CLEANING
#Removing commas in Price Column
df['Price']=df['Price'].str.replace(',','')

#Converting Price currency from Indian Rupees to US Dollars
df['Price'] = pd.to_numeric(df['Price'])
df.loc[:, 'Price'] *= 0.012

#Converting No. Owners from String description to int
df['No_of_Owners']=df['No_of_Owners'].str.replace('1st', "1")
df['No_of_Owners']=df['No_of_Owners'].str.replace('2nd', "2")
df['No_of_Owners']=df['No_of_Owners'].str.replace('3rd', "3")
df['No_of_Owners'] = pd.to_numeric(df['No_of_Owners'])

df = df.rename(columns = {"Fuel_Tank_Capacity(L)" : "Fuel_Tank_Capacity(G)"})
df.loc[:, 'Fuel_Tank_Capacity(G)'] /= 3.785

df['Mileage(kmpl)'] = df['Mileage(kmpl)'].replace(['BS IV'], 22.299999237060547)
df['Mileage(kmpl)'] = df['Mileage(kmpl)'].replace(['105 bhp @ 4400 RPM'], 20.5)

df["Mileage(kmpl)"] = pd.to_numeric(df["Mileage(kmpl)"])
df.loc[:, "Mileage(kmpl)"] *= 2.35215
df = df.rename(columns={"Mileage(kmpl)": "Mileage(mpg)"})

st.header('Data Cleaning')
st.write('In looking at the data we decided to keep each column but that some columns should be changed as it originates from data from India. The Price was converted from Rupee to USD and Mileage was converted to MPG from KMPL. Within mileage a two types of string values were found and were switched their numerical equivalent before their conversion. Finally, it was decided that switching the number of owners into numbers rather than strings would be better for exploring the data later.')


#show off a bit of your data. 
st.header('The Data')
col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
col1.dataframe(df.head())
col2.markdown("\n") #add a line of empty space.
col2.markdown('This is a webscrapped data from a car resale websites, which include more details of the cars along with its respective prices.') #you can add multiple items to each column.
col2.markdown('- **Link: ** https://www.kaggle.com/datasets/rakkesharv/used-cars-detailed-dataset')
st.markdown("""---""")

st.header('Some Plots')
st.plotly_chart(px.histogram(df, x="Make_Year"))

st.plotly_chart(px.scatter(df, x = "Make_Year", y="Power(BHP)", color = "Make"))
#fig.show()
#In average, in terms of both torque and power the Mahindra and especially Skoda shows continuous growth and improvements
"""
Chevrolet shows much more rapid growth and only appearing in year range of 2013 to 2015 and no more growth
On the other hand, Maruti shows almost no improvements in power(BHP) over the course of make years but they are shown to be recorded each year but currently its starting to go down
from it's peak which was around the year-range 2014 - 2016
Also, the highest power reached in each year was achieved by the Skoda, for 2012, 2014, 2019, and 2022.
Also, as torque and power are both dependant on the engine speed, I expected the torque and power to have an overall linear relationship,
which proved to be correct after creating a scatter plot that uses the x axis as the torque and the y axis as it's power.
Currently, the highest point reached in both torque and power(250 Nm and 177 BHP) was achieved by the Skoda brand.

"""
st.plotly_chart(px.scatter(df, x="Price", y="Make_Year"))
st.markdown("This is an example set of charts I made up. You can put your team's charts here if you want!")
st.markdown("""---""")


st.plotly_chart(px.histogram(df, x="Price", color ="No_of_Owners" ))
st.markdown("All of the cars priced above 17k have only one owner.")


st.plotly_chart(px.histogram(df, x = "Price", color = "Make_Year"))
st.markdown("Most expensive cars have been made within the last 3 years.")



###tophalf stuff (teddy)
top_half = df[df['Price']>8892.233607]
top_total = len(top_half)
#tttop
tt1 = top_half["Transmission_Type"].value_counts()["Manual"]
tt2 = top_half["Transmission_Type"].value_counts()["Automatic"]
tt_arr = np.array([(tt1/top_total), (tt2/top_total)])
tt_labels = ["Manual", "Automatic"]
st.plotly_chart(plt.pie(tt_arr, labels = tt_labels, shadow = True))
#fttop
ft1 = top_half["Fuel_Type"].value_counts()["petrol"]
ft2 = top_half["Fuel_Type"].value_counts()["diesel"]
ft_arr = np.array([(ft1/top_total), (ft2/top_total)])
ft_labels = ["petrol", "diesel"]
st.plotly_chart(plt.pie(ft_arr, labels = ft_labels, shadow = True))
#sctop
top_half["Seating_Capacity"].unique()
sc1 = top_half["Seating_Capacity"].value_counts()[5.0]
sc2 = top_half["Seating_Capacity"].value_counts()[7.0]
sc3 = top_half["Seating_Capacity"].value_counts()[6.0]
st.plotly_chart(plt.pie(sc_arr, labels = sc_labels, shadow = True))




#Always good to section out your code for readability.
st.header('Conclusions')
st.markdown('- **Data Science is Fun!**')
st.markdown('- **The [Streamlit Cheatsheet](https://docs.streamlit.io/library/cheatsheet) is really useful.**')

