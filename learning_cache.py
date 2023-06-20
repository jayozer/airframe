import streamlit as st
import time


@st.cache_data
def slow_function(arg):
   time.sleep(2) # Simulating a slow operation
   return arg


def main ():
   result = slow_function(1)
   st.write("Result:", result)


   # This will return the cached result immediately, without executing the function again
   result = slow_function(1)
   st.write("Result:", result)