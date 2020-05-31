def fanction():
    a = int(input("укажите значение А: \n"))
    b = int(input("укажите значение Б: \n"))
    c = int(input("укажите значение В: \n"))
    while a <= b:
        a = a + c
        if a <= b:
            print("А =", a, " - Пока что нет")
        elif a > b:
            print("Дождались А =", a)
fanction()
