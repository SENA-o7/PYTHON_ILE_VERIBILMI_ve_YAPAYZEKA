class Ogrenci:
        def __init__(self, ad, sinif, notlar):
            self.ad = ad
            self.sinif = sinif
            self.notlar = notlar

        def ortalama_hesapla(self):
            if not self.notlar:
                return "Hesap yapılabilecek bir not yok!"
            return sum(self.notlar) / len(self.notlar)

        def bilgileri_goster(self):
          print(f"Ad: {self.ad}\n",f"Sınıf: {self.sinif}\n",f"Notlar: {self.notlar}\n",f"Ortalama Not: {self.ortalama_hesapla()}\n")



ogrenci1=Ogrenci("Sare Maraz","8C",[89,65,100])
ogrenci2=Ogrenci("Sinan Yılmaz","8C",[80,70,87])
ogrenci3=Ogrenci("Selin Kara","8C",[93,100,34])
ogrenci4=Ogrenci("Samet Öz","8C",[68,100,100])

ogrenciler=[]
ogrenciler.append(ogrenci1)
ogrenciler.append(ogrenci2)
ogrenciler.append(ogrenci3)
ogrenciler.append(ogrenci4)
for ogrenci in ogrenciler:
    ogrenci.bilgileri_goster()

