import sys
import random

def lis(array):
    l = len(array)
    LIS = [1] * l
    # max_LIS = 0
    for i in range(1,l):
        max_lis_sub = 0
        for k in range(i):
            if array[k] < array[i]:
                max_lis_sub =  max(max_lis_sub,LIS[k])
        # max_LIS = max(1 + max_lis_sub, max_LIS)
        LIS[i] = 1 + max_lis_sub 
    return max(LIS) 



def generate_cases(number_of_cases: int):
    print(number_of_cases)
    for _ in range(number_of_cases):
        for _ in range(random.randint(5, 20)):
            print(random.randint(-100, 100), end=" ")
        print()

if __name__ == "__main__":
    # generate_cases(100)
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        _list = list(map(int, sys.stdin.readline().split()))
        print(lis(_list))