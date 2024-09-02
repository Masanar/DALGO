import sys


def CoinChange_noDP(value: int, coins: list[int]) -> int:
    return_value = 1_000_000_000_000
    if value == 0:
        return_value = 0
    elif value > 0:
        for coin in coins:
            return_value = min(return_value, 1 + CoinChange_noDP(value - coin, coins))
    return return_value


def CoinChange_TD(value: int, coins: list[int], memo: list[int]) -> int:
    return_value = 1_000_000_000_000
    if value == 0:
        return_value = 0
    elif value > 0:
        visited = memo[value]
        if visited != return_value:
            return_value = visited
        else:
            for coin in coins:
                return_value = min(
                    return_value, 1 + CoinChange_TD(value - coin, coins, memo)
                )
        memo[value] = return_value
    return return_value


def CoinChange_BU(value: int, coins: list[int]) -> int:
    return_value = 1_000_000_000_000
    memo = [return_value] * (value + 1)
    memo[0] = 0

    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)
    return memo[value]


if __name__ == "__main__":
    return_value = 1_000_000_000_000
    value = int(sys.stdin.readline().strip())
    # coins_value = list(map(int, sys.stdin.readline().split()))
    memo = [return_value] * (value + 1)
    print(CoinChange_BU(value, [50, 25, 5, 1]))
    # print(CoinChange_TD(value, [50, 25, 5, 1], memo))
    # print(CoinChange_noDP(value, [50, 25, 5, 1]))
