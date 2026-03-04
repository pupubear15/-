
import streamlit as st
import random

# 設定頁面資訊
st.set_page_config(page_title="日文學習小助手", page_icon="🇯🇵")

# 準備一些基礎單字資料 (你之後可以擴充這個清單)
word_dict = [
    {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
    {"kanji": "美味しい", "kana": "おいしい", "romaji": "oishii", "english": "好吃"},
    {"kanji": "勉強", "kana": "べんきょう", "romaji": "benkyou", "english": "學習"},
    {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶/時鐘"},
    {"kanji": "朝ご飯", "kana": "あさごはん", "romaji": "asagohan", "english": "早餐"},
]

# 初始化 Session State (確保重新整理時單字不會亂跳)
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(word_dict)
if 'score' not in st.session_state:
    st.session_state.score = 0

def next_word():
    st.session_state.current_word = random.choice(word_dict)
    st.session_state.user_answer = ""

# 介面設計
st.title("🇯🇵 日文單字挑戰賽")
st.write("請輸入對應的平假名或中文意思！")

# 顯示題目
word = st.session_state.current_word
st.subheader(f"題目： {word['kanji']}")

# 使用者輸入
user_input = st.text_input("輸入答案 (平假名或中文):", key="user_answer")

# 按鈕區
col1, col2 = st.columns(2)

with col1:
    if st.button("提交答案"):
        if user_input == word['kana'] or user_input == word['english']:
            st.success("🎉 正確！太棒了！")
            st.session_state.score += 1
        else:
            st.error(f"差一點點！正確答案是：{word['kana']} ({word['english']})")

with col2:
    if st.button("下一題"):
        next_word()
        st.rerun()

# 額外功能：顯示目前的得分
st.sidebar.metric("目前得分", st.session_state.score)

# 提示：如何唸這個字
with st.expander("💡 偷看提示"):
    st.write(f"羅馬拼音：{word['romaji']}")
    st.write(f"中文：{word['english']}")
