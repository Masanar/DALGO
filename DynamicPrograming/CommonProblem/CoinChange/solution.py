import sys
import random


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

def generate_value():
    for _ in range(100):
        sys.stdout.write(str(random.randint(0,400)))
        sys.stdout.write('\n')


if __name__ == "__main__":
    return_value = 1_000_000_000_000

    number_of_test = int(sys.stdin.readline().strip())
    for _ in range(number_of_test):
        value = int(sys.stdin.readline().strip())
        sys.stdout.write(str(CoinChange_BU(value, [50, 25, 5, 1])))
        sys.stdout.write('\n')
        # memo = [return_value] * (value + 1)
        # print(CoinChange_TD(value, [50, 25, 5, 1], memo))
        # print(CoinChange_noDP(value, [50, 25, 5, 1]))
