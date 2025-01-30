
a="2"
b="2 python"
c=2
d=2.2
e=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("String değerlerde artı işareti: ", a+b)
print("integer değerlerle işlem: ", c-4)
print("float değerle işlem: ", d*3)

integer_to_string = str(c)
float_to_integer = int(d)
string_to_float = float(a)
print(integer_to_string, float_to_integer,string_to_float)

num1=(float(input("Please! Enter the number : " )))
num2=(float(input("Please! Enter the number : " )))
print(f"{num1 + num2} | {num1 - num2} | {num1 * num2}")

