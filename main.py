import streamlit as st

from streamlit_option_menu import option_menu


import credit , fraud , insurance , customer_service
st.set_page_config(
        page_title="ABC Bank",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='ABC Bank',
                options=['Credit Score Prediction','Fraud Detection','Car Insurance claim','customer service Chatbot'],
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )


        
        if app == "Credit Score Prediction":
            credit.app()
        if app == "Fraud Detection":
            fraud.app()    
        if app == "Car Insurance claim":
            insurance.app()        
        if app == 'customer service Chatbot':
            customer_service.app()
          
             
    run()            
         