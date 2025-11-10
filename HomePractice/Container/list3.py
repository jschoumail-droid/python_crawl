shopping=["bread","milk","eggs"]
print(shopping)
print(shopping[1:])
print(shopping[0:2])

shopping.append("apple")
print("after append:",shopping)

shopping.insert(2,"ham")
print("after insert:",shopping)

item=shopping.pop(3)
print(item,shopping)