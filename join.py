s1 = 'Мама,'
s2 = 'я музыкант'
print(' '.join([s1, s2]))

#' ' - строка-соединитель (то что будет между s1 и s2)
#s1 и s2 составлены в список потму что join() принимает только один аргумент (список, кортеж или словарь из строк)

print(' '.join((s1, s2)))            # Кортеж
print(' '.join({s1: 'a', s2: 'b'}))  # Словарь с s1 и s2 в качестве ключей
print(' '.join({'Мама,':s1, 'я музыкант!':s2}))    # Словарь с s1 и s2 в качестве значений