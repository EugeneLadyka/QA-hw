str = "результат вычислений первой функции ="
str2 = "+ результат второй функции с добавлением строки"
def func(result1):
    return result1
first_number = int(input("укажите первое число: \n"))
second_number = int(input("укажите второе число: \n"))
result1 = first_number * second_number
print("%s" % (str), func(result1),"\n")

def func2(result2):
    return result2
result2 = result1
print(result2, "%s" % (str2))
