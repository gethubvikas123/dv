import pandas as pd
import streamlit as st
data=[[1,"M",50,5.5],[2,"F",55,5.7],[3,"F",60,5.8],[4,"M",70,5.9],[5,"M",75,6.2]]
df=pd.DataFrame(data,columns=["sr.no","Gender","Weight","Height"])
df
st.table(df)
st.line_chart(df["Weight"])
