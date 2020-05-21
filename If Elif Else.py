element1 = int(input('Ведите значение A \n'))
element2 = int(input('Ведите значение Б \n'))
element3 = int(input('Ведите значение B \n'))
if element1 > element2:
    print('"Свершилось!"')
elif element2 > element1:
    print('"Да ну!"')
elif element1 == element2:
    element1 = element1 + element2
    element2 = element2 - element3
    print('"А если так?"')
    print('A = А + Б =', element1)
    print('Б = Б - В =', element2)
    if element1 > element2:
        print('"Свершилось!"')
    elif element2 < element1:
        print('"Да ну!"')
    else:
        print('"А если так?"')





