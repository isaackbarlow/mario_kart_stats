import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')

st.dataframe(df_kart)

df_kart = df_kart[['Body','Weight']]

line_chart = df_kart({
  'on_traction' : df_kart['On-Road traction'],
  'off_traction' : df_kart['Off-Road traction'],
  'Body' : df_kart['Body']
})
st.line_chart(
  df_kart, 
  x ='Body', 
  y = ['on_traction', 'off_traction'
])

area_chart = df_kart({
  'gr_hand' : df_kart['Ground Handling'],
  'wa_hand' : df_kart['Water Handling'],
  'grav_hand' : df_kart['Anti-Gravity Handling'],
  'air_hand' : df_kart['Air Handling'],
  'Body' : df_kart['Body']
})

st.area_chart(
  df_kart,
  x = 'Body',
  y = ['gr_hand', 'wa_hand', 'grav_hand', 'air_hand']
)


chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')

                                                                                     

