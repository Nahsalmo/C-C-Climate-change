import random

def gelecek_dunya():
    print("🌍 Gelecek Dünya Üreticisine Hoş Geldin!")
    print("Birkaç soruya cevap ver, sana gelecekte dünyanın nasıl görüneceğini anlatayım...\n")

    # Sorular
    beslenme = input("🥗 Daha çok ne yersin? (et / sebze): ").strip().lower()
    ulasim = input("🚗 Daha çok nasıl ulaşım sağlarsın? (araba / bisiklet / toplu taşıma / yürüyüş): ").strip().lower()
    enerji = input("⚡ Enerjinin çoğu nereden geliyor? (yenilenebilir / fosil): ").strip().lower()

    # Olası senaryolar
    gelecek = []

    if beslenme == "et":
        gelecek.append("🌡️ 2070’te inekler insanlardan fazla ve saldıkları metan yüzünden dünya dev bir fırın gibi ısınıyor.")
    elif beslenme == "sebze":
        gelecek.append("🥦 2070’te sebzeler dünyayı ele geçiriyor ve brokoli para birimi oluyor.")

    if "araba" in ulasim:
        gelecek.append("🚦 Trafik sıkışıklığı artık kıtalar arası, ama uçan arabalar biraz olsun eğlenceli.")
    elif "bisiklet" in ulasim:
        gelecek.append("🚴 2100’de insanların bacakları süper güçlü ve 'Dünya Turu' en büyük spor etkinliği.")
    elif "toplu" in ulasim:
        gelecek.append("🚌 Toplu taşıma o kadar gelişti ki ışınlanan otobüsler sıradan hale geldi.")
    elif "yürüyüş" in ulasim:
        gelecek.append("👟 İnsanlar o kadar yürüyor ki şehirler dev yürüyen kaldırımlarla birbirine bağlanıyor.")

    if "yenilenebilir" in enerji:
        gelecek.append("🔋 Güneş ağaçları tüm şehirleri besliyor ve gece gökyüzü yeşil ışıklarla parlıyor.")
    elif "fosil" in enerji:
        gelecek.append("💨 Hava o kadar kirli ki insanlar gün batımını görmek için canlı yayın izliyor.")

    # Rastgele eğlenceli bir ekleme
    ekstra = random.choice([
        "🐧 Penguenler Antarktika’da bağımsızlık ilan etti ve kendi krallıklarını kurdu.",
        "🤖 Robotlar yosun yetiştirip hem yakıt üretiyor hem de yemek programı sunuyor.",
        "🐉 Dumanlardan oluşan bir ejderha gökyüzünde dolaşıyor ama şaşırtıcı şekilde dost canlısı.",
        "🌌 İnsanlar Mars’a taşındı ama hâlâ WiFi’den şikayet ediyor."
    ])
    gelecek.append(ekstra)

    # Sonuç
    print("\n✨ Senin Gelecek Dünya Senaryon ✨")
    for satir in gelecek:
        print(" - " + satir)

if __name__ == "__main__":
    gelecek_dunya()
