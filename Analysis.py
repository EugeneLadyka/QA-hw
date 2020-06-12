str = "'Денис даёт нам классные задачки, которые помогут нам найти лучшую работу.'"
symbol = "м"
{symbol:str.count(symbol) for symbol in set(str)}
print(str)
print('символ =', symbol, '\n'
                          'встречается в строке -', str, "-", str.count(symbol), "раз(а).")