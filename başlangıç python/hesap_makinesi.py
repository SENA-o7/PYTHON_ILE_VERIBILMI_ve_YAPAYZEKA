class HesapMakinesi:
    def toplama(self, a, b):
        return a + b

    def cikarma(self, a, b):
        return a - b

    def carpma(self, a, b):
        return a * b

    def bolme(self, a, b):
        if b == 0:
            return "Hata! Sıfıra bölemezsin.."
        return a / b




hesap = HesapMakinesi()
print("Toplama:", hesap.toplama(145, 50))
print("Çıkarma:", hesap.cikarma(190, 67))
print("Çarpma:", hesap.carpma(33, 2))
print("Bölme:", hesap.bolme(35, 7))
print("Bölme (hata testi):", hesap.bolme(7, 0))