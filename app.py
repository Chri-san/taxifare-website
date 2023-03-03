import streamlit as st
import requests
import datetime
import plotly.express as px
import plotly.graph_objects as go

'''
# TaxiFareModel
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''


date = st.text_input('start date', "2013-07-06 17:18:00")
st.write(date)

pickup_longitude = st.text_input("Choose the pickup longitude", '41.123456')
pickup_latitude = st.text_input("Choose the pickup latitude", '41.123456')
dropoff_longitude = st.text_input("Choose dropoff_longitude", '41.123456')
dropoff_latitude = st.text_input("Choose the dropoff_latitude", '41.123456')
passenger_count = st.text_input("Choose the number of passengers", '1')

st.write('The pickup_datetime:', date)
st.write('pickup_longitude:', pickup_longitude)
st.write('pickup_latitude:', pickup_latitude)
st.write('dropoff_longitude:', dropoff_longitude)
st.write('dropoff_latitude:', dropoff_latitude)
st.write('passenger_count:', passenger_count)

Dictionary = {"key": '0', "pickup_datetime": date, "pickup_longitude": pickup_longitude, "pickup_latitude": pickup_latitude, "dropoff_longitude": dropoff_longitude, "dropoff_latitude": dropoff_latitude, "passenger_count": passenger_count}

result = requests.get(url, params=Dictionary).json()


st.write(result)


token = open(".mapbox_token").read()


fig = px.scatter_mapbox(
    lon = [float(pickup_longitude), float(dropoff_longitude)], lat = [float(pickup_latitude), float(dropoff_latitude)],
    text = ["Start", "Stop"],
    zoom=11,
    center={'lon':float(pickup_longitude),'lat':float(pickup_latitude)})

fig.add_trace(
    go.Scattermapbox(
        lat=[float(pickup_latitude), float(dropoff_latitude)],
        lon=[float(pickup_longitude), float(dropoff_longitude)],
        mode='lines',
        line=dict(width=2, color='blue')
    )
)

fig.update_layout(mapbox_style="carto-positron")

with st.container():
    st.plotly_chart(fig)
