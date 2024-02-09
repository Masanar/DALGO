import sys


def subset_recursion(pointer: int, target_sum: int, number_list: int) -> bool:
    return_value = False
    current_value = number_list[pointer]
    end_pointer = pointer + 1 < len(number_list)
    if target_sum == 0 or target_sum - current_value == 0:
        return_value = True
    elif current_value > target_sum and end_pointer:
        return_value = subset_recursion(pointer + 1, target_sum, number_list)
    elif current_value <= target_sum and end_pointer:
        return_value = subset_recursion(
            pointer + 1, target_sum - current_value, number_list
        ) or subset_recursion(pointer + 1, target_sum, number_list)
    return return_value


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for i in range(number_of_cases):
        number_list = list(map(int, sys.stdin.readline().strip().split()))
        target = int(sys.stdin.readline().strip())
        print(subset_recursion(0, target, number_list))



""" 
def subsetSum(A, n, k):
    # Taken from: https://www.techiedelight.com/subset-sum-problem/
    # Why this solution is so bad?

    # return true if the sum becomes 0 (subset found)
    if k == 0:
        return True
 
    # base case: no items left, or sum becomes negative
    if n < 0 or k < 0:
        return False
 
    # Case 1. Include the current item `A[n]` in the subset and recur
    # for the remaining items `n-1` with the remaining total `k-A[n]`
    include = subsetSum(A, n - 1, k - A[n])
 
    # Case 2. Exclude the current item `A[n]` from the subset and recur for
    # the remaining items `n-1`
    exclude = subsetSum(A, n - 1, k)
 
    # return true if we can get subset by including or excluding the
    # current item
    return include or exclude
"""
