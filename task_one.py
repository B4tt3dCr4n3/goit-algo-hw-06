"""Завдання 1. Створіть граф за допомогою бібліотеки networkX для моделювання 
певної реальної мережі (наприклад, транспортної мережі міста, соціальної 
мережі, інтернет-топології). Візуалізуйте створений граф, проведіть аналіз 
основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин)."""

# Для виконання завдання використав дані про маршрути між містами з настільної 
# гри "Ticket to Ride: USA".

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
file_path = 'routes.csv'
routes_df = pd.read_csv(file_path)

# Створення графа
G = nx.Graph()

# Додавання ребер з даних
for _, row in routes_df.iterrows():
    G.add_edge(row['City A'], row['City B'])

# Візуалізація графа
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин (міст): {num_nodes}")
print(f"Кількість ребер (маршрутів): {num_edges}")
print("Ступінь вершин:")
for city, degree in degree_dict.items():
    print(f"{city}: {degree}")
