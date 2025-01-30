sayilar = []
while True:
    sayi = int(input("Lütfen bir sayı girin (-1 ile çıkış): "))
    if sayi == -1:
        break
    sayilar.append(sayi)

teklerin_karesi = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, sayilar)))
print("--------Tek sayıların kareleri:---------\n", teklerin_karesi)



print("-----------çif sayı filiteri---------")
cift_sayilar = list(filter(lambda x: x % 2 == 0, range(0, 51)))
print(cift_sayilar)


print("-----------sayılarım toplamı---------")
sayilar_arasi_toplam = lambda x, y: sum(range(x, y + 1))
print("Lütfen ikitane sayı giriniz:(ilk girilen büyük bir sayı olsun :))")
x = int(input("1.sayıyı giriniz"))
y = int(input("2.sayıyı giriniz"))
print(sayilar_arasi_toplam (x,y))