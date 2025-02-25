import numpy as np
myarray = np.linspace(1, 50, 10).astype(int)
#np.arange(1,51,10) belirli adımda tam sayı aralığını direkt oluşturur fakat 10 eleman istenmesinde doğru ayarlanmalıdır
mean=np.mean(myarray)
std=np.std(myarray)
square=np.square(myarray)
filter=myarray[np.where(square > 25)]
filter2=myarray[np.where(myarray > 25)]

print("Array:\n ",myarray)
print("------------------- ")
print("Mean:\n ",mean)
print("------------------- ")
print("STD.:\n ",std)
print("------------------- ")
print("Square Array:\n ",square)
print("------------------- ")
print("25> Array:\n ",filter)
print("------------------- ")
print("25> Array:\n ",filter2)

