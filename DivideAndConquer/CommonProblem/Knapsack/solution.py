import sys

# Given a set of items, with a weight and a value, and a weight limit. Determine the
# number of items to include so that the total weight do no exceed a
# given limit and the total value is maximum


def knap_sack_recursion(
    weight_limit: int, item_pointer: int, values: list[int], weights: list[int]
) -> int:
    return_value = -1
    next_item = item_pointer - 1
    if weight_limit == 0 or item_pointer == 0:
        return_value = 0
    if weights[next_item] > weight_limit and return_value == -1:
        return_value = knap_sack_recursion(weight_limit, next_item, values, weights)
    elif return_value == -1:
        return_value = max(
            values[next_item]
            + knap_sack_recursion(
                weight_limit - weights[next_item], next_item, values, weights
            ),
            knap_sack_recursion(weight_limit, next_item, values, weights),
        )
    return return_value


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        values = list(map(int, sys.stdin.readline().split()))
        weights = list(map(int, sys.stdin.readline().split()))
        W = int(sys.stdin.readline().strip())
        result = knap_sack_recursion(W, len(values), values, weights)
        # sys.stdout.write(str(result))
        print(result)
