from random import randrange

leght = int(input("укажите аргумент определяющий длину списка: \n"))
max = int(input("укажите аргумент, максимальное значение списка: \n"))
def function(leght, max):
    list=[]
    for i in range (leght):
        list.append(randrange(max))
    print(list)
function(leght, max)


