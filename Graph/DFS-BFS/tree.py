import random
from sys import stdin, stdout


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


def dfs_search(
    graph_list: list[list[str]], graph_matrix: list[list[int]], node_start: int
) -> bool:
    stack = [(node_start,node_start)]
    visited = {node_start}
    cycle_detection = True
    while len(stack) > 0 and cycle_detection:
        current_node,last_node = stack.pop()
        visited.add(current_node)
        current_children_str = graph_list[current_node]
        for i in current_children_str:
            i_int = int(i)
            if not (i_int in visited.difference({last_node})):
                graph_matrix[current_node][i_int] = 1
                if not (i_int in visited):
                    stack.append((i_int,current_node))
            else:
                cycle_detection = False
    return (cycle_detection, visited, graph_matrix)


def which_graph_type(graph_matrix: list[list[int]], size: int):
    no_directed_graph = True
    current_level = size
    while current_level > -1 and no_directed_graph:
        children = size
        while children > -1 and no_directed_graph:
            if (
                graph_matrix[current_level][children]
                != graph_matrix[children][current_level]
            ):
                no_directed_graph = False
            children -= 1
        current_level -= 1
    return no_directed_graph


def main():
    case_number = int(stdin.readline().strip())
    while case_number > 0:
        current_str_graph = stdin.readline().strip()
        current_graph = str_to_list_graph(current_str_graph)
        number_nodes = len(current_graph)
        current_empty_matrix_graph = [
            [0 for _ in range(number_nodes)] for _ in range(number_nodes)
        ]
        start_node = random.randint(0, number_nodes-1)
        cycle, visited, current_graph_matrix = dfs_search(
            current_graph, current_empty_matrix_graph, start_node
        )
        if not (cycle) or len(visited) != number_nodes:
            print(False)
        else:
            graph_type = which_graph_type(current_graph_matrix, number_nodes-1)
            result = cycle and (len(visited) == number_nodes) and graph_type
            print(result)
        case_number -= 1


if __name__ == "__main__":
    main()
