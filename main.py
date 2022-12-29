#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# Accessing your dashboard: after running "streamlit run streamlit_app.py", you'll want to access your website!
# If your URL looks like this: https://coding.ai-camp.dev/projects/ad938e8d-2c1b-480b-b393-94673d3d4628/files/WC22-Data-Science/.....
# Your dashboard will be at: https://coding.ai-camp.dev/ad938e8d-2c1b-480b-b393-94673d3d4628/port/8501
# Notice how there is no more "/projects/" and no more "files/...". Make those changes to get your site running!

# Instructors: if you are having issues, go to /examples/ and copy the contents of the config.toml file to a new file in the location "~/.streamlit/config.toml"



#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Used Cars EDA')
st.subheader('Team Creative Coders')
container_2 = st.empty()
button_A = container_2.button('View the Team')
if button_A:
    container_2.empty()
    button_B = container_2.button('Close')
    st.markdown("""
    Alexandra Ivanova: Grade 11, extremely minimal experience with Python but experienced with JAVA
    \nJayson Kim: Grade 10, No experience with Python but with other languages instead(C++)
    \nOdin Hill: Grade 9, No experience with Python, minimal experience with JavaScript
    \nSpencer Gilleran: Grade 11, No experience with Python, but has used other languages(C#/JAVA)
    \nTeddy Schwartz: Grade 10, minimal experience with Python and but experience in Javascript
    \nHaris Hasan: Data Science Instructor, Junior at Purdue University studying CS and Statistics 
    """)

st.markdown("""---""")

df = pd.read_csv("car_data.csv")

st.header("Context")
st.subheader("The Goal")
st.write("We were looking to see what factors influenced the price of used cars the most, and how those factors influence the price, specifically examining power and torque.")
st.subheader("Why is this dataset important?")
st.write("Getting insights about used car prices is important because used cars tend to be the only option for many people's transportation. Particularly, as students, our first cars will likely be used cars, so knowing about how factors affect the price of used cars can help us get the best value possible.")

st.markdown("""---""")

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

st.header('Data Selection and Cleaning')
st.write('[Our dataset](https://www.kaggle.com/datasets/rakkesharv/used-cars-detailed-dataset) aggregates data from a car resale website and includes car specifications and prices')
st.write('This is how we cleaned our data:')
st.markdown(
"""
- The values in the Price column were converted from Indian Rupee to USD
- Mileage was converted to MPG from KMPL.
    - In Mileage "BS IV" was changed to 22.299999237060547
    - In Mileage "105 bhp @ 4400 RPM" was changed to 20.5
- Fuel Tank Capacity was changed from liters to gallons
- Number of owners have been switched into numbers rather than strings (eg. 3rd -> 3)
"""
)

#show off a bit of your data

st.write("Here is what our (clean) data head looks like:")
st.dataframe(data=df.head())

#column example
#col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
#col1.dataframe(df.head())
#col2.markdown("\n") #add a line of empty space.
#col2.markdown('This is a webscrapped data from a car resale websites, which include more details of the cars along with its respective prices.') #you can add multiple items to each column.


st.markdown("""---""")
st.header('Visualizations')

st.subheader("Make Year vs Price")
st.markdown("Cars made in 2019 and up tend to have a higher price than cars made in past years.")
st.plotly_chart(px.scatter(df, x="Make_Year", y="Price"))
st.subheader("Make Year vs Power(BHP)")
st.markdown("Showcasing the fluctuations for power measured by BHP over the course of make years")
ax4 = st.plotly_chart(px.scatter(df, x = "Make_Year", y = "Power(BHP)", color = "Make"))
st.subheader("Make Year vs Torque(Nm)")
fig4 = st.plotly_chart(px.scatter(df, x = "Make_Year", y = "Torque(Nm)", color = "Make"))
st.markdown("Showcasing the fluctuations for torque measured by Nm over the course of make years")
#fig.show()
#In average, in terms of both torque and power the Mahindra and especially Skoda shows continuous growth and improvements
#Maybe like the list on line 61 so you dont have to markdown each line unless you want to?


st.subheader("Number of Previous Owners vs Price")
st.markdown("Every car valued at 13k or more, only has had one owner, with the exception of one car, that has had two owners.")
st.plotly_chart(px.histogram(df, x="Price", color ="No_of_Owners" ))

st.subheader("Price vs Power(BHP)")
st.plotly_chart(px.scatter(df, x = "Power(BHP)", y="Price", color = "Make"))
st.markdown("Comparison between how power relates to the price and it's correlation with torque(the graph below)")
st.subheader("Price vs Torque(Nm)")
st.plotly_chart(px.scatter(df, x = "Torque(Nm)", y="Price", color = "Make"))
st.markdown("Comparison between how torque relates to the price and it's correlation with power(the graphs above)")

st.subheader("Mileage (mph) vs Fuel Tank Capacity (gallons)")
st.plotly_chart(px.scatter(df, x="Mileage(mpg)", y="Fuel_Tank_Capacity(G)", color = "Make"))
st.markdown("As mileage increases, fuel tank capacity tends to decrease. Most makes tend to have a general fuel tank capacity they stick to.")

st.markdown("""---""")
st.subheader("Attributes of Used Cars Above and Below the Average Price")

##TOP INFO
col1, col2= st.columns(2)
top_half = df[df['Price']>8892.233607]
top_total = len(top_half)
#tttop
tt1 = top_half["Transmission_Type"].value_counts()["Manual"]
tt2 = top_half["Transmission_Type"].value_counts()["Automatic"]
labels = "Manual", "Automatic"
sizes = [(tt1/top_total), (tt2/top_total)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#fttop
ft1 = top_half["Fuel_Type"].value_counts()["petrol"]
ft2 = top_half["Fuel_Type"].value_counts()["diesel"]
ft_arr = np.array([(ft1/top_total), (ft2/top_total)])
ft_labels = "petrol", "diesel"

fig2, ax2 = plt.subplots()
ax2.pie(ft_arr, labels=ft_labels, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')

#sctop
sc1 = top_half["Seating_Capacity"].value_counts()[5.0]
sc2 = top_half["Seating_Capacity"].value_counts()[7.0]
sc3 = top_half["Seating_Capacity"].value_counts()[6.0]
sc_arr = np.array([(sc1/top_total), (sc2/top_total), (sc3/top_total)])
sc_labels = ["5", "7", "6"]
fig3, ax3 = plt.subplots()
ax3.pie(sc_arr, labels=sc_labels, startangle=90)
sc_labels = [f'{l}, {s:0.1f}%' for l, s in zip(sc_labels, sc_arr*100)]
ax3.legend(loc='lower left', labels=sc_labels)
ax3.axis('equal')
# st.write('Cars with a Price less than the mean')
#literally same as above but bottom
##BOTTOM INFO
colors = ['#60b8f7', '#fab57d', '#8df7a4', '#ff6193']
# col4, col5, col6 = st.columns(3)
bottom_half = df[df['Price']<=8892.233607]
bottom_total = len(bottom_half)
#ttbot
tt3 = bottom_half["Transmission_Type"].value_counts()["Manual"]
tt4 = bottom_half["Transmission_Type"].value_counts()["Automatic"]
labels = "Manual", "Automatic"
sizes = [(tt3/bottom_total), (tt4/bottom_total)]
fig4, ax4 = plt.subplots()
ax4.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#ftbot
ft3 = bottom_half["Fuel_Type"].value_counts()["petrol"]
ft4 = bottom_half["Fuel_Type"].value_counts()["diesel"]
ft_arr = np.array([(ft3/bottom_total), (ft4/bottom_total)])
ft_labels = "petrol", "diesel"

fig5, ax5 = plt.subplots()
ax5.pie(ft_arr, labels=ft_labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax5.axis('equal')

#scbot
sc0 = bottom_half["Seating_Capacity"].value_counts()[5.0]
sc1 = bottom_half["Seating_Capacity"].value_counts()[7.0]
sc2 = bottom_half["Seating_Capacity"].value_counts()[4.0]
sc3 = bottom_half["Seating_Capacity"].value_counts()[8.0]
sc_arr = np.array([(sc0/bottom_total), (sc1/bottom_total), (sc2/bottom_total), (sc3/bottom_total)])
sc_labels = ["5", "7", "4", "8"]
fig6, ax6 = plt.subplots()
ax6.pie(sc_arr, labels=sc_labels, startangle=90, colors=colors)
sc_labels = [f'{l}, {s:0.1f}%' for l, s in zip(sc_labels, sc_arr*100)]
ax6.legend(loc='lower left', labels=sc_labels)
ax6.axis('equal')

#display the stuff in columns
with col1:
   st.markdown('<b><center>Top Half of the Car Price Range</center> </b>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: center;">Transmission Type:</div>', unsafe_allow_html=True)
   st.pyplot(fig1)
   st.markdown('<div style="text-align: center;">Fuel Type:</div>', unsafe_allow_html=True)
   st.pyplot(fig2)
   st.markdown('<div style="text-align: center;">Seating Capacity:</div>', unsafe_allow_html=True)
   st.pyplot(fig3)
with col2:
   st.markdown('<b><center>Bottom Half of the Car Price Range</center> </b>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: center;">Transmission Type:</div>', unsafe_allow_html=True)
   st.pyplot(fig4)
   st.markdown('<div style="text-align: center;">Fuel Type:</div>', unsafe_allow_html=True)
   st.pyplot(fig5)
   st.markdown('<div style="text-align: center;">Seating Capacity:</div>', unsafe_allow_html=True)
   st.pyplot(fig6)
st.markdown(
    """
    - All used cars are predominantly manual transmission, however there are more automatic transmission cars in the more expensive range)
    - More expensive used cars are usually petrol-fuled, however less expensive used cars are overwhelmingly petrol-powered)
    - All used cars are overwhelmingly 5-seated, seat capacity doesn't seem to have much impact on price
    """
)

st.markdown("""---""")



#Always good to section out your code for readability.
st.header('Insights')
st.subheader('Power(BHP) & Torque(Nm) over Time')
st.markdown('- Chevrolet shows much more rapid growth but only appears in year range of 2013 to 2015 and 2022 ')
st.markdown('- On the other hand, Maruti shows almost no improvements in power(BHP) over the course of make years but they are shown to be recorded each year and currently its starting to go down from its peak which was around the year-range 2014 - 2016')
st.markdown("- The highest power & torque reached in a year was achieved by the Skoda, for 2012, 2014, 2019, and 2022")
st.markdown("- Currently, the highest point reached in both torque and power(250 Nm and 177 BHP) was achieved by the Skoda brand")
st.markdown("- Torque and power are both dependant on the engine speed and are indicators, thus creating a linear relationship")
st.markdown("""
    - Chevrolet: Appearance in 2014 - 2016 and 2022, most rapid growth in power and torque)
    - Maruti: No apparent improvements in terms of power, peaked at year range 2014 to 2016)
    - Skoda: Has the highest power in four of the make years, which are 2012, 2014, 2019, and 2022)
"""
)

st.subheader('Price Insights')
st.markdown("- Every car valued at 13k or more, only has had one owner, with one outlier")
st.markdown("- Every car valued at over 20k was made in from 2019 to 2022")
st.markdown('- Higher power and torque tend to raise the price')
st.markdown("- More expensive cars tend to use automatic transmission and diesel than less expensive ones")
st.subheader('Attributes of the Most and Least Expensive Cars Sold')
st.markdown("""
- Most expensive car sold:
    - Skoda:
        - Power: 250 BHP
        - Torque: 177 Nm
        - Price: 35.292K
- Least expensive car sold:
    - Tata:
        - Power: 35 BHP
        - Torque: 48 Nm
        - Price: 2256
""")
st.markdown("""---""")

#Since its like extra info maybe "about the authors" sorta thing at the end?
st.header('')





