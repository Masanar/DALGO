from sys import stdin
class DisjoinSet:
    def __init__(self, set_size) -> None:
        self.rank = [1] * set_size
        self.parent = [i for i in range(set_size)]

    def find(self,x: int) -> int:
        if self.parent[x] != x:
            # Update the parent of x
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x: int,y: int) -> None:

        x_parent = self.find(x)
        y_parent = self.find(y)
        x_rank = self.rank[x_parent]
        y_rank = self.rank[y_parent]

        if x_parent != y_parent:
            if x_rank < y_rank:
                self.parent[x_parent] = y_parent 
            elif y_rank < x_rank:
                self.parent[y_parent] = x_parent 
            else:
                self.parent[y_parent] = x_parent 
                self.rank[x_parent] = self.rank[x_parent] + 1
                
# This is a slightly different Kruskal implementation, it don't return the MST rather the
# value of the MST

def Kruskal(graph: list[list[int]], graph_nodes: int) -> int:
    total_cost = 0
    mst_value = 0
    graph.sort(key=lambda x:x[2]) 
    disjoin_set = DisjoinSet(graph_nodes)
    for edge in graph:
        if disjoin_set.find(edge[0]) != disjoin_set.find(edge[1]):
            total_cost += edge[2]
            mst_value += edge[2]
            disjoin_set.union(edge[0],edge[1])
        else:
            total_cost += edge[2]
    return total_cost-mst_value


def main():
    info = stdin.readline().strip()
    while info != '0 0':
        graph = []
        nodes_txt , connections_txt = info.split()
        nodes , connections = int(nodes_txt), int(connections_txt) 
        for _ in range(connections):
            current_connection = stdin.readline().strip().split()
            graph.append(list(map(int, current_connection)))
        print(Kruskal(graph,nodes))
        info = stdin.readline().strip()

if __name__ == '__main__':
    main()
    