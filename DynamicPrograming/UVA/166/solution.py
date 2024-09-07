import sys
from decimal import Decimal


# This is the first approach to the problem first problem, I do not delete this
# because this is the base for the BU solution
def solve_first_problem_divide_conquer(value, coins, pointer):
    return_value = 1_000_000
    if value == 0:
        return_value = 0
    elif value > 0:
        return_value = min(
            solve_first_problem_divide_conquer(value, coins, pointer + 1),
            solve_first_problem_divide_conquer(
                value - coins[pointer], coins, pointer + 1
            )
            + 1,
        )
    return return_value


def prepare_input_data(input_case: str):
    number_of_coins = list(map(int, input_case.split()[:6]))
    change = Decimal(input_case.split()[6])
    change_int = int(change * 100)
    len_coins = 0
    all_coins = []
    while len_coins < 6:
        all_coins += [zealand_coins[len_coins]] * number_of_coins[len_coins]
        len_coins += 1
    max_change_int = change_int + max(all_coins)
    return all_coins, change_int, max_change_int


def filter_list_each_five(targe_value, max_value, dp, matrix):
    possible_values = []
    for i in range(targe_value, max_value, 5):
        if matrix:
            possible_values.append(min(dp[i]))
        else:
            possible_values.append(dp[i])

    return possible_values


def solve_first_problem_BU(
    max_value,
    targe_value,
    coins,
):
    # Create the table [max_value][coin] with all the max_values as the big number
    # This table could be improve to only use the 5 'multiplos' of the max_value
    # the same optimization must be done in the iterations ahead
    dp = [[big_number] * (len(coins) + 1) for _ in range(max_value + 1)]
    # The base case [0][coin] is 0 for any coins, give a change for 0 is always 0 no
    # matter the coins
    dp[0] = [0] * (len(coins) + 1)

    for v in range(1, max_value + 1):
        for c in range(1, len(coins) + 1):
            # if we decide not to use the cth coin, the result will be the same as if we
            # had only c-1 coins available. Additionally, notice that the 'big' change
            # with the TD solution is that instead of going +1 in the pointer
            # (coins dimension) we are going -1 in the same dimension.
            dp[v][c] = dp[v][c - 1]
            if v >= coins[c - 1]:
                dp[v][c] = min(dp[v][c], dp[v - coins[c - 1]][c - 1] + 1)
    # Until this point we have a matrix with max_values [max_value][coin] where the
    # max_value corresponds to the min number of coins until that coin for giving change
    # on that max_value. Notice that the whole array dp[max_value] (where the cell is diff
    # from big_number) represent all the different forms of giving change to the
    # max_value. Remember that we only need the minimum way to give change for the values
    # in the range target_value...max_value. That is what we are going to do now
    return filter_list_each_five(targe_value, max_value, dp, True)


def CoinChange_BU(max_value: int, targe_value: int, coins: list[int]) -> int:
    memo = [big_number] * (max_value + 1)
    memo[0] = 0
    for i in range(1, max_value + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)
    # The same as in the first problem
    return filter_list_each_five(targe_value, max_value, memo, False)


def check_min_coin_combination(min_coins_pay, min_coins_return):
    min_value = big_number
    for i in range(0, len(min_coins_pay)):
        current_sum = min_coins_pay[i] + min_coins_return[i]
        if current_sum < min_value:
            min_value = current_sum
    return f"  {min_value}"


if __name__ == "__main__":
    # The bast majority of this code could be 'improve' to has less lines
    # I am writing in such manner to improve readability for a student that is struggling
    # with DP. Or probably this way make it worst... idk
    # I thinks that is a version to solver the first problem in space O(n), this is my
    # version of the solution and it is good enough, if you find better solutions 
    # please PR
    eol = "0 0 0 0 0 0"
    big_number = 1_000_000
    zealand_coins = [5, 10, 20, 50, 100, 200]
    current_case = sys.stdin.readline().strip()
    while current_case != eol:
        available_coins, value_to_pay, max_value_to_pay = prepare_input_data(
            current_case
        )
        min_coins_to_pay = solve_first_problem_BU(
            max_value_to_pay, value_to_pay, available_coins
        )
        min_coins_to_return = CoinChange_BU(
            max_value_to_pay - value_to_pay, 0, zealand_coins
        )
        print(check_min_coin_combination(min_coins_to_pay, min_coins_to_return))
        current_case = sys.stdin.readline().strip()
