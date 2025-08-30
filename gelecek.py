import random
import streamlit as st

st.title("🌍 Gelecek Dünya Üreticisi")
st.write("Birkaç seçim yap, gelecekte dünyanın nasıl görüneceğini öğren! 🚀")

# Kullanıcı seçimleri
beslenme = st.selectbox("🥗 Daha çok ne yersin?", ["Seç...", "Et", "Sebze"])
ulasim = st.selectbox("🚗 Ulaşımı nasıl tercih edersin?", ["Seç...", "Araba", "Bisiklet", "Toplu taşıma", "Yürüyüş"])
enerji = st.selectbox("⚡ Enerji kaynağın daha çok hangisi?", ["Seç...", "Yenilenebilir", "Fosil"])

if st.button("🔮 Geleceği Gör"):
    gelecek = []

    if beslenme == "Et":
        gelecek.append("🌡️ 2070’te inekler insanlardan fazla ve dünya dev bir fırın gibi ısınıyor.")
    elif beslenme == "Sebze":
        gelecek.append("🥦 2070’te sebzeler dünyayı ele geçiriyor ve brokoli para birimi oluyor.")

    if ulasim == "Araba":
        gelecek.append("🚦 Trafik artık kıtalar arası, ama uçan arabalar biraz olsun eğlenceli.")
    elif ulasim == "Bisiklet":
        gelecek.append("🚴 2100’de insanların bacakları süper güçlü ve 'Dünya Turu' en büyük spor etkinliği.")
    elif ulasim == "Toplu taşıma":
        gelecek.append("🚌 Işınlanan otobüsler sıradan hale geldi.")
    elif ulasim == "Yürüyüş":
        gelecek.append("👟 İnsanlar o kadar yürüyor ki şehirler dev yürüyen kaldırımlarla bağlanıyor.")

    if enerji == "Yenilenebilir":
        gelecek.append("🔋 Güneş ağaçları tüm şehirleri besliyor ve gece gökyüzü yeşil ışıklarla parlıyor.")
    elif enerji == "Fosil":
        gelecek.append("💨 Hava o kadar kirli ki gün batımı izlemek için canlı yayın açılıyor.")

    ekstra = random.choice([
        "🐧 Penguenler Antarktika’da bağımsızlık ilan etti.",
        "🤖 Robotlar yosun yetiştirip yemek programı sunuyor.",
        "🐉 Dumanlardan oluşan bir ejderha gökyüzünde dolaşıyor ama dost canlısı.",
        "🌌 İnsanlar Mars’a taşındı ama hâlâ WiFi’den şikayet ediyor."
    ])
    gelecek.append(ekstra)

    st.subheader("✨ Senin Gelecek Dünya Senaryon ✨")
    for satir in gelecek:
        st.write("- " + satir)
