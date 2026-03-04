import streamlit as st
import random
import streamlit.components.v1 as components

# 1. 頁面設定
st.set_page_config(page_title="N2 日文口說挑戰", page_icon="🎓", layout="wide")

# 2. 核心題庫：區分 N2 考點與生活對話
word_library = {
    "JLPT N2 高頻單字": [
        {"kanji": "深刻", "kana": "しんこく", "romaji": "shinkoku", "english": "嚴重的/深刻的", "desc": "問題が深刻化する (問題變得嚴重)"},
        {"kanji": "範囲", "kana": "はんい", "romaji": "han'i", "english": "範圍", "desc": "試験の範囲を確認する (確認考試範圍)"},
        {"kanji": "慎重", "kana": "しんちょう", "romaji": "shinchou", "english": "慎重的", "desc": "慎重に検討する (慎重考慮)"},
        {"kanji": "契機", "kana": "けいき", "romaji": "keiki", "english": "契機/轉機", "desc": "これを契機に改善する (以此為契機進行改善)"},
        {"kanji": "普及", "kana": "ふきゅう", "romaji": "fukyuu", "english": "普及", "desc": "スマホが急速に普及した (手機迅速普及)"}
    ],
    "生活情境對話": [
        {"kanji": "お会計お願いします", "kana": "おかいけいおねがいします", "romaji": "o kaikei onegaishimasu", "english": "麻煩買單", "desc": "餐廳結帳常用語"},
        {"kanji": "お口に合いますか", "kana": "おくちにあいますか", "romaji": "o kuchi ni aimasu ka", "english": "合胃口嗎？", "desc": "招待客人吃飯時的客套話"},
        {"kanji": "ちょっとよろしいですか", "kana": "ちょっとよろしいですか", "romaji": "chotto yoroshi
