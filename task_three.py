"""Завдання 3. Реалізуйте алгоритм Дейкстри для знаходження найкоротшого 
шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть 
найкоротший шлях між всіма вершинами графа."""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
file_path = 'routes.csv'
routes_df = pd.read_csv(file_path)

# Створення графа
G = nx.Graph()

# Додавання ребер з даних, використовуючи дистанцію як вагу
for _, row in routes_df.iterrows():
    G.add_edge(row['City A'], row['City B'], weight=row['Distance'])

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    visited = []
    shortest_path = {vertex: [] for vertex in graph.nodes}
    shortest_path[start] = [start]

    while len(visited) < len(graph.nodes):
        # Знаходимо невідвідану вершину з найменшою відстанню
        min_distance = float('infinity')
        current_vertex = None
        for vertex in graph.nodes:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex

        if current_vertex is None:
            break

        visited.append(current_vertex)

        for neighbor, attributes in graph[current_vertex].items():
            distance = distances[current_vertex] + attributes['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = shortest_path[current_vertex] + [neighbor]

    return distances, shortest_path

# Знаходимо найкоротші шляхи між усіма вершинами
all_shortest_paths = {}
for node in G.nodes:
    distances, paths = dijkstra(G, node)
    all_shortest_paths[node] = paths

# Виведення найкоротших шляхів між усіма вершинами
for start, paths in all_shortest_paths.items():
    for end, path in paths.items():
        print(f"Найкоротший шлях між {start} та {end}: {path}")

# Візуалізація графа з вагами
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
