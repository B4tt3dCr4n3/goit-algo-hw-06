## Висновки

### DFS Path:
- Маршрут, знайдений за допомогою алгоритму DFS, проходить через наступні міста: 
  - Vancouver → Seattle → Helena → Calgary → Winnipeg → Sault St. Marie → Montreal → Boston → New York → Washington → Pittsburgh → Toronto → Chicago → Saint Louis → Little Rock → Dallas → El Paso → Houston → New Orleans → Miami
- Шлях DFS має тенденцію проходити через глибокі, іноді менш оптимальні маршрути, що призводить до довшого шляху.

### BFS Path:
- Маршрут, знайдений за допомогою алгоритму BFS, проходить через наступні міста:
  - Vancouver → Calgary → Helena → Denver → Oklahoma City → Little Rock → New Orleans → Miami
- Шлях BFS завжди знаходить найкоротший шлях за кількістю вершин, що призводить до більш прямого та оптимального маршруту.

### Порівняння:

- **DFS (Depth-First Search)**:
  - Проходить якнайглибше по кожному можливому шляху, перш ніж повернутися назад і спробувати наступний шлях.
  - У нашому випадку, шлях DFS проходить через більше міст та містить більше кроків, ніж шлях BFS. Це пов'язано з тим, що DFS обирає глибокий шлях без перевірки, чи є він найкоротшим.
  
- **BFS (Breadth-First Search)**:
  - Проходить якнайширше по кожному рівню графа, перш ніж перейти на наступний рівень.
  - У нашому випадку, шлях BFS є значно коротшим за кількістю кроків, що робить його більш ефективним для пошуку найкоротшого шляху між двома точками в графі.

### Висновок:
- **DFS** підходить для завдань, де потрібен повний обхід графа або коли нам потрібно знайти будь-який шлях до цілі, навіть якщо він не є найкоротшим.
- **BFS** є кращим вибором для завдань, де важливо знайти найкоротший шлях за кількістю кроків між початковою та кінцевою точками.
