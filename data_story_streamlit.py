import streamlit as st
import pandas as pd

st.write("""
# How do the amount of rinks and courts in Pittsburgh neighborhoods connect to other data sets?
         
For my dataset I wanted to look at all the basketball, tennis, pickleball and bocce courts as well as hockey rinks in the city of Pittsburgh to see if there was any correlation between them.
""")

data = pd.read_csv("rinksAndCourts.csv")
data.columns = data.columns.str.strip()
locations_by_district = data['council_district'].value_counts()
locations_by_district_sorted = locations_by_district.sort_index()
st.title('Amount of Rinks and Courts per Council District')
st.bar_chart(locations_by_district_sorted)

data = pd.read_csv("arrests.csv")
data.columns = data.columns.str.strip()
arrests_by_district = data['COUNCIL_DISTRICT'].value_counts()
arrests_by_district_sorted = arrests_by_district.sort_index()
st.title('Amount of Arrests per Council District')
st.bar_chart(arrests_by_district_sorted)
