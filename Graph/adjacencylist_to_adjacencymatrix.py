if __name__ == '__main__':
    graph = dict()

    graph['A'] = ['B','C']
    graph['B'] = ['E','A','C']
    graph['C'] = ['A','B','E','F']
    graph['E'] = ['B','C']
    graph['F'] = ['C']

    matrix_elements = sorted(graph.keys())
    print(matrix_elements)

    col = row = len(matrix_elements)
    print(row)

    adjacency_matrix = [[0 for x in range(row)] for y in range(col)]
    print(adjacency_matrix)
    edge_lists = []

    for key in matrix_elements:
        for neighbour in graph[key]:
            edge_lists.append((key,neighbour))

    print(edge_lists)

    for edge in edge_lists:
        first_index = matrix_elements.index(edge[0])
        second_index = matrix_elements.index(edge[1])
        adjacency_matrix[first_index][second_index] = 1

    print(adjacency_matrix)