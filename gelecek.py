import streamlit as st

st.set_page_config(page_title="İklim Geleceği Simülasyonu", layout="centered")

# ----- CSS -----
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/zWdxKQn/5.jpg");
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff;
    }

    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 2px 2px 5px #000000;
    }

    .result-card {
        background: rgba(0,0,0,0.65);
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0px 0px 10px #000000aa;
    }

    /* Floating donate image button */
    .donate-btn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
    }

    .donate-btn img {
        width: 120px;
        cursor: pointer;
        transition: transform 0.2s;
    }

    .donate-btn img:hover {
        transform: scale(1.1);
    }
    </style>

    <div class="donate-btn">
        <img src="https://cdn-icons-png.flaticon.com/512/1041/1041883.png" title="Donate for Climate 🌱"/>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🌍 İklim Geleceği Simülasyonu")
st.write("Seçimlerin iklim değişikliğini nasıl etkileyecek? 🔮")

# Skor tutucu
skor = 0

# ----- Sorular -----
beslenme = st.radio("🌱 Beslenme alışkanlıkların?", ["Et ağırlıklı", "Sebze ağırlıklı", "Vegan"])
if beslenme == "Et ağırlıklı": skor += 3
elif beslenme == "Sebze ağırlıklı": skor += 1
elif beslenme == "Vegan": skor += 0

ulasim = st.radio("🚗 Ulaşım tercihin?", ["Kişisel araç", "Toplu taşıma", "Bisiklet/Yürüyüş", "Elektrikli araç"])
if ulasim == "Kişisel araç": skor += 3
elif ulasim == "Toplu taşıma": skor += 2
elif ulasim == "Bisiklet/Yürüyüş": skor += 0
elif ulasim == "Elektrikli araç": skor += 1

enerji = st.radio("⚡ Enerji kaynağı?", ["Fosil yakıt", "Nükleer", "Yenilenebilir", "Karma"])
if enerji == "Fosil yakıt": skor += 3
elif enerji == "Nükleer": skor += 1
elif enerji == "Yenilenebilir": skor += 0
elif enerji == "Karma": skor += 2

sanayi = st.radio("🏭 Sanayi üretim biçimi?", ["Fosil yoğun", "Yeşil dönüşüm", "Döngüsel ekonomi"])
if sanayi == "Fosil yoğun": skor += 3
elif sanayi == "Yeşil dönüşüm": skor += 1
elif sanayi == "Döngüsel ekonomi": skor += 0

orman = st.radio("🌳 Orman ve arazi kullanımı?", ["Ormansızlaşma", "Kısmi koruma", "Tam koruma ve ağaçlandırma"])
if orman == "Ormansızlaşma": skor += 3
elif orman == "Kısmi koruma": skor += 1
elif orman == "Tam koruma ve ağaçlandırma": skor += 0

sehir = st.radio("🏘️ Şehir planlaması?", ["Otomobil odaklı", "Yeşil şehirler", "Karma"])
if sehir == "Otomobil odaklı": skor += 3
elif sehir == "Yeşil şehirler": skor += 0
elif sehir == "Karma": skor += 1

atik = st.radio("🚮 Atık yönetimi?", ["Çöp depolama", "Geri dönüşüm", "Sıfır atık"])
if atik == "Çöp depolama": skor += 3
elif atik == "Geri dönüşüm": skor += 1
elif atik == "Sıfır atık": skor += 0

tuketim = st.radio("📦 Tüketim alışkanlıkları?", ["Aşırı tüketim", "İhtiyaç kadar", "Minimalizm"])
if tuketim == "Aşırı tüketim": skor += 3
elif tuketim == "İhtiyaç kadar": skor += 1
elif tuketim == "Minimalizm": skor += 0

su = st.radio("💧 Su kullanımı?", ["Savurgan", "Orta", "Verimli"])
if su == "Savurgan": skor += 3
elif su == "Orta": skor += 1
elif su == "Verimli": skor += 0

politika = st.radio("🤝 Politika ve toplum hareketleri?", ["Umursamazlık", "Kısmi önlemler", "Küresel işbirliği"])
if politika == "Umursamazlık": skor += 3
elif politika == "Kısmi önlemler": skor += 1
elif politika == "Küresel işbirliği": skor += 0


# ----- Sonuç -----
if st.button("🔮 Geleceği Gör"):
    st.subheader("✨ Senin İklim Geleceği Senaryon ✨")

    # Virtual Earth health bar
    max_skor = 30
    health = max(0, max_skor - skor)
    percent = int((health / max_skor) * 100)
    st.progress(percent)

    if skor <= 7:
        st.markdown("<div class='result-card'>🌍 Dünya sürdürülebilir bir geleceğe doğru gidiyor! İklim değişikliği büyük oranda kontrol altına alındı.</div>", unsafe_allow_html=True)
    elif skor <= 15:
        st.markdown("<div class='result-card'>🌤️ Dünya bazı zorluklarla karşılaşıyor ama hâlâ yaşanabilir. Önlemler alındı fakat yetersiz.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-card'>🔥 Dünya iklim felaketiyle karşı karşıya! Deniz seviyeleri yükseldi, ekosistemler çöktü.</div>", unsafe_allow_html=True)

    st.write(f"🌡️ **Karbon Ayak İzi Skorun:** {skor} (0 = en iyi, 30 = en kötü)")
    st.write(f"💖 **Dünya Sağlık Durumu:** %{percent}")



