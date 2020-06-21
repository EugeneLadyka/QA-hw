my_dict = {'a':645, 'b':3987, 'c':93,'d':111, 'e':646, 'f':20}
items = [(key, value) for value, key in my_dict.items()]
# возврат трех максимальных ключей из словаря:
print (sorted(my_dict, reverse=True, key=my_dict.get)[:3])
# возврат трех максимальных пар ключ-значение из словаря:
print (sorted(items, reverse=True)[:3])
# возврат максимального ключа-значение из словаря:
print(max(items))
