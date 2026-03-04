import streamlit as st
import random

# 設定頁面資訊
st.set_page_config(page_title="日文學習小助手", page_icon="🇯🇵")

# --- 題庫擴充區 ---
# 你可以隨時在這裡增加大括號 {} 來添加新單字
word_library = {
    "基礎名詞 (N5)": [
        {"kanji": "猫", "kana": "ねこ", "romaji": "neko", "english": "貓"},
        {"kanji": "犬", "kana": "いぬ", "romaji": "inu", "english": "狗"},
        {"kanji": "時計", "kana": "とけい", "romaji": "tokei", "english": "手錶/時鐘"},
        {"kanji": "電話", "kana": "でんわ", "romaji": "denwa", "english": "電話"},
        {"kanji": "机", "kana": "つくえ", "romaji": "tsukue", "english": "桌子"},
        {"kanji": "椅子", "kana": "いす", "romaji": "isu", "english": "椅子"},
        {"kanji": "先生", "kana": "せんせい", "romaji": "sensei", "english": "老師"},
        {"kanji": "学生", "kana": "がくせい", "romaji": "gakusei", "english": "學生"},
        {"kanji": "友達", "kana": "ともだち", "romaji": "tomodachi", "english": "朋友"},
        {"kanji": "家族", "kana": "かぞく", "romaji": "kazoku", "english": "家人"},
    ],
    "食物與生活": [
        {"kanji": "美味しい", "kana": "おいしい", "romaji": "oishii", "english": "好吃"},
        {"kanji": "朝ご飯", "kana": "あさごはん", "romaji": "asagohan", "english": "早餐"},
        {"kanji": "水", "kana": "みず", "romaji": "mizu", "english": "水"},
        {"kanji": "お茶", "kana": "おちゃ", "romaji": "ocha", "english": "茶"},
        {"kanji": "林檎", "kana": "りんご", "romaji": "ringo", "english": "蘋果"},
        {"kanji": "卵", "kana": "たまご", "romaji": "tamago", "english": "雞蛋"},
    ],
    "實用動詞": [
        {"kanji": "勉強", "kana": "べんきょう", "romaji": "benkyou", "english": "學習"},
        {"kanji": "食べる", "kana": "たべる", "romaji": "taberu", "english": "吃"},
        {"kanji": "飲む", "kana": "のむ", "romaji": "nomu", "english": "喝"},
        {"kanji": "行く", "kana": "いく", "romaji": "iku", "english": "去"},
        {"kanji": "来る", "kana": "くる", "romaji": "kuru", "english": "來"},
        {"kanji": "寝る", "kana": "ねる", "romaji": "neru", "english":
