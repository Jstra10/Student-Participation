import streamlit as st

st.title("Student Performance Application Project")
st.text('My Coding Temple Project application that utilizes Pandas, Streamlit, SkLearn, SpaCy, MongoDB, Plotly, and Python to create a MTG Recommendation System')

st.header('Here are the different pages of my application:')
st.subheader('Summary:')
st.text('Summary Page, explaining all the inner workings of my application and the "why" behind decisions we made!')

st.subheader('Query')
st.text('Query: Allows a user to enter a card name and queries the database in mongo for all information matching that card name. Card names MUST be exact')

# st.subheader('Relationships')
# st.text('')

st.subheader('Interactive Charts')
st.text('Interactive Charts: Ability to create visualizations using Plotly')


