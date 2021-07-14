
def DepthFirstSearch(graph,root):
    visited_vertices = []
    graph_stack = []
    graph_stack.append(root)
    #print(graph_stack)
    while len(graph_stack) > 0:
        node = graph_stack.pop()
        #print("exploring node\t",node)
        if node not in visited_vertices:
            visited_vertices.append(node)
        #print("intermediate\t",visited_vertices)

        adjacent_nodes = graph[node]
        remaining_nodes = set(adjacent_nodes).difference(set(visited_vertices))
        if remaining_nodes is None:
            continue
        #print(remaining_nodes)
        remaining_nodes = sorted(remaining_nodes)
        #print(remaining_nodes)

        #count = len(remaining_nodes)
        #print(count)


        for i in range(len(remaining_nodes)):
            
            #print("appending elem",elem)
            graph_stack.append(remaining_nodes.pop())
            #visited_vertices.append(elem)
            #print('STACK\t',graph_stack)
            #print('Final\t',visited_vertices)

    return visited_vertices



if __name__ == '__main__':
    graph = dict()
    graph['A'] = ['B', 'S']
    graph['B'] = ['A']
    graph['S'] = ['A', 'G', 'C']
    graph['D'] = ['C']
    graph['G'] = ['S', 'F', 'H']
    graph['H'] = ['G', 'E']
    graph['E'] = ['C', 'H']
    graph['F'] = ['C', 'G']
    graph['C'] = ['D', 'S', 'E', 'F']


    result = DepthFirstSearch(graph,'A')
    print(result)