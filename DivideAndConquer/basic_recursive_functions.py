def max_element(array: list[int]) -> int:
    return max_element_aux(array[1:], array[0])


def max_element_aux(array: list[int], acc) -> int:
    """
        Función que recibe un arreglo de números enteros
        y retorna el valor máximo del arreglo.
        IMPLEMENTACIÓN RECURSIVA!!!
    """
    if len(array) == 1:
        acc = max(array[0], acc)
    else:
        acc = max_element_aux(array[1:], max(array[0], acc))
    return acc


if __name__ == "__main__":
    test = [1, 2, 3, -1, 10, 30, -1, 0, 20, 15, -1, -500]
    print(max_element(test))
