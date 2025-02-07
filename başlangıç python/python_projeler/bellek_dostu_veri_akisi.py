import random


def random_generator(count, lower, upper):
     for _ in range(count):
        yield random.uniform(lower, upper)  # Ondalıklı sayılar üretiyoruz

def calculate_average(generator):
    total = 0
    count = 0
    for number in generator:
        total += number
        count += 1

    return total / count if count > 0 else 0


while True:
    try:
        n = int(input("Kaç adet rastgele sayı üretmek istersiniz? "))
        if n <= 0:
            print("Lütfen pozitif bir tam sayı girin.")
            continue
        break
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")


while True:
    try:
        lower = float(input("Sayıların alt sınırını girin: "))
        upper = float(input("Sayıların üst sınırını girin: "))
        if lower > upper:
            print("Alt sınır, üst sınırdan büyük olamaz.")
            continue
        break
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")


gen = random_generator(n, lower, upper)
average = calculate_average(gen)

print(f"{n} adet [{lower}, {upper}] aralığında üretilen sayının ortalaması: {average:.2f}")
