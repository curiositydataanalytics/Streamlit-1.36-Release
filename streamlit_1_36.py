# Data process
import numpy as np
import datetime as dt
import pandas as pd

# Data viz
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)



# App title
st.title("What's new in Streamlit 1.36?")
st.logo("logo.png")
st.divider()

with st.sidebar:
    st.image('background.png')

#
#

def home_page():

    # 1) Introducing st.navigation and st.Page
    #---------------------------------------------------------------------------------------#
    st.header(':one: Introducing st.navigation and st.Page')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.35')
    cols[1].subheader('Streamlit 1.36')

    cols[0].image('screenshot_1.png')
    cols[0].image('screenshot_2.png')

    cols[1].code('''
    def page1():
        # code from 1_page_1.py

    def page2():
        # code from 2_page_2.py
                
    pg = st.navigation([st.Page(page1, title='Page 1'), st.Page(page2, title='Page 2')])
    pg.run()
    ''')

    st.divider()

    # 2) st.bar_chart can render charts horizontally
    #---------------------------------------------------------------------------------------#
    st.header(':two: st.bar_chart can render charts horizontally')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.35')
    cols[1].subheader('Streamlit 1.36')

    cols[0].code('''
    st.bar_chart(df)
    ''')
    cols[1].code('''
    st.bar_chart(df, horizontal=True)
    ''')

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    cols = st.columns(2, vertical_alignment='center')
    cols[0].bar_chart(chart_data, horizontal=False)

    cols[1].bar_chart(chart_data, horizontal=True)

    st.divider()

    # 3) st.expander supports adding an icon next to its label
    #---------------------------------------------------------------------------------------#
    st.header(':three: st.expander supports adding an icon next to its label')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.35')
    cols[1].subheader('Streamlit 1.36')

    cols[0].code('''
    st.expander('Warning')
    ''')
    cols[1].code('''
    st.expander('Warning', icon=":material/warning:")
    ''')

    # expander
    cols = st.columns(2)
    with cols[0].expander("Warning"):
        st.empty()
    with cols[0].expander("See explanation"):
        st.empty()
    with cols[0].expander("FAQ"):
        st.empty()

    with cols[1].expander("Warning", icon=":material/warning:"):
        st.empty()

    with cols[1].expander("See explanation", icon=":material/info:"):
        st.empty()

    with cols[1].expander("FAQ", icon=":material/question_mark:"):
        st.empty()

    st.divider()

    # 4) st.columns lets you set vertical alignment.
    #---------------------------------------------------------------------------------------#
    st.header(':four: st.columns lets you set vertical alignment')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.35')
    cols[1].subheader('Streamlit 1.36')

    cols[0].code('''
    st.columns(2)
    ''')
    cols[1].code('''
    st.columns(2, vertical_alignment='center')
    ''')


    subcols = cols[0].columns(2)

    subcols[0].image("logo.png", width=200)
    subcols[1].image("1_9Ml5_jx8SPibG0aJ4r7iDw2.png", width=200)

    subcols = cols[1].columns(2, vertical_alignment='center')

    subcols[0].image("logo.png", width=200)
    subcols[1].image("1_9Ml5_jx8SPibG0aJ4r7iDw2.png", width=200)

    st.divider()

    # 5) You can now customize axis labels for st.area_chart, st.bar_chart, st.line_chart, and st.scatter_chart
    #---------------------------------------------------------------------------------------#
    st.header(':five: You can now customize axis labels for st.area_chart, st.bar_chart, st.line_chart, and st.scatter_chart')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.35')
    cols[1].subheader('Streamlit 1.36')


    cols[0].code('''
    st.line_chart(df, x='x', y='y')
    ''')
    cols[1].code('''
    st.line_chart(df, x='x', y='y', x_label='time', y_label='count')
    ''')

    linechart_data = pd.DataFrame({'x' : [1,2,4,5,7,8], 'y' : [2,5,6,8,9,13]})
    cols[0].line_chart(linechart_data, x='x', y='y')
    cols[1].line_chart(linechart_data, x='x', y='y', x_label='time', y_label='count')

    st.divider()

def page1():
    st.title(':one: First Page')
    st.subheader('This is my first page')

def page2():
    st.title(':two: Second Page ')
    st.subheader('This is my second page')

pg = st.navigation([st.Page(home_page, title='Home Page'), st.Page(page1, title='Page 1'), st.Page(page2, title='Page 2')])
pg.run()


