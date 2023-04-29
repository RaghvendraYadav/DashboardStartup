import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(layout='wide')
df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month']=df['date'].dt.month



def load_overall_analysis():
    st.title('Overall Analysis')
    total = str(round(df['amount'].sum()))
    max_amount = df.groupby('startup')['amount'].sum().max()
    avg_amount=round(df.groupby('startup')['amount'].sum().mean())
    total_funded_startups=len(set(df['startup']))
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.metric("Overall Invested Amount",total+ " Cr.")
       #max Amount  infused in Starup

    with c2:
        st.metric('Overall Maximum Amount',str(max_amount)+" Cr.")

    with c3:
        st.metric('Overall Average Funding',str(avg_amount)+" Cr.")
    with c4:
        st.metric('Total Funded Startups',total_funded_startups)
    st.subheader('Mom Graph')
    selected_option=st.selectbox("select type",['Count','Sum'])
    if selected_option == 'Sum':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x1_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig7, ax7 = plt.subplots()
    ax7.plot(temp_df['x1_axis'], temp_df['amount'])
    st.pyplot(fig7)


def  load_investors(investor):
    st.title(investor)
    last5_df=df[df['investors'].str.contains(investor)].head(5)[['date','startup','city','vertical','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    #Biggest Investment
    col1,col2=st.columns(2)
    with col1:
        biggest_invest=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5 )
        st.subheader('Most Biggest Investments')
        #st.dataframe(biggest_invest)
        fig,ax=plt.subplots()
        ax.bar(biggest_invest.index,biggest_invest.values)
        st.pyplot(fig)
    with  col2:
       sectors_df=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
       st.subheader('Sectors Invested In')
       fig1,ax1=plt.subplots()
       ax1.pie(sectors_df,labels=sectors_df.index,autopct="%0.01f%%")
       st.pyplot(fig1)
    col3,col4 =st.columns(2)
    with col3:
        stage_df = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Stage Invested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_df, labels=stage_df.index, autopct="%0.01f%%")
        st.pyplot(fig2)
    with col4:
        city_df = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('City Invested In')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_df, labels=city_df.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    year_df=df[df['investors'].str.contains('Sequoia Capital India')].groupby('year')['amount'].sum()
    st.subheader('Year Invested In')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_df.index,year_df.values)
    st.pyplot(fig4)
st.sidebar.title('StartUp Dashboard')




option=st.sidebar.selectbox('Select One ',['Overall Analysis','Startups','Investors'])
if option =='Overall Analysis':
    btn2=st.sidebar.button('Overall Analysis')
    load_overall_analysis()
elif option == 'Startups':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Startup Details')
    if btn1:
        st.title('Startup Analysis')
else:
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button("Investor's Details ")
    if btn2:
        load_investors(selected_investor)

