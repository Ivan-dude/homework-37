first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second) #записал для удобства в переменную

first_result = (len(x) - len(y) for x, y in zp if len(x) != len(y))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))