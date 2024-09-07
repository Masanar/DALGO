import sys
from decimal import Decimal


def coin_change(amount: int, pointer: int) -> int:
  return_value = 0
  if pointer > 10 or amount < 0:
    # This means that we have reached the end of the coins (no more coins to check)
    # or the amount is negative (we have used too many coins)
    return_value = 0
  elif dp[amount][pointer] != 0:
    return_value = dp[amount][pointer]
  elif amount == 0:
    # This means that we have found a way to make the change
    return_value = 1
    dp[amount][pointer] = return_value
  else:
    # Here the first recursion is the idea of 'I don't want to use the coin', notice
    # that the pointer is increased by one, that makes the coin to be ignored in the
    # future calls.
    # The second recursion is the idea of 'I want to use the coin', notice that the
    # pointer is the same, that makes the coin to be used in the future calls.
    return_value = coin_change(amount, pointer + 1) + coin_change(
        amount - coins[pointer], pointer
    )
    dp[amount][pointer] = return_value
  return return_value

def clear_dp(value):
  for i in range(value):
    for j in range(11):
      dp[i][j] = 0

# The key to solve this problem is use a coin as many times as you want while giving the
# possibility to restrict the use of the coin in some point.
# Here the idea to translate this to a BU strategy is the same as in 166
# output with wrong format
if __name__ == "__main__":
  dp = [[0] * 11 for _ in range(30001)]
  coins = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
  current_case = sys.stdin.readline().strip()
  current_case_int = int(Decimal(current_case) * 100)
  while current_case != "0.00":
    value = coin_change(current_case_int, 0)
    # value = coin_change_bu(current_case_int)
    print(value)
    clear_dp(current_case_int)
    current_case = sys.stdin.readline().strip()
    current_case_int = int(float(current_case) * 100)
