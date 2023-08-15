import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo-kt.png")

with col2:
    st.title("Katie Taghavian")
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