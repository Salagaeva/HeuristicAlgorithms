# Города
cities = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И"]

# Входящие дороги (из условия)
input_paths = [
    "Б = А",
    "В = А Б Г",
    "Г = А Д",
    "Д = А",
    "Е = Б В",
    "Ж = Е В З",
    "З = В Г Д",
    "И = Е Ж З"
]

# Строим граф исходящих дорог
graph = {city: [] for city in cities}
for line in input_paths:
    target, sources = line.split("=")
    target = target.strip()
    sources = sources.strip().split()
    for src in sources:
        if target not in graph[src]:
            graph[src].append(target)

print("Граф исходящих дорог:")
for city in sorted(graph.keys()):
    if graph[city]:
        print(f"{city} -> {sorted(graph[city])}")

# Рекурсивный поиск всех путей из А в И, проходящих через В
def find_paths(current, end, path, passed_V):
    path = path + [current]
    
    if current == "В":
        passed_V = True
    
    if current == end:
        if passed_V:
            print(" -> ".join(path))
            return 1
        return 0
    
    total = 0
    for next_city in sorted(graph[current]):
        if next_city not in path:  # избегаем циклов
            total += find_paths(next_city, end, path, passed_V)
    
    return total

print(f"\nВсе пути из А в И, проходящие через В:")
result = find_paths("А", "И", [], False)
print(f"Всего: {result}")