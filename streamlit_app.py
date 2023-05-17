import streamlit
import pandas
import requests

streamlit.title('Meal options')
streamlit.header('Breakfast Ideas')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Smoothie Build 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# pick the fruit I want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display
streamlit.dataframe(fruits_to_show)

#Display fruityvice api response
streamlit.header("Fruityvice Fruit Advice")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#take json version and normalise it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display normalised version
streamlit.dataframe(fruityvice_normalized)
