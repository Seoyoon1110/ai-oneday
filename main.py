# from openai import OpenAI
# import streamlit as st

# client = OpenAI(api_key=st.secrets["API_KEY"])

# chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "user",
#         "content": "너에 대해서 설명해줘",
#     }],
#     model="gpt-4o",
# )

# chat_result = chat_completion.choices[0].message.content
# print(chat_result)

# response = client.images.generate(
#     model="dall-e-3",
#     prompt="대나무 숲의 판다",
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )

# image_url = response.data[0].url
# print(image_url)

import streamlit as st
from openai import OpenAI

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

client = OpenAI(api_key=st.secrets["API_KEY"])

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
  with st.spinner('생성 중입니다.'):
      chat_completion = client.chat.completions.create(
          messages=[{
              "role": "user",
              "content": keyword + " 에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
          }],
          model="gpt-4o",
      )
    
      chat_result = chat_completion.choices[0].message.content
    
      response = client.images.generate(
          model="dall-e-3",
          prompt=keyword,
          size="1024x1024",
          quality="standard",
          n=1,
      )
      image_url = response.data[0].url
      st.write(chat_result)
      st.image(image_url)