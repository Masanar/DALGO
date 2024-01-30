import sys


def subset_recursion_dp(pointer: int, target_sum: int, number_list: int) -> bool:
    return_value = False
    current_value = number_list[pointer]
    current_store_value = memo[pointer][target_sum]
    end_pointer = pointer + 1 < len(number_list)
    if current_store_value != -1:
       return_value = current_store_value 
    elif target_sum == 0 or target_sum - current_value == 0:
        return_value = True
        memo[pointer][target_sum] =  return_value
    elif current_value > target_sum and end_pointer:
        return_value = subset_recursion_dp(pointer + 1, target_sum, number_list)
        memo[pointer][target_sum] =  return_value
    elif current_value <= target_sum and end_pointer:
        return_value = subset_recursion_dp(
            pointer + 1, target_sum - current_value, number_list
        ) or subset_recursion_dp(pointer + 1, target_sum, number_list)
        memo[pointer][target_sum] =  return_value
    return return_value


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for i in range(number_of_cases):
        number_list = list(map(int, sys.stdin.readline().strip().split()))
        target = int(sys.stdin.readline().strip())
        memo = [[-1 for i in range(target + 1)] for j in range(len(number_list) + 1)]
        print(subset_recursion_dp(0, target, number_list))

