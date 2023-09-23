import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Airbnb Listings and The Van Gogh Museum")
st.markdown("Imagine you want to visit the **Van Gogh Museum** in Amsterdam, Netherlands. Let's say you on a budget and want to find a place close to the museum to stay. The visualization below will help you do just that with minimal effort!")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 100 pounds per night
dataframe = dataframe[dataframe["Price"] <= 100]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "£ " + dataframe["Price"].round(2).astype(str) # <--- CHANGE THIS POUND SYMBOL IF YOU CHOSE CURRENCY OTHER THAN POUND
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the location we've chosen with a blue dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    color_discrete_sequence=["blue", "red"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)

st.markdown("*Shoutout*📣: To **NumPy** for an efficient 🔥 data manipulation. To **pandas** 😉 for displaying the dataset as seen above. And to the team 🥰 at **Uplimit** for making all this possible 🙏")
st.markdown("PS: The visualization might not be useful to you at the time of viewing it as various factors such as price, space etc. surrounding Airbnb listings might have changed after creating it. ")
