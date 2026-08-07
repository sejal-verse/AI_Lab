def dfs(graph,start):
    visited = []
    stack  = [start]
    while(stack):
        current_node = stack.pop()
        if current_node not in visited :
            print(f"exploring node : {current_node} ")
            visited.append(current_node)
            for neighbor in graph.get(current_node,[]):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
    return visited
print("------Building graph -----")
student_graph = {}
num_edges = int(input("how many edges (connections) does your graph have ?="))
print("enter each edge separated by a space (e.g. A B) : ")
for i in range(num_edges):    
    u,v = input(f"Edge {i+1}").split()
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)
start = input("Enter the starting node for DFS: ")
print(f"\nYour graph dictionary :{student_graph}")
print("starting dfs traversal ........")
dfs(student_graph, start)
