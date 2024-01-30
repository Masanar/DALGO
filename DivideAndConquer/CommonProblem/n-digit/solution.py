import sys

def n_digit(depth, previous_digit):
    if depth == 0:
        return 0
    if depth == 1:
        if previous_digit:
            return 1
        else:
            return 2
    if previous_digit:
        return n_digit(depth - 1, 0)
    else:
        return n_digit(depth - 1, 0) + n_digit(depth - 1, 1)


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        current_case = int(sys.stdin.readline().strip())
        print(n_digit(current_case, 0))
