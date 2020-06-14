# Статистика игроков трех футбольных клубов Английской Премьер Лиги (сезон 2018/2019)
Liverpool = {'name':'Mohamed Salah', 'Yellow cards':1, 'Red сards':0, 'Goals':22, 'Goal pass':8,}
Chelsea = {'name':'Eden Hazard','Goals':16, 'Penalty':4, 'Goal pass':15}
Man_City = {'name':'Sergio Aguero','Goals':21, 'Goal pass':8}
print(Liverpool)
print(Chelsea)
print(Man_City, '\n')

# первый вариант слияния:
Super_team = {**Liverpool, **Chelsea, **Man_City}
print('первый вариант слияния:', '\n', Super_team, '\n')

# второй вариант слияния:
def function (*result):
    Dictionary={}
    for i in result:
        Dictionary.update(i)
    return Dictionary
print('второй вариант слияния:', '\n', function(Liverpool, Chelsea, Man_City))