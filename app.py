import streamlit as st
import random
import streamlit.components.v1 as components

# 1. 頁面設定
st.set_page_config(page_title="日文學習助手", page_icon="🇯🇵")

# 2. 核心題庫 (確保每行簡短，防止截斷)
word_library = {
    "JLPT N2 高頻": [
        {"q": "深刻", "a": "しんこく", "m": "嚴重的", "d": "問題が深刻化する"},
        {"q": "範囲", "a": "はんい", "m": "範圍", "d": "試験の範囲を確認"},
        {"q": "慎重", "a": "しんちょう", "m": "慎重的", "d": "慎重に検討する"},
        {"q": "契機", "a": "けいき", "m": "契機", "d": "これを契機に改善"},
        {"q": "普及", "a": "ふきゅう", "m": "普及", "d": "スマホが急速に普及"}
    ],
    "生活情境": [
        {"q": "お会計お願いします", "a": "おかいけいおねがいします", "m": "買單", "d": "餐廳結帳常用"},
        {"q": "お口に合いますか", "a": "おくちにあいますか", "m": "合胃口嗎", "d": "招待客人用餐"},
        {"q": "お疲れ様です", "a": "おつかれさまです", "m": "辛苦了", "d": "職場萬用問候"}
    ]
}

# 3. 初始化 Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# 側邊欄
st.sidebar.title("📚 學習選項")
cat = st.sidebar.selectbox("選擇題庫", list(word_library.keys()))
pool = word_library[cat]

if 'word' not in st.session_state or st.session_state.get('last_cat') != cat:
    st.session_state.word = random.choice(pool)
    st.session_state.last_cat = cat
    st.session_state.ans_status = None

# 4. 語音功能
def play_voice(text):
    js = f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='ja-JP';u.rate=0.8;window.speechSynthesis.speak(u);</script>"
    components.html(js, height=0)

# 5. 主畫面
st.title("🎓 N2 & 生活日語")
curr = st.session_state.word

st.info(f"當前分類：{cat}")
st.subheader(f"題目：{curr['q']}")
st.write(f"💡 用法：{curr['d']}")

# 答題區
with st.form(key='my_form', clear_on_submit=True):
    user_in = st.text_input("輸入平假名：")
    btn_submit = st.form_submit_button("檢查答案")

if btn_submit:
    play_voice(curr['a'])
    if user_in.strip() == curr['a']:
        st.session_state.ans_status = ("ok", f"🎯 正確！{curr['a']}")
        st.session_state.score += 1
    else:
        st.session_state.ans_status = ("no", f"❌ 錯誤！正確是：{curr['a']}")

if st.session_state.ans_status:
    t, msg = st.session_state.ans_status
    if t == "ok": st.success(msg)
    else: st.error(msg)

# 按鈕區
c1, c2 = st.columns(2)
with c1:
    if st.button("下一題 ➡️", use_container_width=True):
        st.session_state.word = random.choice(pool)
        st.session_state.ans_status = None
        st.rerun()
with c2:
    if st.button("🔊 聽發音", use_container_width=True):
        play_voice(curr['a'])

st.sidebar.metric("目前分數", st.session_state.score)
with st.sidebar.expander("解說"):
    st.write(f"意思：{curr['m']}")
