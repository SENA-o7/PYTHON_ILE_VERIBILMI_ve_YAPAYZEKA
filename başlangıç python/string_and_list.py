sentence=input("Enter a sentence: ")
print("Translating a sentence into big letters: ", sentence.upper())
print("\n")
print("-------------------------------------------------")
myshoppinglist=[]
myshoppinglist.append("yoğurt")
myshoppinglist.append("süt")
myshoppinglist.append("peynir")
myshoppinglist.append("zeytin")
myshoppinglist.append("patates")
myshoppinglist.append("soğan")
myshoppinglist.append("mantar")
myshoppinglist.append("havuç")

print( "The first version of the shopping list: ",myshoppinglist)
deleted = input("Enter the product you want to delete:")
if deleted in myshoppinglist:
    myshoppinglist.remove(deleted)
    print("The product has been deleted. Current list:", myshoppinglist)
else:
    print("This product could not be found in the list.")
