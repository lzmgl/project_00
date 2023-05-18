import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd
import pydeck as pdk
import math

st.title('9호선 시간대별 혼잡도(2020)')

df = pd.read_csv('9_honjab2020.csv', encoding='utf-8')
pos = pd.read_csv('9_position.csv', encoding='utf-8')
df.columns=['idx', '구분']+list(map(str, list(range(0,37,1))))

pos.columns=['idx','역명','수도권','위도','경도','선명']
# print(df)
# stock_name = st.sidebar.text_input('역 이름') 

arr_ = []
for i in range(24):
    st_time = str(i).zfill(2)
    end_time = str(i + 1).zfill(2)
    arr_.append(f"{st_time}:00 ~ {st_time}:30")
    arr_.append(f"{st_time}:30 ~ {end_time}:00")

arr_=arr_[11:]

df['구분']+='역'
df_sor= df.sort_values(by='구분')
pos_sor= pos.sort_values(by='역명')

df_sor['위도']=pos_sor['위도']
df_sor['경도']=pos_sor['경도']
st.dataframe(df_sor)
time = st.select_slider('시간 선택', options=arr_)

df_sor= df_sor.sort_values(by='idx')
df_sor["exits_radius"] = df_sor[f"{arr_.index(time)}"]+50
df_sor["exits_color"] = df_sor[f"{arr_.index(time)}"]/136

#출근
df_sor["go_rad"] = df_sor["5"]+50
df_sor["go_col"] = df_sor["5"]/136

#퇴근
df_sor["back_rad"] = df_sor["25"]+50
df_sor["back_col"] = df_sor["25"]/136
# df_sor["exits_radius"] = df_sor[f"{arr_.index(time)}"].apply(lambda exits_count: math.sqrt(exits_count))

# for idx, item in enumerate(arr_):
#     df_sor[str(idx)] += 10


st.write(
    # df_sor[["구분",f'{arr_.index(time)}']].T,
    # df_sor[[f'{arr_.index(time)}', '경도', '위도']],
    # df_sor
)
# tmp={}
# tmp['경도']=df_sor['경도']
# tmp['위도']=df_sor['위도']
# tmp[f'{arr_.index(time)}']=df_sor[f'{arr_.index(time)}']


# tmp=df_sor[[f'{arr_.index(time)}', '경도', '위도']]
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.5035,
        longitude=126.9961,
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df_sor,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position='[경도, 위도]',
            get_radius='exits_radius',
            get_fill_color='[255*exits_color, 90, 90]',
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
        ),
        
        # pdk.Layer(
        #     'ScatterplotLayer',
        #     data=df_sor,
        #     get_position='[경도, 위도]',
        #     radius='exits_radius',
        #     get_fill_color='[0, 0, 0]',
        #     pickable=True,
        #     extruded=True,
        # ),
    ],
))


# The layer therefore falls back to an 8-bit low-precision mode, where weights must be integers and the accumulated weights in any pixel cannot exceed 255

st.title("출근 시간")
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.5035,
        longitude=126.9961,
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df_sor,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position='[경도, 위도]',
            get_radius='go_rad',
            get_fill_color='[255*go_col, 90, 90]',
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
        ),
    ],
))
st.title("퇴근 시간")
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.5035,
        longitude=126.9961,
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df_sor,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position='[경도, 위도]',
            get_radius='back_rad',
            get_fill_color='[255*back_col, 90, 90]',
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
        ),
    ],
))