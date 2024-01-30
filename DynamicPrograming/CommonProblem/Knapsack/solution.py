import sys

# Given a set of items, with a weight and a value, and a weight limit. Determine the
# number of items to include so that the total weight do no exceed a
# given limit and the total value is maximum


def knap_sack_dp(
    weight_limit: int, item_pointer: int, values: list[int], weights: list[int]
) -> int:
    pass


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        values = list(map(int, sys.stdin.readline().split()))
        weights = list(map(int, sys.stdin.readline().split()))
        W = int(sys.stdin.readline().strip())
        # result = knap_sack_recursion(W, len(values), values, weights)
        # # sys.stdout.write(str(result))
        # print(result)

        t = [[-1 for i in range(W + 1)] for j in range(len(values) + 1)]
        print(knapsack(weights, values, W, len(values)))
