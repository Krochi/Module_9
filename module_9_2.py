#Даны несколько списков, состоящих из строк

# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов.
# В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
# В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.

# Примечания:
# Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.

#Решение:

# Для решения задачи, нужно создать три переменные с использованием генераторов списков и словарей:
#
# 1. first_result: Нужно создать список, состоящий из длин строк из списка first_strings, при условии,
#    что длина строки не менее 5 символов.
#
# 2. second_result: Нужно создать список пар слов (кортежей), состоящих из слов из списка first_strings и second_strings,
#    где оба слова имеют одинаковую длину.
#
# 3. third_result: Нужно создать словарь, где ключами будут строки из объединённых списков first_strings и second_strings,
#    а значениями — длины этих строк, при условии, что длина строки четная.


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(n) for n in first_strings if len(n) >= 5]

second_result = [(n1,n2) for n2 in second_strings for n1 in first_strings if len(n2) == len(n1)]

third_result = {n: len(n) for n in second_strings + first_strings if len(n) % 2 == 0}


# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
#Вывод на консоль:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
