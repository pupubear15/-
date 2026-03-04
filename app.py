import streamlit as st
import random
import streamlit.components.v1 as components

# 1. 頁面基礎設定
st.set_page_config(page_title="MOJI 模擬練習器", page_icon="📖")

# 2. 模擬 MOJI 辭典 N2 數據庫 (擴充內容)
word_library = {
    "N2 高頻單字 (MOJI 精選)": [
        {"q": "妥協", "a": "だきょう", "m": "妥協", "d": "互いに妥協点を見出す"},
        {"q": "克服", "a": "こくふく", "m": "克服", "d": "困難を克服して進む"},
        {"q": "反映", "a": "はんえい", "m": "反映", "d": "世論を政治に反映させる"},
        {"q": "貢献", "a": "こうけん", "m": "貢獻", "d": "社会に貢献する"},
        {"q": "維持", "a": "いじ", "m": "維持", "d": "現状を維持する"},
        {"q": "考慮", "a": "こうりょ", "m": "考慮", "d": "周囲の状況を考慮する"}
    ],
    "生活對話 (情境式)": [
        {"q": "お邪魔します", "a": "おじゃまします", "m": "打擾了", "d": "進入別人家中時的禮貌用語"},
        {"q": "お先に失礼します", "a": "おさきにしつれいします", "m": "我先走了", "d": "下班或先離開時"},
        {"q": "お世話になっております", "a": "おせわになっております", "m": "承蒙照顧", "d": "商務對話開頭"},
        {"q": "確認させていただきます", "a": "かくにんさせていただきます", "m": "請容我確認一下", "d": "職場正式表達"}
    ],
    "N2 核心文法辨析": [
        {"q": "～をめぐって", "a": "をめぐって", "m": "圍繞著...", "d": "環境問題をめぐって議論する"},
        {"q": "～に反して", "a": "にはんして", "m": "與...相反", "d": "予想に反して結果は良かった"},
        {"q": "～に基づき", "a": "にもとづき", "m": "根據...", "d": "法律に基づき判決を下す"}
    ]
}

# 3. 初始化 Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0

# 側邊欄分類選擇
st.sidebar.title("📑 MOJI 題庫分類")
cat = st.sidebar.selectbox("切換等級/情境", list(word_library.keys()))
pool = word_library[cat]

# 換題邏輯
if 'word' not in st.session_state or st.session_state.get('curr_cat') != cat:
    st.session_state.word = random.choice(pool)
    st.session_state.curr_cat = cat
    st.session_state.result = None

# 4. TTS 語音播放功能
def play_sound(text):
    js = f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='ja-JP';u.rate=0.85;window.speechSynthesis.speak(u);</script>"
    components.html(js, height=0)

# 5. 主畫面設計
st.title("📖 MOJI 日語學習助手")
curr = st.session_state.word

# 模擬辭典卡片介面
st.markdown(f"""
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #ddd; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
        <span style="color: #ed4337; font-weight: bold; border: 1px solid #ed4337; padding: 2px 5px; border-radius: 3px;">{cat[:2]}</span>
        <h1 style="color: #333; margin: 10px 0;">{curr['q']}</h1>
        <p style="color: #666; font-size: 18px;">💡 例句：{curr['d']}</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# 答題 Form
with st.form(key='answer_box', clear_on_submit=True):
    user_input = st.text_input("輸入平假名：", placeholder="請在此輸入...")
    submit = st.form_submit_button("送出檢查")

if submit:
    play_sound(curr['a'])
    st.session_state.total += 1
    if user_input.strip() == curr['a']:
        st.session_state.result = ("success", f"🎯 正確！讀音：{curr['a']}")
        st.session_state.score += 1
    else:
        st.session_state.result = ("error", f"❌ 錯誤！正確讀音是：{curr['a']}")

# 顯示回饋
if st.session_state.result:
    rtype, rmsg = st.session_state.result
    if rtype == "success": st.success(rmsg)
    else: st.error(rmsg)

# 功能按鈕
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("下一題 ➡️", use_container_width=True):
        st.session_state.word = random.choice(pool)
        st.session_state.result = None
        st.rerun()
with c2:
    if st.button("🔊 重聽發音", use_container_width=True):
        play_sound(curr['a'])
with c3:
    if st.button("🔄 分數重置", use_container_width=True):
        st.session_state.score = 0
        st.session_state.total = 0
        st.rerun()

# 側邊欄數據看板
st.sidebar.divider()
st.sidebar.subheader("📊 學習統計")
st.sidebar.write(f"正確數：{st.session_state.score}")
st.sidebar.write(f"總題數：{st.session_state.total}")
if st.session_state.total > 0:
    rate = (st.session_state.score / st.session_state.total) * 100
    st.sidebar.progress(rate / 100)
    st.sidebar.write(f"正確率：{rate:.1f}%")

with st.sidebar.expander("📝 詳細釋義"):
    st.write(f"**中文意思：** {curr['m']}")
