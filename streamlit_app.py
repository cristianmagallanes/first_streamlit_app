import streamlit
streamlit.title ('My parents New Healty Dinner')


streamlit.header ('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')

streamlit.text('Hard-Boiled free-Renge Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(fruits_to_show)

