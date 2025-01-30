import random


def amiralBatti():
    # 5x5 tahtayı oluşturalım
    gemi_satir = random.randint(1, 5)
    gemi_sutun = random.randint(1, 5)
    TahminHakki = 5
    print("\n--------------------------------------------\n")
    print("Amiral Battı Oyununa Hoş Geldiniz!")
    print("Tahta 5x5 boyutunda ve 1-5 arasında bir satır ve sütun seçmelisiniz.")
    print("Toplam 5 tahmin hakkınız var. Başarılar!\n")
    print("\n--------------------------------------------\n")
    # hataları daha kolay tespit edebilmek için try except metodu kullandım
    while TahminHakki > 0:
        try:

            satir = int(input("Satır sayını tahmin ediniz (1-5): "))
            sutun = int(input("Sütun sayını tahmin ediniz (1-5):"))

            if satir == gemi_satir and sutun == gemi_sutun:
                print("Tebrikler, gemiyi vurdunuz! Oyunu KAZANDINIZ!")
                return True  # Başarıyla ilk seviyeyi geçti
            else:
                TahminHakki -= 1
                if TahminHakki > 0:
                    print(f"Yanlış tahmin, tekrar deneyin! Kalan hakkınız: {TahminHakki}")
                else:
                    print("Tahmin hakkınız kalmadı. Oyunu KAYBETTİNİZ!")
                    print(f"Gemi {gemi_satir}. satır ve {gemi_sutun}. sütunda idi.")
                    return False  # Oyun kaybedildi

        except ValueError:
            print("Lütfen geçerli bir sayı girin!")


def amiralBatti_level2():
    # İkinci seviyede iki gemi olacak
    gemi_satir1 = random.randint(1, 5)
    gemi_sutun1 = random.randint(1, 5)
    gemi_satir2 = random.randint(1, 5)
    gemi_sutun2 = random.randint(1, 5)
    print("\n--------------------------------------------\n")
    print("İkinci seviyeye geçtiniz. Bu seviyede iki gemi bulacaksınız. DİKKATLİ OLMALISIN!")
    print("\n--------------------------------------------\n")

    gemi1_bulundu = False
    gemi2_bulundu = False
    TahminHakki = 100  # Bu seviyede hak sınırı yok

    while not (gemi1_bulundu and gemi2_bulundu):
        try:
            satir = int(input("Satır sayını tahmin ediniz (1-5): "))
            sutun = int(input("Sütun sayını tahmin ediniz (1-5):"))

            if satir == gemi_satir1 and sutun == gemi_sutun1:
                print("Tebrikler, birinci gemiyi vurdunuz!")
                gemi1_bulundu = True
            elif satir == gemi_satir2 and sutun == gemi_sutun2:
                print("Tebrikler, ikinci gemiyi vurdunuz!")
                gemi2_bulundu = True
            else:
                print("Yanlış tahmin, tekrar deneyin!")

            # Pes etme durumu
            pes_et = input("Pes etmek istiyor musunuz? (evet/hayır): ").lower()
            if pes_et == "evet":
                print(f"Birinci gemi {gemi_satir1}. satır ve {gemi_sutun1}. sütunda idi.")
                print(f"İkinci gemi {gemi_satir2}. satır ve {gemi_sutun2}. sütunda idi.")
                print("Oyunu KAYBETTİNİZ!")
                break

        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

    if gemi1_bulundu and gemi2_bulundu:
        print("Tebrikler, ikinci leveli geçtiniz! Oyunun GALİBİSİNİZ!")


def amiralBatti_sonuç():
    if amiralBatti():
        amiralBatti_level2()


amiralBatti_sonuç()

