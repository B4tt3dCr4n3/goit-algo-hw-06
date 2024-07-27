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

# Функція для знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra_all_paths(graph):
    shortest_paths = dict(nx.all_pairs_dijkstra_path(graph, weight='weight'))
    return shortest_paths

# Знаходимо найкоротші шляхи між усіма вершинами
shortest_paths = dijkstra_all_paths(G)

# Виведемо кілька прикладів найкоротших шляхів
for start, paths in shortest_paths.items():
    for end, path in paths.items():
        print(f"Найкоротший шлях між {start} та {end}: {path}")

# Візуалізація графа з вагами
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Transport Network Graph with Weights")
plt.show()
