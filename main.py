import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamli 超入門')

st.write('プログレスバー')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字')
if button:
  right_column.write("右カラムです")

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容')

st.write('DataFrame')

df = pd.DataFrame({'一列目': [1,2,3,4],
                  '二列目': [10,50,30,40],
                  })

st.write('Streamlit 超入門')

condition = st.sidebar.slider('今のコンディション', 0,100,50)
text = st.sidebar.text_input('あなたの趣味は？')


option = st.selectbox(
  'あなたの好きな数字は',
  list(range(1,11))
)

st.write(option," ",text," ", condition)


st.write('Display Image')

if st.checkbox('画像表示'):
  img = Image.open('AJJJ0523.jpg')
  st.image(img, caption='MinatoMirai', use_column_width=True)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamli 超入門')

st.write('DataFrame')

```

$a_a$
"""