import streamlit as st
import pandas

data = {
    'Series_1': [1, 3, 4, 5, 7],
    'Series_2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)
st.title("Our fisrt App")
st.subheader("Instroduction to Streamlit")
st.write("""
    This is our first Web Application!
    Enjoy it!
""")
st.write(df)
st.line_chart(df)
st.area_chart(df)

mySlider = st.slider("Celsius")
st.write(mySlider, "in Fahrenheit in", mySlider = 9/5 + 32 )