import streamlit as st
import io
from PIL import Image

import google.generativeai as genai
genai.configure(api_key="AIzaSyA0TwQnk0mKo9rgnty9z9l05hoz7F2dfmU")
model = genai.GenerativeModel("gemini-pro-vision")

st.title("ยินดีต้อนรับสู่การบรรยายภาพ")
#prompt = st.text_input("ป้อน prompt: ","บรรยายภาพนี้")
                  
prompt = "สิ่งนี้คืออะไร ถ้าคือไข่ไก่มีกี่ฟองและถ้าไม่ใช่ไข่ไก่ไม่ต้องบอกว่ามีกี่ฟอง ถ้าคือเนื้อหมูมีประมาณกี่กิโลกรัมและดูใกล้หมดอายุหรือยังและถ้าไม่ใช่เนื้อหมูไม่ต้องบอกว่ามีกี่กรัม"

img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:
    imagefile = io.BytesIO(img_file.read())
    img = Image.open(imagefile)
    st.image(img_file,channels="BGR")

if st.button("ประมวลผล"):
    try:
        response = model.generate_content([img,prompt])
        st.text(response.text)
    except:
        st.text("no response")




    



