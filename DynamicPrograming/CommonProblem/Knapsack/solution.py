import sys

# Given a set of items, with a weight and a value, and a weight limit. Determine the
# number of items to include so that the total weight do no exceed a
# given limit and the total value is maximum


def knap_sack_dp(
    weight_limit: int, item_pointer: int, values: list[int], weights: list[int]
) -> int:
    return_value = -1
    next_item_pointer = item_pointer - 1
    current_store_value = t[item_pointer][weight_limit]
    if weight_limit == 0 or item_pointer == 0:
        return_value = 0
    elif current_store_value != -1:
        return_value = current_store_value
    elif weights[next_item_pointer] > weight_limit:
        current_store_value = knap_sack_dp(
            weight_limit, next_item_pointer, weights, values
        )
        t[item_pointer][weight_limit] = current_store_value
        return_value = current_store_value
    else:
        current_store_value = max(
            values[next_item_pointer]
            + knap_sack_dp(
                weight_limit - weights[next_item_pointer],
                next_item_pointer,
                values,
                weights,
            ),
            knap_sack_dp(weight_limit, next_item_pointer, values, weights),
        )
        t[item_pointer][weight_limit] = current_store_value
        return_value = current_store_value
    return return_value


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        values = list(map(int, sys.stdin.readline().split()))
        weights = list(map(int, sys.stdin.readline().split()))
        W = int(sys.stdin.readline().strip())
        t = [[-1 for i in range(W + 1)] for j in range(len(values) + 1)]
        result = knap_sack_dp(W, len(values), values, weights)
        # # sys.stdout.write(str(result))
        print(result)
