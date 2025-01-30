

class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgiler(self):
        return f"{self.yil} {self.marka} {self.model}"

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, pil_seviyesi=100):
        super().__init__(marka, model, yil)
        self.pil_seviyesi = pil_seviyesi

    def sarjet(self):
        self.pil_seviyesi = 100
        return f"{self.marka} {self.model} tamamen şarj edildi!"

    def pil(self):
        return f"Pil seviyesi: %{self.pil_seviyesi}"



a = ElektrikliAraba("DGDJFHJ", "Model S", 2023, 75)

print(a.bilgiler())  # 2023 Tesla Model S
print(a.pil())  # Pil seviyesi: %75
print(a.sarjet())  # Tesla Model S tamamen şarj edildi!
print(a.pil())  # Pil seviyesi: %100
