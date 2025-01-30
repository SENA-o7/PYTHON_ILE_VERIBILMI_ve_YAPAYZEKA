counter = 0

def sayac_arttir():
    global counter #global değişkeni fonksiyonun içine çağırmazsak counter olarak yazsaydık o da local olurdu
    counter += 1
    local_num= 5
    print(f"fonksiyon içindeki  sayı: {local_num}")
    print(f"Global sayaç değeri: {counter}")

print(f"başlangıçtaki global sayaç: {counter}\n")
sayac_arttir()
print("\n")
sayac_arttir()
print("\n")
print(f"son global sayaç değeri: {counter}")