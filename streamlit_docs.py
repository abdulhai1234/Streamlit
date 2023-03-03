import streamlit as st
import pandas as pd
import time

# title
st.title("startup  Dashboard")

# header
st.header('I am Learning Streamlit')
# subheader
st.subheader("Hello this is me")

# paragraph printing
st.write("this is my paragraph")

# markdown
st.markdown("""
### this is my thired level heading in markdown
- heading 1
- heading 2
""")
# code in streamlit
st.code("""
def foo(input):
    return input**2
x = foo(20)
""")

# adding latex
st.latex('x^2+y^3+2=0')

# Display Elements
# display dataframe
df = pd.DataFrame({
    "Name":['Ali','Ahmad','Mamood'],
    "Marks":[10,20,30],
    "Package":[30,40,50]
})
st.dataframe(df)

# metric
st.metric("Revenue",'Rs 3L','+3%')

# json
st.json({
    "Name":['Ali','Ahmad','Mamood'],
    "Marks":[10,20,30],
    "Package":[30,40,50]
})

# working with images
st.image("widget_image.jpg")

# working with videos
st.video("vecteezy_the-footage-animation-of-countdown-timer-from-5-seconds__666.mp4")

# sidebar
st.sidebar.title("Dashboard Sidebar")

# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image("widget_image.jpg")
with col2:
    st.image("widget_image.jpg")
with col3:
    st.image("widget_image.jpg")

# messages
st.error("this is error message")

st.success("this is success message")

st.info("this is info message")
st.warning("this is warning message")

# progress bar
bar = st.progress(0)
for i in range(1,100):
    # time.sleep(0.1)
    bar.progress(i)

# user input
text = st.text_input("Enter Some texts")
# getting number
number = st.number_input("Enter Number")

# button
st.button("Click Me")
