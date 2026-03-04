import streamlit as st
import random

# 設定頁面資訊
st.set_page_config(page_title="日文學習小助手", page_icon="🇯🇵")

# 準備單字資料
word_dict = [
    {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
    {"kanji": "美味しい", "kana": "おいしい", "romaji": "oishii", "english": "好吃"},
    {"kanji": "勉強", "kana": "べんきょう", "romaji": "benkyou", "english": "學習"},
    {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶/時鐘"},
    {"kanji": "朝ご飯", "kana": "あさごはん", "romaji": "asagohan", "english": "早餐"},
]

# 初始化 Session State
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(word_dict)
if 'score' not in st.session_state:
    st.session_state.score = 0

# 修正後的換題函式：移除對 st.session_state.user_answer 的直接賦值
def next_word():
    st.session_state.current_word = random.choice(word_dict)

# 介面設計
st.title("🇯🇵 日文單字挑戰賽")

# 顯示題目
word = st.session_state.current_word
st.subheader(f"題目： {word['kanji']}")

# 使用 Form 來處理輸入，這可以讓介面更穩定
with st.form(key='my_form', clear_on_submit=True):
    user_input = st.text_input("輸入對應的「平假名」或「中文」:")
    submit_button = st.form_submit_button(label='提交答案')

if submit_button:
    if user_input == word['kana'] or user_input == word['english']:
        st.success(f"🎉 正確！答案就是「{word['kana']}」")
        st.session_state.score += 1
    else:
        st.error(f"差一點點！正確答案是：{word['kana']} ({word['english']})")

# 下一題按鈕（獨立於 Form 之外）
if st.button("下一題 ➡️"):
    next_word()
    st.rerun()

# 側邊欄與提示
st.sidebar.metric("目前得分", st.session_state.score)

with st.expander("💡 偷看提示"):
    st.write(f"羅馬拼音：{word['romaji']}")
    st.write(f"中文：{word['english']}")
