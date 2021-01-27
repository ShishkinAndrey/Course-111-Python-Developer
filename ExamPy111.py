import networkx as nx
import numpy as np

def task1(arr):
    a = len(arr) - 1
    out = list()
    while a > 0:
        out.append(arr[a])
        a = a // 1.7
    #В цикле while деление на 1.7 равносильно делению на 2 (как в бинарном поиске). Значит сложность O(log(n)
    out.merge_sort()
    # Алгоритм слияния работает за O(n*log(n)) и требует  O(n*log(n)) памяти
    # Ответ: сложность данного алгоритма О(n * log(n) * log(n))

def task3(g: nx.Graph):
    '''
    3.	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
    Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
    Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
    :param g: Граф
    :return: число компонент связности графа
    '''
    visited = {node: False for node in g.nodes}

    def dfs_count(current_node, g, visited):
        visited[current_node] = True
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                dfs_count(neighbor, g, visited)
    s = 0
    for i in visited:
        if not visited[i]:
            dfs_count(i, g, visited)
            s += 1
    return s


def task4(field):
    '''
    4.	Навигатор на сетке.
    Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода
    в каждую ячейку (все стоимости положительные).
    Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
    :param field: массив
    :return: путь минимальной стоимости из заданной ячейки в заданную ячейку
    '''
    for i in range(1, len(field)):
        field[i, 0] += field[i-1, 0]
    for j in range(1, len(field[i])):
        field[0, j] += field[0, j-1]
    for i in range(1, len(field)):
        for j in range(1, len(field[i])):
            field[i, j] += min(field[i-1, j], field[i, j-1])

    list_ind = [(i, j) for i in range(len(field)) for j in range(len(field[i]))]
    path = list()
    path.append(list_ind[-1])
    i, j = list_ind[-1]
    while (i, j) != (0, 0):
        if field[i - 1, j] < field[i, j - 1]:
            path.append((i - 1, j))
            i, j = i - 1, j
        else:
            path.append((i, j - 1))
            i, j = i, j - 1
    return path


def task6(lst_time):
    '''
    6.	Аренда ракет
    Вы – компания, дающая в аренду ракеты.
    Каждый день к вам приходит список заявок на использование ракет в виде:
    (час_начала, час_конца), (час_начала, час_конца), ...
    Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова

    :param lst_time: список заявок на использование ракет
    :return: хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
    '''
    time_dict = {}
    for period in lst_time:
        for i in range(period[0], period[1]):
            if i not in time_dict.keys():
                time_dict[i] = True
            else:
                return 'Одной ракеты не хватит, чтобы удовлетворить все заявки на этот день'
    return 'Одной ракеты хватит, чтобы удовлетворить все заявки на этот день'


def task5(lst_words):
    '''
    Для входного списка из N строк одинаковой длины построить консенсус-строку
    :param lst_words: список строк
    :return: консенсус-строку
    '''
    consensus_str = ''
    dict_letter = dict()
    for j in range(len(lst_words[0])):
        for i in lst_words:
            if i[j] not in dict_letter:
                dict_letter[i[j]] = 1
            else:
                dict_letter[i[j]] += 1
        max_ = max(dict_letter.values())
        for k in dict_letter:
            if dict_letter[k] == max_:
                consensus_str += k
        dict_letter.clear()
    return consensus_str





if __name__ == '__main__':
    g = nx.Graph()
    g.add_nodes_from('ABCDEFG')
    g.add_edges_from([('A', 'B'),
                      ('B', 'C'),
                      ('C', 'D'),
                      ('F', 'G')])
    # print(task3(g))
    #---------------------------------
    field_ = np.array([[2, 7, 9, 3], [12, 4, 1, 9], [1, 5, 2, 5]])
    # print(task4(field_))
    # ---------------------------------
    # print(task6([(10,12),(13,15),(12,13),(15,18)]))

    task5(['ATTA','ACTA','AGCA','ACAA'])