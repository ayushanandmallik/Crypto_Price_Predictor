import streamlit as st
import pyrebase



#custom imports
from multipage import MultiPage
from pages import predict, prices




#creating an instance of the app
app= MultiPage()

#title of the main page
#st.title('CryptoCurrency Price Prediction')

#adding all the pages to the website
app.add_page('Predict the future price',predict.app)
app.add_page('Top CryptoCurrencies', prices.app)
#app.add_page('Demo', demo.app)


#running the main app
app.run()
