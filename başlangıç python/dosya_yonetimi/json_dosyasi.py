import json

def json_olustur():
    veri = {
        "Isim": "SENA",
        "Yas": 21,
        "Sehir": "ANKARA"
    }

    with open("veri.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, indent=4, ensure_ascii=False)

    print("veri.json dosyası oluşturuldu ve veri kaydedildi.")


def json_oku():
    try:
        with open("veri.json", "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)
            print("Dosyadaki Veri:", veri)
            return veri
    except FileNotFoundError:
        print("Hata: veri.json dosyası bulunamadı.")
        return None


def json_guncelle():
    veri = json_oku()

    if veri:
        yeni_sehir = input("Yeni şehir adı girin: ")
        yeni_isim = input("Yeni isim giriniz.")



        veri["Sehir"] = yeni_sehir
        veri["Isim"]=yeni_isim


        with open("veri.json", "w", encoding="utf-8") as dosya:
            json.dump(veri, dosya, indent=4, ensure_ascii=False)

        print("JSON dosyası güncellendi!")


# Program Çalıştırma
json_olustur()
json_oku()
json_guncelle()
json_oku()
