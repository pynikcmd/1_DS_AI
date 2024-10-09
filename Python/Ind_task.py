import heapq
import math
import time
from Problem import Problem
from Node import Node, failure, expand, path_actions, path_states
from Queue import PriorityQueue
from collections import deque

# Обновленный список городов и расстояний между ними
distances = {
    ('Ставрополь', 'Михайловск'): 14,
    ('Михайловск', 'Московское'): 25,
    ('Московское', 'Донское'): 20,
    ('Донское', 'Изобильный'): 22,
    ('Михайловск', 'Изобильный'): 46,
    ('Изобильный', 'Новотроицкая'): 14,
    ('Новотроицкая', 'Новоалександровск'): 17,
    ('Новоалександровск', 'Кропоткин'): 56,
    ('Кропоткин', 'Новоивановский'): 25,
    ('Кропоткин', 'Восточный'): 32,
    ('Новоивановский', 'Мирный'): 7,
    ('Мирный', 'Тбилисская'): 14,
    ('Тбилисская', 'Ладожская'): 25,
    ('Восточный', 'Ладожская'): 41,
    ('Ладожская', 'Двубратский'): 14,
    ('Двубратский', 'Васюринская'): 39,
    ('Васюринская', 'Знаменский'): 37,
    ('Васюринская', 'Старокорсунская'): 12,
    ('Старокорсунская', 'Хутор Ленина'): 10,
    ('Хутор Ленина', 'Краснодар'): 25,
    ('Знаменский', 'Краснодар'): 17,
}



# Функция для получения расстояния между городами
def get_distance(city1, city2):
    return distances.get((city1, city2)) or distances.get((city2, city1), float('inf'))


class TSPProblem(Problem):
    """Класс для решения задачи коммивояжёра."""

    def __init__(self, initial, goal):
        super().__init__(initial=initial, goal=goal)
        self.cities = list(distances.keys())

    def actions(self, state):
        """Возвращает возможные действия - соседние города."""
        return [city for city in distances.keys() if state in city]

    def result(self, state, action):
        """Возвращает следующий город, в который переходит коммивояжер."""
        return action[1] if state == action[0] else action[0]

    def action_cost(self, state, action, result):
        """Возвращает стоимость перехода между городами."""
        return get_distance(state, result)


# Инициализация задачи
problem = TSPProblem(initial='Ставрополь', goal='Краснодар')


# Поиск решения методом полного перебора
def search_tsp(problem):
    frontier = PriorityQueue([Node(problem.initial)])  # Исправление: удален лишний кортеж
    explored = set()

    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return path_states(node), node.path_cost

        explored.add(node.state)
        for child in expand(problem, node):
            if child.state not in explored:
                frontier.add(child)

    return failure


# Замер времени выполнения
start_time = time.time()

# Запуск поиска
route, distance = search_tsp(problem)

# Вывод результатов
end_time = time.time()
execution_time = end_time - start_time

print(f"Минимальный маршрут: {route}")
print(f"Расстояние: {distance} км")
print(f"Время выполнения программы: {execution_time:.4f} секунд")
