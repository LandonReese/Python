from typing import List

def solve(input: str) -> List[int]:
    # dfs with a flip flop from black to white for each neighbor node visited
    # 6 6\n1 2\n1 3\n2 4\n2 5\n3 4\n4 6\n
    visited = set()
    node_graph = {}   
    return_list = []
    
    def dfs(node, bool):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in node_graph[node]:
                if bool == True:
                    return_list.append(node)
                dfs(neighbor, not bool)
    
    nodes, edges = -1, -1
    
    for line in input.split('\n'):
        if not line:
            continue
        print(line)
        if nodes == -1 and edges == -1:
            nodes, edges = line.split()
            for node in range(1, int(nodes) + 1):
                node_graph[str(node)] = []
        else:
            #put it in the graph
            key, value = line.split()
            node_graph[key].append(value)

    print(f"{nodes} {edges}\n{node_graph}")
    
    dfs('1', True)

    print(f"rl {return_list}")
    return return_list



def Main():
    solve('6 6\n1 2\n1 3\n2 4\n2 5\n3 4\n4 6\n')

if __name__ == Main():
    Main()
