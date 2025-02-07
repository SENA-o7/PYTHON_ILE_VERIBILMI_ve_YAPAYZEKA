def veri_kaydet():
    veri = input("Kaydetmek istediğiniz veriyi girin: ")

    with open("data.txt", "w", encoding="utf-8") as dosya:
        dosya.write(veri)

    print("Veri başarıyla data.txt dosyasına kaydedildi.")


def veri_oku():
    try:
        with open("data.txt", "r", encoding="utf-8") as dosya:
            veri = dosya.read()
            print("Dosyadaki Veri:", veri)
    except FileNotFoundError:
        print(" data.txt dosyası bulunamadı.")



veri_kaydet()
veri_oku()
