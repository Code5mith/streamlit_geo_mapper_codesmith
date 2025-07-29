import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as mplot
from fetch import fetch

urls = ["https://financialmodelingprep.com/api/v3/quote/AAPL?datatype=json","https://jsonplaceholder.typicode.com/users", "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max"]

st.markdown(
    '''
        # Streamlit **GeoMapper**
    '''
)

# API call
response = fetch(urls[1]) 

df = pd.DataFrame(response)
df = df.reset_index()

geo_locs = {"lat" : [], "lng": []}

for item in response:
    for key,value in item.items():
        if key == "address":
            for key,value in value.items():
                if key == "geo":
                    for key,value in value.items():
                        geo_locs[key].append(value)

df2 = pd.DataFrame(geo_locs)

# Ya i see it
df2 = df2.rename(columns={"lng":"lon"})

# Convert dtype to type float 
df2["lat"] = pd.to_numeric(df2["lat"], errors="coerce").astype(float)
df2["lon"] = pd.to_numeric(df2["lon"], errors="coerce").astype(float)

# USER - LOCATION 
user_loc_df = {"name":[],"street":[], "geo_coordinate":[]}

for row in df.iterrows():
    user_loc_df["name"].append(row[1]["name"])
    user_loc_df["street"].append(row[1]["address"]["street"])
    user_loc_df["geo_coordinate"].append(row[1]["address"]["geo"])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.write(df)
st.table(df2)
st.header("Section 2")
st.line_chart(df2)
st.bar_chart(df2)
st.title("User -> Geo_Coordinate Table")
st.table(user_loc_df)
st.header("Map")
st.map(df2)
st.header("Test Map")
st.map(map_data)