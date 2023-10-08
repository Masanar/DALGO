from sys import stdin, stdout
from collections import deque


def aux_map(s: str) -> list[str]:
    if s == "[]":
        return list()
    else:
        return s[1:-1].split(",")


def str_to_list_graph(graph_str: str) -> list[list[str]]:
    graph_str_no_beginning = graph_str[1:-1]
    for i in range(1, len(graph_str_no_beginning) - 1):
        if (
            graph_str_no_beginning[i] == ","
            and graph_str_no_beginning[i - 1] == "]"
            and graph_str_no_beginning[i + 1] == "["
        ):
            graph_str_no_beginning = (
                graph_str_no_beginning[:i] + "." + graph_str_no_beginning[i + 1 :]
            )
    graph_list_str_inside = graph_str_no_beginning.split(".")
    return list(map(aux_map, graph_list_str_inside))


def bfs_search(graph: list[list[str]], node_start: str, node_end: str) -> bool:
    queue = deque([int(node_start)])
    visited = [int(node_start)]
    result = True
    while len(queue) > 0 and result:
        current_node = queue.popleft()
        if current_node == int(node_end):
            result = False
        else:
            current_chields_str = graph[current_node]
            for node in current_chields_str:
                node_int = int(node)
                if not (node_int in visited):
                    visited.append(node_int)
                    queue.append(node_int)
    return not (result)


def main():
    case_number = int(stdin.readline().strip())
    while case_number > 0:
        current_str_graph = stdin.readline().strip()
        current_graph = str_to_list_graph(current_str_graph)
        v, w = stdin.readline().strip().split(",")
        number_nodes = len(current_graph)
        if int(v) < number_nodes and int(w) < number_nodes:
            print(bfs_search(current_graph, v, w))
        else:
            print("False")
        case_number -= 1


if __name__ == "__main__":
    main()
