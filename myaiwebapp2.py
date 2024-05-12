import streamlit as st
import io
from PIL import Image

import google.generativeai as genai
genai.configure(api_key="AIzaSyA0TwQnk0mKo9rgnty9z9l05hoz7F2dfmU")
model = genai.GenerativeModel("gemini-pro-vision")

st.title("ยินดีต้อนรับสู่การบรรยายภาพ")
#prompt = st.text_input("ป้อน prompt: ","บรรยายภาพนี้")
                  
prompt = "สิ่งนี้คืออะไร"

img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:
    imagefile = io.BytesIO(img_file.read())
    img = Image.open(imagefile)
    st.image(img_file,channels="BGR")

if st.button("ประมวลผล"):
    try:
        response = model.generate_content([img,prompt])
        if st.text(response.text)=='ไข่ไก่':
            descrip = "มีกี่ฟอง"
            answer = model.generate_content([img,descrip])
            st.text(answer.text)
        print(response)
    except:
        st.text("no response")




    



