import streamlit as st
import random

# --- CSS Arka plan ve panel
page_bg = """
<style>
.stApp {
  background-image: url("https://i.ibb.co/zWdxKQn/5.jpg");
  background-size: cover;
}
.panel {
  background-color: rgba(255,255,255,0.85);
  padding: 20px;
  border-radius: 15px;
  margin-bottom: 20px;
}
.donate-img {
  position: fixed;
  bottom: 10px;
  right: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- State
if "puan" not in st.session_state:
    st.session_state.puan = 100
if "step" not in st.session_state:
    st.session_state.step = 0
if "cevaplar" not in st.session_state:
    st.session_state.cevaplar = {}

# --- Kategoriler
kategoriler = [
    ("🚗 Ulaşım", {"Araba (fosil yakıt)": -10, "Elektrikli araç": +10, "Bisiklet": +15, "Toplu Taşıma": +5, "Yürüyüş": +15}),
    ("🥗 Beslenme", {"Aşırı et tüketimi": -15, "Dengeli": +5, "Vejetaryen": +10, "Vegan": +15}),
    ("⚡ Enerji", {"Kömür santrali": -15, "Doğalgaz": -5, "Yenilenebilir enerji": +15, "Nükleer enerji": +10}),
    ("💻 Teknoloji", {"Savunma sanayii": -10, "Yeşil teknoloji": +15, "Eğitim": +10, "Yapay zeka ile enerji tasarrufu": +10}),
    ("🏙️ Toplum", {"Tüketim odaklı": -10, "Geri dönüşüm kültürü": +10, "Paylaşım ekonomisi": +15}),
    ("🏭 Sanayi", {"Petrol ağırlıklı üretim": -15, "Yeşil üretim": +15, "Karbon yakalama teknolojisi": +10}),
    ("🌾 Tarım", {"Monokültür": -10, "Organik tarım": +15, "Agroekoloji": +10, "Dikey tarım": +10}),
    ("💧 Su Kaynakları", {"Aşırı sulama": -10, "Damla sulama": +10, "Geri dönüştürülmüş su": +15}),
    ("🗑️ Atık Yönetimi", {"Her şeyi çöpe at": -15, "Geri dönüşüm": +10, "Kompost": +15, "Sıfır atık": +20}),
    ("🌐 Uluslararası İşbirliği", {"Hiç işbirliği yok": -15, "Zayıf anlaşmalar": -5, "Paris Anlaşması": +10, "Küresel güçlü işbirliği": +20}),
]

# --- Rastgele olaylar
rastgele_olaylar = [
    ("🌋 Yanardağ patladı, atmosfer geçici olarak soğudu.", +5),
    ("📉 Ekonomi çöküyor, yenilenebilir yatırımlar durdu.", -10),
    ("🚀 Karbon yakalama cihazları yaygınlaştı.", +15),
    ("🏭 Kömür santralleri hızla artıyor.", -15),
    ("🌱 Küresel anlaşma imzalandı, emisyonlar azaldı.", +10),
]

# --- Quiz
quiz_sorular = [
    ("🌡️ Dünya’daki sera gazı emisyonlarının en büyük kaynağı nedir?", ["Tarım", "Enerji", "Moda"], "Enerji"),
    ("🌲 Ormanların kesilmesi hangi gazın artmasına neden olur?", ["Oksijen", "Karbondioksit", "Azot"], "Karbondioksit"),
    ("🌊 Küresel ısınmanın en belirgin etkilerinden biri nedir?", ["Deniz seviyesinin yükselmesi", "Yerçekiminin azalması", "Güneşin küçülmesi"], "Deniz seviyesinin yükselmesi"),
]

# --- Akış
with st.container():
    if st.session_state.step < len(kategoriler):
        kategori, secenekler = kategoriler[st.session_state.step]
        st.markdown(f'<div class="panel"><h3>{kategori}</h3></div>', unsafe_allow_html=True)
        cevap = st.radio("Seçimini yap:", list(secenekler.keys()), key=f"radio_{st.session_state.step}")
        if st.button("Onayla", key=f"btn_{st.session_state.step}"):
            st.session_state.cevaplar[kategori] = cevap
            st.session_state.puan += secenekler[cevap]

            # %30 ihtimalle rastgele olay
            if random.random() < 0.3:
                olay, etkisi = random.choice(rastgele_olaylar)
                st.warning(f"Rastgele Olay: {olay} ({etkisi:+} puan)")
                st.session_state.puan += etkisi

            st.session_state.step += 1
            st.experimental_rerun = lambda: None  # eski kullanım yerine boş lambda
            st.experimental_rerun()  # UI otomatik güncellenecek

    elif st.session_state.step < len(kategoriler) + len(quiz_sorular):
        quiz_index = st.session_state.step - len(kategoriler)
        soru, secenekler, dogru = quiz_sorular[quiz_index]
        st.markdown('<div class="panel"><h3>📖 Quiz</h3></div>', unsafe_allow_html=True)
        cevap = st.radio(soru, secenekler, key=f"quiz_{quiz_index}")
        if st.button("Cevabı Onayla", key=f"quizbtn_{quiz_index}"):
            if cevap == dogru:
                st.success("✅ Doğru! +10 puan")
                st.session_state.puan += 10
            else:
                st.error(f"❌ Yanlış! Doğru cevap: {dogru}")
            st.session_state.step += 1
            st.experimental_rerun = lambda: None
            st.experimental_rerun()

    else:
        st.markdown('<div class="panel"><h3>🌍 Nihai Sonuç</h3></div>', unsafe_allow_html=True)
        st.write(f"Toplam Puanın: {st.session_state.puan}")
        if st.session_state.puan >= 150:
            st.success("🌱 Gezegen sağlıklı ve sürdürülebilir bir geleceğe kavuştu! 🎉")
        elif st.session_state.puan >= 120:
            st.info("😊 Dünya iyileşiyor, ancak biraz daha çaba gerekiyor...")
        elif st.session_state.puan >= 100:
            st.warning("😐 Dünya krizlerle boğuşuyor ama hâlâ kurtarılabilir...")
        else:
            st.error("☠️ Dünya yaşanmaz hale geldi...")

# --- Bağış görseli
st.markdown(
    '<div class="donate-img"><img src="https://cdn-icons-png.flaticon.com/512/1047/1047711.png" width="120"></div>',
    unsafe_allow_html=True
)




