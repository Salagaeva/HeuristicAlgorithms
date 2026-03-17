capacity = int(input("Вместимость рюкзака: "))  # например, вводим: 10
n = int(input("Количество предметов: "))       # например, вводим: 3

items = []

for i in range(n):
    weight, value = map(int, input("Вес и ценность через пробел: ").split())
    ratio = value / weight
    items.append((i + 1, weight, value, ratio))

# Сортируем по отношению ценность/вес, по убыванию
items.sort(key=lambda x: x[3], reverse=True)

total_weight = 0
total_value = 0
chosen = []

for item in items:
    index, weight, value, ratio = item
    if total_weight + weight <= capacity:
        chosen.append(index)
        total_weight += weight
        total_value += value

print("Выбраны предметы:", *chosen)
print("Итоговая ценность:", total_value)
