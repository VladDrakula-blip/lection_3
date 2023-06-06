# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", 'r') as file:
    lines = file.readlines()

prices = []
current_purchase = []

for line in lines:
    line = line.strip()
    if line:
        try:
            price = float(line)
            current_purchase.append(price)
        except ValueError:
            continue
    elif current_purchase:
        prices.append(sum(current_purchase))
        current_purchase = []

# Добавляем сумму оставшейся покупки, если есть
if current_purchase:
    prices.append(sum(current_purchase))

# Сортируем суммы покупок в порядке убывания
sorted_prices = sorted(prices, reverse=True)

# Выбираем три самые дорогие покупки
three_most_expensive_purchases = sum(sorted_prices[:3])

print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
