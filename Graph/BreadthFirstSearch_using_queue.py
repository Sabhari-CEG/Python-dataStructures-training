from collections import deque
def BreadthFirstSearch(graph,root):
    visited_vertices = []
    graph_queue = deque([root])
    visited_vertices.append(root)

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adjacent_nodes = graph[node]
        remaining_nodes = set(adjacent_nodes).difference(set(visited_vertices))
        if len(remaining_nodes) > 0:
            for node in sorted(remaining_nodes):
                visited_vertices.append(node)
                graph_queue.append(node)
    return  visited_vertices



if __name__ == '__main__':

    graph = dict()
    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']


    result = BreadthFirstSearch(graph,'A')
    print(result)