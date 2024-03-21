car_list = ['Лада', 'Жигули', 'Волга']

for car in reversed(car_list):
    print(car)


for i, car in enumerate(car_list):
    print(i, car)

for i, car in list(enumerate(reversed(car_list))):
    print(i, car)
