import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    # st.image("images/photo-kt.png")
    st.title("Katie Taghavian")

with col2:

    content = """
    Data Analytics Engineer with a proven track record of over 10 years, 
    excelling in designing robust data infrastructure, architecting scalable data models, and delivering impactful 
    advanced analytics solutions across diverse industries such as Banking, Healthcare, Automotive, and Social Media.
    Proficient in end-to-end analytics strategies, optimizing data import efficiency, and driving cost-effective 
    operational enhancements. Expertise in SQL, Python scripting, and data mining. Demonstrated mastery in Tableau 
    for dynamic data visualization. Recognized for collaborative prowess in translating intricate concepts into 
    actionable insights and collaborating with leaders to refine key performance measures that drive improvements 
    in cost, quality, and speed. Renowned for effective leadership, fostering collaboration, and achieving data-driven 
    success. A dedicated learner with an unwavering commitment to staying updated on industry trends and innovations.
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python.Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")




