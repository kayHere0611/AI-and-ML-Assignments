graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)
    
    # goal
    if start == goal:
        return path

    #explore child nodes
    for ch_node in graph.get(start, []): #get ch_nodes
        if ch_node not in visited: #check if visited
            result = dfs(graph, ch_node, goal, visited, path.copy()) 
            if result:
                return result

    return None 


start_node = 'A'
goal_node = 'F'

result = dfs(graph, start_node, goal_node)

if result:
    print("Path found:"," -> ".join(result))
else:
    print("Path not found")
