"""Завдання 2. Напишіть програму, яка використовує алгоритми DFS і BFS 
для знаходження шляхів у графі, який було розроблено у першому завданні. 
Далі порівняйте результати виконання обох алгоритмів для цього графа, 
висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для 
алгоритмів саме такі."""

import pandas as pd
import networkx as nx

# Завантаження даних з CSV файлу
file_path = 'routes.csv'
routes_df = pd.read_csv(file_path)

# Створення графа
G = nx.Graph()

# Додавання ребер з даних
for _, row in routes_df.iterrows():
    G.add_edge(row['City A'], row['City B'])

# Функція для знаходження шляху за допомогою DFS
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))
    return None

# Функція для знаходження шляху за допомогою BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# Задаємо початкову та кінцеву вершини для пошуку
start, goal = 'Vancouver', 'Miami'

# Знаходимо шляхи за допомогою DFS та BFS
dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

# Порівняння результатів
print("DFS Path:")
print(dfs_result)

print("\nBFS Path:")
print(bfs_result)
