import snowflake.connector
import streamlit as st
my_cnx = snowflake.connector.connect(user = "rravisekar",
                                     password = "Rachana33$",
                                     account = "ID89449.ca-central-2.aws",
                                     warehouse = "compute_wh",
                                     database = "zenas_athleisure_db",
                                     schema = "products")
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
