import streamlit as st
import random

# 1. 頁面基礎設定
st.set_page_config(page_title="日文單字達人", page_icon="🇯🇵")

# 2. 完整題庫
word_library = {
    "基礎名詞 (N5)": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
        {"kanji": "犬", "kana": "いぬ", "romaji": "inu", "english": "狗"},
        {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶"},
        {"kanji": "電話", "kana": " federal", "romaji": "denwa", "english": "電話"},
        {"kanji": "机", "kana": "つくえ", "romaji": "tsukue", "english": "桌子"},
        {"kanji": "椅子", "kana": "いす", "romaji": "isu", "english": "椅子"},
        {"kanji": "先生", "kana": "せんせい", "romaji": "sensei", "english": "老師"},
        {"kanji": "学生", "kana": "がくせい", "romaji": "gakusei", "english": "學生"},
        {"kanji": "友達", "kana": "ともだち", "romaji": "tomodachi", "english": "朋友"},
        {"kanji": "家族", "kana": "かぞく", "romaji": "kazoku", "english": "家人"}
    ],
    "實用動詞與形容詞": [
        {"kanji": "美味しい", "kana": "おいしい", "romaji": "oishii", "english": "好吃"},
        {"kanji": "食べる", "kana": "たべる", "romaji": "taberu", "english": "吃"},
        {"kanji": "飲む", "kana": "のむ", "romaji": "nomu", "english": "喝"},
        {"kanji": "行く", "kana": "いく", "romaji": "iku", "english": "去"},
        {"kanji": "来る", "kana": "くる", "romaji": "kuru", "english": "來"},
        {"kanji": "寝る", "kana": "ねる", "romaji": "neru", "english": "睡覺"},
        {"kanji": "勉強", "kana": "べんきょう", "romaji": "benkyou", "english": "學習"},
        {"kanji": "書く", "kana": "かく", "romaji": "kaku", "english": "寫"}
    ]
}

# 3. 初始化 Session State
if 'score' not in st.session_state:
    st.session_state.score = 0

# 側邊欄設定
st.sidebar.title("⚙️ 設定")
category = st.sidebar.selectbox("選擇題庫", list(word_library.keys()))
current_pool = word_library[category]

# 檢查分類是否切換，若切換則重置單字
if 'current_category' not in st.session_state or st.session_state.current_category != category:
    st.session_state.current_category = category
    st.session_state.current_word = random.choice(current_pool)
    st.session_state.feedback = None

# 定義下一題的函式
def next_question():
    st.session_state.current_word = random.choice(current_pool)
    st.session_state.feedback = None

# 4. 主介面
st.title("🇯🇵 日文單字練習")

# 取得目前單字
word = st.session_state.current_word

# 顯示題目卡片
st.info(f"目前分類：{category}")
st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{word['kanji']}</h1>", unsafe_allow_html=True)

# 5. 輸入與檢查 (使用 form 確保穩定性)
with st.form(key='q_form', clear_on_submit=True):
    user_input = st.text_input("輸入平假名或中文：")
    submitted = st.form_submit_button("檢查答案")

if submitted:
    ans = user_input.strip()
    if ans == word['kana'] or ans == word['english']:
        st.session_state.feedback = ("success", f"🎯 正確！答案是：{word['kana']} ({word['english']})")
        st.session_state.score += 1
    else:
        st.session_state.feedback = ("error", f"❌ 錯誤！正確答案是：{word['kana']} ({word['english']})")

# 顯示回饋
if st.session_state.get('feedback'):
    style, msg = st.session_state.feedback
    if style == "success":
        st.success(msg)
    else:
        st.error(msg)

# 6. 按鈕列
col1, col2 = st.columns(2)
with col1:
    if st.button("下一題 ➡️", use_container_width=True):
        next_question()
        st.
