import streamlit as st
from datetime import datetime, timedelta 
import pandas as pd
import numpy as np
import pydeck as pdk
import os
def find_time(timeline):
  timeline = timeline.strftime('%H:%M')
  if timeline=='05:30':
    return '05:30~05:59'
  elif timeline=='06:00':
    return '06:00~06:29'
  elif timeline=='06:30':
    return '06:30~06:59'
  elif timeline=='07:00':
    return '07:00~07:29'
  elif timeline=='07:30':
    return '07:30~07:59'
  elif timeline=='08:00':
    return '08:00~08:29'
  elif timeline=='08:30':
    return '08:30~08:59'
  elif timeline=='09:00':
    return '09:00~09:29'
  elif timeline=='09:30':
    return '09:30~09:59'
  elif timeline=='10:30':
    return '10:30~10:59'
  elif timeline=='11:00':
    return '11:00~11:29'
  elif timeline=='11:30':
    return '11:30~11:59'
  elif timeline=='12:00':
    return '12:00~12:29'
  elif timeline=='12:30':
    return '12:30~12:59'
  elif timeline=='13:00':
    return '13:00~13:29'
  elif timeline=='13:30':
    return '13:30~13:59'
  elif timeline=='14:00':
    return '14:00~14:29'
  elif timeline=='14:30':
    return '14:30~14:59'
  elif timeline=='15:00':
    return '15:00~15:29'
  elif timeline=='15:30':
    return '15:30~15:59'
  elif timeline=='16:00':
    return '16:00~16:29'
  elif timeline=='16:30':
    return '16:30~16:59'
  elif timeline=='17:00':
    return '17:00~17:29'
  elif timeline=='17:30':
    return '17:30~17:59'
  elif timeline=='18:00':
    return '18:00~18:29'
  elif timeline=='18:30':
    return '18:30~18:59'
  elif timeline=='19:00':
    return '19:00~19:29'
  elif timeline=='19:30':
    return '19:30~19:59'
  elif timeline=='20:00':
    return '20:00~20:29'
  elif timeline=='20:30':
    return '20:30~20:59'
  elif timeline=='21:00':
    return '21:00~21:29'
  elif timeline=='21:30':
    return '21:30~21:59'
  elif timeline=='22:00':
    return '22:00~22:29'
  elif timeline=='22:30':
    return '22:30~22:59'
  elif timeline=='23:00':
    return '23:00~23:29'
  elif timeline=='23:30':
    return '23:30~23:59'

def draw_graph(temp) :
  hon = pd.DataFrame()
  i = 37
  while i>=0:
    #temp의 혼잡도 = j
    j = round(temp.iloc[i][1])
    while j>0:
      hon=pd.concat([hon, position_9.iloc[i,[2,3]]])
      # hon =hon.append(position_9.iloc[i,[2,3]])
      j-=1
    i -= 1
  # hon_p=hon.pivot( columns=0, values='0')
  # hon.values
  # hon.reshape(-1,2)
  hon=hon.values.reshape(-1,2)
  hon=pd.DataFrame(hon)
  hon.columns=['lat', "lon"]
  st.write(hon, hon.shape)
  st.pydeck_chart(pdk.Deck(
      map_style=None,
      initial_view_state=pdk.ViewState(
          latitude=37.51,
          longitude=126.99,
          zoom=10.5,
          pitch=50,
      ),
      # tooltip={
      #   'html': '{hon.구분}<b>혼잡도:</b> {elevationValue}',
      #   'style':{
      #     'color':'white'
      #   }
      # },
      layers=[
          pdk.Layer(
            'HexagonLayer',
            data=hon,
            get_position='[lat, lon]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 2000],
            pickable=True,
            extruded=True,
            
          ),
          pdk.Layer(
              'ScatterplotLayer',
              data=hon,
              get_position='[lat, lon]',
              get_color='[200, 30, 0, 160]',
              get_radius=200,
              
          ),
      ],
  ))

def show_table(temp):
  temp.columns = ['역명', '해당 시간 혼잡도']
  st.table(temp)


folder = '/../data/'
position_path = os.path.dirname(os.path.abspath(__file__))+folder+'9_position.csv'
h_2020_path = os.path.dirname(os.path.abspath(__file__))+folder+'9_honjab2020.csv'
position_cols = ['name', 'position', 'lat', 'lon','line']
position_9 = pd.read_csv(position_path, names=position_cols)
position_9['name'] = position_9['name'].str.replace(pat='역',repl='', regex=True)

#honjab_2020 = pd.read_csv('9_honjab2020.csv', index_col=0, header =0)
honjab_2020 = pd.read_csv(h_2020_path)
#hon: 매번 혼잡도만큼 위도경도개수 저장하는 dataframe


st.sidebar.header("시간 조절하기")
st.header('9호선 혼잡도 시간별로 알아보기')

# time_check = datetime(2000, 1, 1, 5,30)
timeline = st.sidebar.slider('시간대를 골라주세요', value=datetime(2020,1,1,5,30), min_value=datetime(2020,1,1,5,30), max_value=datetime(2020,1,1,23,59), step=timedelta(minutes=30), format='hh:mm' ,key='start')
# st.write((timeline))
# count = 0
# while True:
#   if timeline != timeline:
#     temp = honjab_2020.loc[: , ['구분',find_time(timeline)]]
#     draw_graph(temp)
  
#   # timeline = st.sidebar.slider('시간대를 골라주세요', value=datetime(2020,1,1,5,30), min_value=datetime(2020,1,1,5,30), max_value=datetime(2020,1,1,23,59), step=timedelta(minutes=30), format='hh:mm', key=count)
#   # timeline_check = timeline
#   count+=1
temp = honjab_2020.loc[: , ['구분',find_time(timeline)]]
draw_graph(temp)
st.write('* 혼잡도는 30분간 각 역사를 지나는 열차들의 평균 혼잡도입니다')
st.write('* (정원대비 승차인원으로 6칸열차에 922명이 승차한 경우 혼잡도 100% 산정)')

show_table(temp)
