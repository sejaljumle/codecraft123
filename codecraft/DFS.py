def dfs_recursive(graph, vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    print(vertex, end=' ')  # Print the vertex during traversal
    
    # Recursively visit all the adjacent vertices that are not visited
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example of using the recursive DFS implementation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()  # Set to store visited nodes
start_vertex = 'A'
print("DFS Recursive Traversal:")
dfs_recursive(graph, start_vertex, visited)