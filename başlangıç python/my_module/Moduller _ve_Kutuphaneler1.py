import math


def HesapMakinesi():
    print("-------Matematiksel Hesap Makinesi-------")
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Üstel")
    print("6.Karekök")
    print("7.10 Tabanında Logaritma")
    print("8.Sinüs")
    print("9.Kosinüs")
    print("10.Tanjant")

    secim = input("1 ile 10 arasında bir sayı giriniz ve işlem başlasın: ")

    if secim in ['1', '2', '3', '4', '5']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        if secim == '1':
            print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == '2':
            print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 + sayi2}")
        elif secim == '3':
            print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 + sayi2}")
        elif secim == '4':
            if sayi2 != 0:
                print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 + sayi2}")
            else:
                print("Sıfıra Bölme Hatası!")
        elif secim == '5':
            print(f"Sonuç: {sayi1} ^ {sayi2} = {math.pow(sayi1, sayi2)}")

    elif secim in ['6', '7', '8', '9', '10']:
        sayi = float(input("Sayıyı girin: "))
        if secim == '6':
            if sayi >= 0:
                print(f"Sonuç: √{sayi} = {math.sqrt(sayi)}")
            else:
                print("Negatif Sayıların Karekökü Alınamaz!")
        elif secim == '7':
            if sayi > 0:
                print(f"Sonuç: log10({sayi}) = {math.log10(sayi)}")
            else:
                print("Logaritma Negatif Veya Sıfır Olamaz!")
        elif secim == '8':
            print(f"Sonuç: sin({sayi}) = {math.sin(math.radians(sayi))}")
        elif secim == '9':
            print(f"Sonuç: cos({sayi}) = {math.cos(math.radians(sayi))}")
        elif secim == '10':
            print(f"Sonuç: tan({sayi}) = {math.tan(math.radians(sayi))}")
    else:
        print("Geçersiz seçim, lütfen 1-10 arasında bir sayı girin.")


HesapMakinesi()

import my_module
print("\n----- KENDİ MODÜLÜM ------")
print(f" cot(45)={my_module.cotanjant(45)}")
print(f" String olarak toplama={my_module.string_toplama(4, 5)}")

