class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y) #ki nesne arasında toplama işlemi yapılmasını sağlar.

    def __str__(self):
        return f"Vektör({self.x}, {self.y})" #print'in yaptığını ypar



vektor1 = Vektor(8, 4)
vektor2 = Vektor(1, 9)

toplam = vektor1 + vektor2  # __add__ metodu çağrılır
print(toplam)
