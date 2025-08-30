import streamlit as st
import random

# ----- Özel CSS -----
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.ibb.co/MCh8mM6/forest.jpg');
        background-size: cover;
        background-attachment: fixed;
    }

    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 5px #000000;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.05);}
        100% {transform: scale(1);}
    }

    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- Başlık -----
st.title("🌍 Gelecek Dünya Simülasyonu")
st.write("Seçimlerin geleceği nasıl değiştirecek?")

# ----- Sorular -----
beslenme = st.radio("🥗 Daha çok ne yersin?", ["et", "sebze"])
ulasim = st.radio("🚗 Daha çok nasıl ulaşım sağlarsın?", ["araba", "bisiklet", "toplu taşıma", "yürüyüş"])
enerji = st.radio("⚡ Enerjinin çoğu nereden geliyor?", ["yenilenebilir", "fosil"])

if st.button("🔮 Geleceği Gör"):
    gelecek = []

    # Beslenme
    if beslenme == "et":
        gelecek.append("🌡️ 2070’te inekler insanlardan fazla ve saldıkları metan yüzünden dünya dev bir fırın gibi ısınıyor.")
    elif beslenme == "sebze":
        gelecek.append("🥦 2070’te sebzeler dünyayı ele geçiriyor ve brokoli para birimi oluyor.")

    # Ulaşım
    if ulasim == "araba":
        gelecek.append("🚦 Trafik sıkışıklığı artık kıtalar arası, ama uçan arabalar biraz olsun eğlenceli.")
    elif ulasim == "bisiklet":
        gelecek.append("🚴 2100’de insanların bacakları süper güçlü ve 'Dünya Turu' en büyük spor etkinliği.")
    elif ulasim == "toplu taşıma":
        gelecek.append("🚌 Toplu taşıma o kadar gelişti ki ışınlanan otobüsler sıradan hale geldi.")
    elif ulasim == "yürüyüş":
        gelecek.append("👟 İnsanlar o kadar yürüyor ki şehirler dev yürüyen kaldırımlarla birbirine bağlanıyor.")

    # Enerji
    if enerji == "yenilenebilir":
        gelecek.append("🔋 Güneş ağaçları tüm şehirleri besliyor ve gece gökyüzü yeşil ışıklarla parlıyor.")
    elif enerji == "fosil":
        gelecek.append("💨 Hava o kadar kirli ki insanlar gün batımını görmek için canlı yayın izliyor.")

    # Rastgele eğlenceli ek
    ekstra = random.choice([
        "🐧 Penguenler Antarktika’da bağımsızlık ilan etti ve kendi krallıklarını kurdu.",
        "🤖 Robotlar yosun yetiştirip hem yakıt üretiyor hem de yemek programı sunuyor.",
        "🐉 Dumanlardan oluşan bir ejderha gökyüzünde dolaşıyor ama şaşırtıcı şekilde dost canlısı.",
        "🌌 İnsanlar Mars’a taşındı ama hâlâ WiFi’den şikayet ediyor.",
        "🐠 Denizlerin altında dev şehirler kuruldu ve balıklarla birlikte yaşıyoruz."
    ])
    gelecek.append(ekstra)

    # ----- Sonuç Göster -----
    st.subheader("✨ Senin Gelecek Dünya Senaryon ✨")
    for satir in gelecek:
        st.write(" - " + satir)


