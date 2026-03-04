import streamlit as st
import random

# 1. 頁面基礎設定
st.set_page_config(page_title="日文單字達人", page_icon="🇯🇵", layout="centered")

# 2. 擴充題庫 (確保括號完全閉合)
word_library = {
    "基礎名詞 (N5)": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
        {"kanji": "犬", "kana": "いぬ", "romaji": "inu", "english": "狗"},
        {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶"},
        {"kanji": "電話", "kana": "でんわ", "romaji": "denwa", "english": "電話"},
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

# 側邊欄選擇分類
st.sidebar.title("⚙️ 學習設定")
category = st.sidebar.selectbox("選擇題庫範圍", list(word_library.keys()))
current_pool = word_library[category]

# 如果換了分類或還沒初始化題目
if 'current_category' not in st.session_state or st.session_state.current_category != category:
    st.session_state.current_category =
