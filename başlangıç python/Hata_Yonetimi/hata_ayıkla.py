class NegativeNumberError(Exception):
    def __init__(self, mesaj="Negatif sayı girişi yasak!"):
        self.mesaj = mesaj
        super().__init__(self.mesaj)
        
def bolme_islemi():
    try:
        sayi1 = float(input("Bölünecek sayıyı girin: "))
        sayi2 = float(input("Bölen sayıyı girin: "))

        if sayi1 < 0 or sayi2 < 0:
            raise NegativeNumberError("Negatif sayı giremezsiniz!")

        if sayi2 == 0:
            raise ZeroDivisionError("Bir sayı sıfıra bölünemez!")

        sonuc = sayi1 / sayi2
        print(f"Sonuç: {sonuc}")

    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
    except NegativeNumberError as e:
        print(f"Hata: {e}")
    except ZeroDivisionError as e:
        print(f"Hata: {e}")


bolme_islemi()

