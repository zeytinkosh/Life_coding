# Напиши код, используя лямбда-выражение, чтобы найти максимальное число в списке
# Подсказка: используй функцию max() и передай ей ключ (key) с лямбда-выражением

numbers = [10, 5, 25, 15, 30, 20]
maximum = lambda x: max(x)
print(maximum(numbers))


# Напиши код, используя лямбда-выражение, чтобы отфильтровать список и оставить только строки,
# которые начинаются с заглавной буквы (подсказка: используй метод isupper() для строк)

words = ["Apple", "banana", "Cherry", "Date", "Fig"]
upper_word = list(filter(lambda word: word.istitle(), words))
print(upper_word)
