import streamlit as st
import random
import streamlit.components.v1 as components

# 1. 頁面設定
st.set_page_config(page_title="N2 & 生活日語口說", page_icon="🎓")

# 2. 核心題庫 (確保每行完整閉合)
word_library = {
    "JLPT N2 高頻單字": [
        {"kanji": "深刻", "kana": "しんこく", "romaji": "shinkoku", "english": "嚴重的", "desc": "問題が深刻化する"},
        {"kanji": "範圍", "kana": "はんい", "romaji": "han'i", "english": "範圍", "desc": "試験の範囲を確認する"},
        {"kanji": "慎重", "kana": "しんちょう", "romaji": "shinchou", "english": "慎重的", "desc": "慎重に検討する"},
        {"kanji": "契機", "kana": "けいき", "romaji": "keiki", "english": "契機", "desc": "これを契機に改善する"},
        {"kanji": "普及", "kana": "ふきゅう", "romaji": "fukyuu", "english": "普及", "desc": "スマホが急速に普及した"}
    ],
    "生活情境對話": [
        {"kanji": "お会計お願いします", "kana": "おかいけいおねがいします", "romaji": "kaikei", "english": "麻煩結帳", "desc": "餐廳買單常用語"},
        {"kanji": "お口に合いますか", "kana": "おくちにあいますか", "romaji": "kuchi", "english": "合胃口嗎", "desc": "招待客人用餐"},
        {"kanji": "よろしいですか", "kana": "よろしいですか", "romaji": "yoroshii", "english": "方便嗎", "desc": "找人說話前的開場"},
        {"kanji": "お疲れ様です", "kana": "おつかれさまです", "romaji": "otsukare", "english": "辛苦了", "desc": "職場萬用問候"}
    ],
    "N2 文法慣用語": [
        {"kanji": "際して", "kana": "さいして", "romaji": "saishite", "english": "當...之際", "desc": "N2文法：表示特殊時機"},
        {"kanji": "せっかく", "kana": "せっかく", "romaji": "sekkaku", "english": "好不容易", "desc": "せっかく来たのに"},
        {"kanji": "あいにく", "kana": "あいにく", "romaji": "ainiku", "english": "不湊巧", "desc": "あいにく外出中です"}
    ]
}

# 3. 初始化 Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# 側邊欄設定
st.sidebar.title("📚 學習面板")
category = st.sidebar.selectbox("選擇學習內容", list(word_library.keys()))
current_pool = word_library[category]

# 分類切換邏輯
if 'current_word' not in st.session_state or st.session_state.get('last_cat') != category:
    st.session_state.current_word = random.choice(current_pool)
    st.session_state.last_cat = category
    st.session_state.feedback = None

# 4. 語音播放 JavaScript
def speak_js(text):
    js = f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='ja-JP';u.rate=0.8;window.speechSynthesis.speak(u);</script>"
    components.html(js, height=0)

# 5. 主介面設計
st.title("🎓 N2 & 生活日語挑戰")
word = st.session_state.current_word

# 題目呈現
st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 25px; border-radius: 10px; border-left: 5px solid #FF4B4B;">
        <h3 style="color: #555; margin:0;">{category}</h3>
        <h1 style="font-size: 50px; margin: 10px 0;">{word['kanji']}</h1>
        <p style="color: #666; font-style: italic;">用法提示：{word['desc']}</p>
    </div>
""", unsafe_allow_html=True)

# 答題區
with st.form(key='study_form', clear_on_submit=True):
    user_input = st.text_input("輸入平假名 (例如: しんこく)：")
    submit = st.form_submit_button("提交答案並聽發音")

if submit:
    speak_js(word['kana'])
    if user_input.strip() == word['kana']:
        st.session_state.feedback = ("success", f"🎯 正確！{word['kana']}")
        st.session_state.score += 1
    else:
        st.session_state.feedback = ("error", f"❌ 錯誤！正確讀音是：{word['kana']}")

# 顯示回饋
if st.session_state.get('feedback'):
    ftype, fmsg = st.session_state.feedback
    if ftype == "success": st.success(fmsg)
    else: st.error(fmsg)

# 按鈕控制
c1, c2 = st.columns(2)
with c1:
    if st.button("下一題 ➡️", use_container_width=True):
        st.session_state.current_word = random.choice(current_pool)
        st.session_state.feedback = None
        st.rerun()
with c2:
    if st.button("🔊 重聽發音", use_container_width=True):
        speak_js(word['kana'])

# 側邊欄顯示分數
st.
