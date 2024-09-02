import sys
# 0 -> False
def n_digit(depth, previous_digit):
    digit_count = 0
    if not depth:
        return 0
    if depth == 1:
        if previous_digit:
            digit_count = 1
        else:
            digit_count = 2
    elif previous_digit:
        digit_count = n_digit(depth - 1, 0)
    elif not previous_digit:
        digit_count = n_digit(depth - 1, 0) + n_digit(depth - 1, 1)
    return digit_count


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        current_case = int(sys.stdin.readline().strip())
        print(n_digit(current_case, 0))
