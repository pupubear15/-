import streamlit as st
import random

# 1. 頁面基本設定
st.set_page_config(page_title="日文單字練習", page_icon="🇯🇵")

# 2. 題庫資料 (確保格式正確)
word_library = {
    "基礎名詞": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
        {"kanji": "犬", "kana": "いぬ", "romaji": "inu", "english": "狗"},
        {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶"},
        {"kanji": "先生", "kana": "せんせい", "romaji": "sensei", "english": "老師"}
    ],
    "基礎動詞": [
        {"kanji": "食べる", "kana": "たべる", "romaji": "taberu", "english": "吃"},
        {"kanji": "飲む", "kana": "のむ", "romaji": "nomu", "english": "喝"},
        {"kanji": "寝る", "kana": "ねる", "romaji": "neru", "english": "睡覺"},
        {"kanji": "勉強", "kana": "べんきょう", "romaji": "benkyou", "english": "學習"}
    ]
}

# 3. 初始化狀態 (Session State)
if 'score' not in st.session_state:
    st.session_state.score = 0

# 側邊欄選擇分類
category = st.sidebar.selectbox("選擇題庫", list(word_library.keys()))
current_pool = word_library[category]

# 檢查是否需要更換題目
if 'current_word' not in st.session_state or st.session_state.get('last_cat') != category:
    st.session_state.current_word = random.choice(current_pool)
    st.session_state.last_cat = category
    st.session_state.feedback = None

# 4. 主介面顯示
st.title("🇯🇵 日文單字練習")
word = st.session_state.current_word

st.subheader(f"題目： {word['kanji']}")

# 5. 輸入區域 (使用 Form)
with st.form(key='my_form', clear_on_submit=True):
    user_input = st.text_input("輸入平假名或中文：")
    submit = st.form_submit_button("送出答案")

if submit:
    ans = user_input.strip()
    if ans == word['kana'] or ans == word['english']:
        st.session_state.feedback = f"✅ 正確！答案是：{word['kana']} ({word['english']})"
        st.session_state.score += 1
    else:
        st.session_state.feedback = f"❌ 錯誤！正確答案是：{word['kana']} ({word['english']})"

# 顯示回饋訊息
if st.session_state.feedback:
    st.info(st.session_state.feedback)

# 6. 功能按鈕
col1, col2 = st.columns(2)
with col1:
    if st.button("下一題 ➡️"):
        st.session_state.current_word = random.choice(current_pool)
        st.session_state.feedback = None
        st.rerun()
with col2:
    if st.button("重設分數 🔄"):
        st.session_state.score = 0
        st.rerun()

# 側邊欄狀態
st.sidebar.divider()
st.sidebar.write(f"目前分數：{st.session_state.score}")
with st.sidebar.expander("💡 提示"):
    st.write(f"拼音：{word['romaji']}")
