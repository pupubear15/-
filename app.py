import streamlit as st
import random
import streamlit.components.v1 as components

# 1. 頁面基礎設定
st.set_page_config(page_title="時雨風格-日文學習助手", page_icon="🌧️")

# 2. 整合「時雨之町」核心題庫 (N2 語法與近義詞)
word_library = {
    "N2 近義詞辨析 (時雨精選)": [
        {"q": "固い・硬い・堅い", "a": "かたい", "m": "硬/堅固", "d": "口が堅い (守口如瓶) / 守りが見硬い"},
        {"q": "覚める・冷める", "a": "さめる", "m": "醒來/冷卻", "d": "夢が覚める / 料理が冷める"},
        {"q": "早い・速い", "a": "はやい", "m": "早/快", "d": "朝が早い / 足が速い"},
        {"q": "易しい・優しい", "a": "やさしい", "m": "簡單/溫柔", "d": "問題が易しい / 性格が優しい"}
    ],
    "N2 核心助詞與接續": [
        {"q": "～ことだ", "a": "ことだ", "m": "應該/最好...", "d": "日本語が上手になりたければ、毎日話すことだ。"},
        {"q": "～おかげで", "a": "おかげで", "m": "多虧...", "d": "先生のおかげで、合格できました。"},
        {"q": "～せいで", "a": "せいで", "m": "都是因為...(負面)", "d": "雨のせいで、試合が中止になった。"},
        {"q": "～ばかりに", "a": "ばかりに", "m": "只因為...", "d": "嘘をついたばかりに、信用を失った。"}
    ],
    "生活常用慣用語": [
        {"q": "耳を貸す", "a": "みみをかす", "m": "聽從/肯聽...", "d": "彼は人の忠告に耳を貸さない。"},
        {"q": "口が軽い", "a": "くちがかるい", "m": "大嘴巴", "d": "彼女は口が軽いから、秘密は言えない。"},
        {"q": "手を焼く", "a": "てをやく", "m": "束手無策/棘手", "d": "いたずらな子供に手を焼く。"}
    ]
}

# 3. 初始化 Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0

# 側邊欄分類
st.sidebar.title("🍵 時雨之町語法庫")
cat = st.sidebar.selectbox("選擇主題", list(word_library.keys()))
pool = word_library[cat]

# 換題邏輯
if 'word' not in st.session_state or st.session_state.get('curr_cat') != cat:
    st.session_state.word = random.choice(pool)
    st.session_state.curr_cat = cat
    st.session_state.result = None

# 4. 語音播放 JavaScript
def play_sound(text):
    # 針對辨析題，只播放讀音部分
    js = f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='ja-JP';u.rate=0.85;window.speechSynthesis.speak(u);</script>"
    components.html(js, height=0)

# 5. 主畫面設計
st.title("🌧️ 日文學習助手 (時雨之町內容整合)")
curr = st.session_state.word

# 模擬時雨之町清爽的筆記介面
st.markdown(f"""
    <div style="background-color: #fdfdfd; padding: 25px; border-radius: 10px; border-top: 5px solid #5d9ab2; box-shadow: 0px 4px 6px rgba(0,0,0,0.05);">
        <h3 style="color: #5d9ab2; margin:0;">Topic: {cat}</h3>
        <h1 style="color: #333; margin: 15px 0; font-size: 40px;">{curr['q']}</h1>
        <p style="color: #555; font-size: 18px; line-height: 1.6;"><b>💡 時雨註解：</b><br>{curr['d']}</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# 答題 Form
with st.form(key='answer_box', clear_on_submit=True):
    user_input = st.text_input("請輸入正確讀音或假名：", placeholder="例如：さめる")
    submit = st.form_submit_button("送出檢查")

if submit:
    play_sound(curr['a'])
    st.session_state.total += 1
    if user_input.strip() == curr['a']:
        st.session_state.result = ("success", f"🎯 正確！讀音為：{curr['a']}")
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
    if st.button("🔊 聽範例音", use_container_width=True):
        play_sound(curr['a'])
with c3:
    if st.button("🔄 重置進度", use_container_width=True):
        st.session_state.score = 0
        st.session_state.total = 0
        st.rerun()

# 側邊欄：進度監控
st.sidebar.divider()
st.sidebar.subheader("📊 學習進度")
st.sidebar.write(f"正確：{st.session_state.score} / 總計：{st.session_state.total}")
if st.session_state.total > 0:
    rate = (st.session_state.score / st.session_state.total)
    st.sidebar.progress(rate)
    st.sidebar.write(f"達成率：{rate*100:.1f}%")

with st.sidebar.expander("📚 本題詳細釋義"):
    st.write(f"**中文意思：** {curr['m']}")
    st.write("建議前往 [時雨之町](https://www.sigure.tw) 搜尋相關語法獲得更詳細的圖解說明。")
