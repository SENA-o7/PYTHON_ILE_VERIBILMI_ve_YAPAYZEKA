class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def ses_cikar(self):
        pass
        '''Bunun sebebi, farklı hayvanların farklı sesler
             çıkarmasını sağlamak için alt sınıfların bu
             metodu kendilerine göre yeniden tanımlamasıdır (override)'''

class Kedi(Hayvan):
    def ses_cikar(self):
        return f"{self.ad}: Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return f"{self.ad}: Hav hav!"



kedi = Kedi("MİNİŞ")
kopek = Kopek("KÖPÜŞ")

print(kedi.ses_cikar())
print(kopek.ses_cikar())