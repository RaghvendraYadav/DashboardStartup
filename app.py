import streamlit as st
import pandas as pd

st.title('STARTUP DASHBOARD')
st.header('I Am Learning Streamlit')
st.subheader('It is easy than flask')
st.write('This is a normal Text')
st.markdown('''
### My Favourite Movies
- Race 3
- Humskul
''')

st.code("""
def foo(input):
    return input**2
x=foo(2)
""")

st.latex('x^2 + y^2 = 1')

df=pd.DataFrame(
    {
        'name':['Nitesh','KP','Bobby','Raghvendra'],
        'company':['TCS','Infy','Byjus','Infy']
    }
)
st.dataframe(df)
st.metric('Revenue','RS 3 lakh','3%')
st.json(
{
        'name':['Nitesh','KP','Bobby','Raghvendra'],
        'company':['TCS','Infy','Byjus','Infy']
    }
)

