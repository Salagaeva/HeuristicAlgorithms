cities = ["A", "B", "C", "D"]

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * len(cities)
path = []
total_distance = 0

current = 0
visited[current] = True
path.append(cities[current])

for _ in range(len(cities) - 1):
    nearest = None
    min_dist = float("inf")

    for j in range(len(cities)):
        if not visited[j] and graph[current][j] < min_dist and graph[current][j] != 0:
            min_dist = graph[current][j]
            nearest = j

    visited[nearest] = True
    path.append(cities[nearest])
    total_distance += min_dist
    current = nearest

print("Кратчайший путь чтобы посетить все точки:")
print(" → ".join(path))
print("Займёт этот путь:", total_distance)
