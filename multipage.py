import streamlit as st

#Defining the multipage class to manage multiple pages in web app
class MultiPage:
    def __init__(self):
        #constructor class to generate a list which will store all our applications as we create them

        self.pages=[]

    def add_page(self,title,func)->None:
        #class method to add pages to the app. Args= title: The title of page which we are adding to the web app. func: Python function to render the page in app.
        self.pages.append( {
            'title': title,
            'function': func
        })
    def run(self):
        #Dropdown to select the page to go to

        page= st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )

        #running the app function
        page['function']()

