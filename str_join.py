# Вводится строка, состоящая из названий городов, разделенных пробелом. 
# Необходимо преобразовать эту строку, чтобы названия городов шли через точку с запятой. 
# Результат отобразить на экране.


s = input().split()
print(';'.join(s))