import random
import time
import streamlit as st

# Cấu hình trang web
st.set_page_config(
    page_title="Chúc Mừng 20/10 🌸", page_icon="🌷", layout="centered"
)

# CSS tùy chỉnh giao diện (Màu hồng pastel, hiệu ứng mượt mà)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .title-text {
        color: #d63384;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .message-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 18px;
        color: #4a4a4a;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #ff4b6e;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        background-color: #ff2a51;
        transform: scale(1.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Tiêu đề trang
st.markdown(
    "<h1 class='title-text'>🌸 Chúc Mừng Ngày 20/10 🌸</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: #6f42c1;'>Gửi những lời chúc tốt đẹp nhất đến một nửa thế giới!</h3>",
    unsafe_allow_html=True,
)

# Hiển thị hình ảnh hoặc icon hoa
st.markdown(
    "<p style='text-align: center; font-size: 60px;'>💐 🌷 🌹 🌻 🌺</p>",
    unsafe_allow_html=True,
)

# Phần thiệp chúc mừng
st.markdown(
    """
    <div class='message-box'>
        <h3>💌 Lời Chúc 20/10 💌</h3>
        <p>Nhân ngày Phụ nữ Việt Nam 20/10, xin gửi lời chúc chân thành và tốt đẹp nhất đến tất cả các chị em phụ nữ.</p>
        <p>Chúc bạn luôn luôn <b>tươi trẻ</b>, <b>xinh đẹp</b>, gặt hái được nhiều thành công trong công việc và lúc nào cũng ngập tràn niềm vui, hạnh phúc trong cuộc sống!</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Hộp quà bí mật tương tác
if "clicked" not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    if st.button("🎁 Nhận Quà Ngay Nhé!"):
        st.session_state.clicked = True
        st.rerun()
else:
    st.balloons()  # Hiệu ứng bong bóng bay cực kỳ sinh động trên Streamlit
    st.success(
        "🎉 Chúc mừng bạn đã nhận được một bầu trời bình an, một biển tình yêu và một gia đình luôn hạnh phúc! 💖"
    )
    if st.button("🔄 Gửi lại lời chúc"):
        st.session_state.clicked = False
        st.rerun()