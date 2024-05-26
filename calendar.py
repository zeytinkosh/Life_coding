# преобразование года и месяца в календарь

import calendar

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))
