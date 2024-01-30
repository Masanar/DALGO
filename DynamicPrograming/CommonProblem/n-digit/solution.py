import sys

def n_digit_dp(depth, previous_digit):
    return_value = 0
    current_case_value = memo[depth][previous_digit]
    def _save(ccv):
        memo[depth][previous_digit] = ccv 
        return ccv
    if current_case_value != -1:
        return_value = current_case_value
    elif previous_digit:
        current_case_value = n_digit_dp(depth - 1, 0)
        return_value = _save(current_case_value)
        # memo[depth][previous_digit] = current_case_value
        # return_value = current_case_value
    else:
        current_case_value = n_digit_dp(depth - 1, 0) + n_digit_dp(depth - 1, 1)
        return_value = _save(current_case_value)
        # memo[depth][previous_digit] = current_case_value
        # return_value = current_case_value
    
    return return_value


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        current_case = int(sys.stdin.readline().strip())
        # Let me assume that the cases are not less than 2
        memo = [[0,0],[2,1]] + [[-1,-1] for _ in range(current_case - 1)]
        print(n_digit_dp(current_case, 0))
