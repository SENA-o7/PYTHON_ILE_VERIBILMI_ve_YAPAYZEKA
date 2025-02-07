import math
def cotanjant(sayi):
    if math.tan(math.radians(sayi)) == 0:
        return "Hata: Cotanjant tanımsızdır!"
    return 1 / math.tan(math.radians(sayi))

def string_toplama(a, b):
    return f"{a} + {b} = {a + b}"