import pandas as pd
data={
    "İsim":["Veli","Ayşe","Mehmet","Betül"],
    "Yaş":[25,30,22,27],
    "Maaş":[5000,6000,4500,5200]
}
df=pd.DataFrame(data)
print(df)

mean_yas=df["Yaş"].mean()
mean_maas=df["Maaş"].mean()
sort_yas=df.sort_values(by="Yaş")

print("----------------------------")
print("Ortalama Yaş:", mean_yas)
print("----------------------------")
print("Ortalama Maaş:", mean_maas)
print("----------------------------")
print("Maaşı 5000 büyük olan:\n", df[df["Maaş"]>5000])
print("----------------------------")
print("Yaşa göre sıralama:", sort_yas)
