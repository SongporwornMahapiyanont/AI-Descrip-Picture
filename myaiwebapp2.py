import streamlit as st
import io
from PIL import Image

import google.generativeai as genai
genai.configure(api_key="AIzaSyA0TwQnk0mKo9rgnty9z9l05hoz7F2dfmU")
model = genai.GenerativeModel("gemini-pro-vision")

st.set_page_config(page_title="LNC-BOT")
st.title("Welcome To LNC-BOT")
st.markdown(f'<p style="background-color:#cc6666;color:#ffffff;font-size:150%;text-align:center">{"Create by Songporworn Mahapiyanont"}</p>', unsafe_allow_html=True)
text4 = "AI By Gemini (google)"
st.markdown(f'<p style="text-align:right">{text4}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center">{"This Web is My project for reseach, learning ,etc."}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center">{"You can copy for using learning etc. - Have for fun Guy!"}</p>', unsafe_allow_html=True)

a = 9999
st.write(a)
#prompt = st.text_input("ป้อน prompt: ","บรรยายภาพนี้")
                  
prompt = "คืออะไรไม่ต้องบอกระเอียดมาก ถ้าสิ่งของมีสีดำหรือเทาหรือน้ำตาลให้บอกว่า'เสีย'และถ้าไม่มีให้บอกว่า'ไม่เสีย' มีจำนวนเท่าไหร่บอกหน่วยด้วยและมีประมาณกี่กิโลกรัมทศนิยมสองตำแหน่งและแช่ในตู้เย็นจะหมดอายุประมาณกี่วัน ตอบทุกคำถามจัดระเบียบคำตอบให้สวยงาม"

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



model2 = genai.GenerativeModel("gemini-pro")

st.title("Translate")
ch = st.selectbox("Type your language",
                 ("thai","english","korea","japan"))

text_in = st.text_input("input your word : ")

prompt = "Translate language " + text_in + " to " + ch  
st.text(prompt)

if st.button("Translate"):
    try:
        response = model2.generate_content(prompt)
        st.text(response.text)
    except:
        st.text("no response")


    



