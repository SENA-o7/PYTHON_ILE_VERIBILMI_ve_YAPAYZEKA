from functools import reduce
numbers = [-3,4,-7,8,-10,10,2,5,6,12]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Karesi :", squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Çift sayılar:", even_numbers)

multiplication=reduce(lambda x, y: x * y, numbers)
print("Listedeki sayıların çarpımı:", multiplication)

sorted_numbers_1 = sorted(numbers, key=lambda x: abs(x))
print("Mutlak değerlere göre sıralanmış liste:", sorted_numbers_1)

sorted_numbers_2 = sorted(numbers, reverse=True)
print("Büyükten küçüğe sıralanmış liste:", sorted_numbers_2)

sorted_numbers_3 = sorted(numbers, key=lambda x: abs(x), reverse=True)
print("Mutlak değerlere göre büyükten küçüğe sıralanmış liste:", sorted_numbers_3)

