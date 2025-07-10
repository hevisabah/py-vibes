my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}    

def shortest_path(graph, start, target=''):
    unvisited = list(graph) # list of nodes that have not been visited
    distances = {node: 0 if node == start else float('inf') for node in graph}   # distances from start to each node
    paths = {node: [] for node in graph}     # paths from start to each node
    paths[start].append(start)       # path from start to start
    
    while unvisited:   
        current = min(unvisited, key=distances.get)   # node with shortest distance
        for node, distance in graph[current]: # For every node that you can get to directly by traveling from the current node

            if distance + distances[current] < distances[node]: 
                distances[node] = distance + distances[current]# distance from start to node
                if paths[node] and paths[node][-1] == node:# if the path to node is already in the list of paths
                    paths[node] = paths[current][:]  # then extend the path

                else:# if the path to node is not in the list of paths
                    paths[node].extend(paths[current]) 
                paths[node].append(node)# add the node to the end of the path
        unvisited.remove(current)# remove the current node from the list of unvisited nodes
    
    targets_to_print = [target] if target else graph  # nodes to print
    for node in targets_to_print:# for every node in the list of nodes to print
        if node == start:  # if the node is the start node
            continue # then don't print it
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')   # print the distance and path
    
    return distances, paths    # return the distances and paths
    
shortest_path(my_graph, 'A', 'F') # print the shortest path from A to F