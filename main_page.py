import streamlit as st
from PIL import Image
import os 

_abspath = os.path.dirname(os.path.abspath(__file__))+'/data/'

st.header('메인페이지')
image_path1 = _abspath + 'news1.png'
image_path2 = _abspath + 'news2.png'
image_path3 = _abspath + 'news3.png'
# image = Image.open(image_path) # 경로와 확장자 주의!
# st.image(image)

col1, col2= st.columns(2)
with col1:
    image1 = Image.open(image_path1)
    st.image(image1)
    st.markdown('[뉴스 보기](https://www.hani.co.kr/arti/opinion/editorial/1087645.html)' )

with col2:
    image3 = Image.open(image_path3)
    st.image(image3)
    st.markdown('[뉴스 보기](https://www.donga.com/news/Society/article/all/20221110/116425004/1)' )

# with col3:
#     image3 = Image.open(image_path3)
#     st.image(image3)
# st.markdown("[![Foo](_abspath + 'news1.png')](https://www.hani.co.kr/arti/opinion/editorial/1087645.html)")
# st.markdown("[![Foo](https://i.imgur.com/SJocsgm.png)](https://www.hani.co.kr/arti/opinion/editorial/1087645.html)")
#[img]https://i.imgur.com/SJocsgm.png[/img]