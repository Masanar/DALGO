import random
from sys import stdin, stdout

import random

def generate_random_numbers(count, min_val=1, max_val=50_000):
    return [random.randint(min_val, max_val) for _ in range(count)]

def generate_case():
    number_of_statue = 50_000
    sorted_statues = sorted(generate_random_numbers(number_of_statue))
    number_of_queries = 100
    queries = generate_random_numbers(number_of_queries)
    print(number_of_statue)
    print(" ".join(map(str, sorted_statues)))
    print(number_of_queries)
    print(" ".join(map(str, queries)))

# ns is never used
def binary_search(statues, ns, query, start, end):
    middle = (end + start) // 2
    current_middle = statues[middle]
    return_index = middle
    if current_middle < query:
        # Solutions never in the top nor the bottom
        right_middle = statues[middle + 1]
        if right_middle < query:
            # keep searching
            return_index = binary_search(statues, ns, query, middle + 1, end)
        # elif query == right_middle:
        else:
            return_index = middle + 1
    elif query < current_middle:
        # Solutions never in the top nor the bottom
        left_middle = statues[middle - 1]
        if query < left_middle:
            # keep searching
            return_index = binary_search(statues, ns, query, start, middle - 1)
        else:
            # found the exact place on the next left
            return_index = middle - 1
    return return_index


def find_no_repetition_left(statues, index, query):
    if index <= 0:
        return statues[0]
    elif query <= statues[index]:
        return find_no_repetition_left(statues, index - 1, query)
    else:
        return statues[index]

def find_no_repetition_right(statues, index, query):
    if index >= len(statues) - 1:
        return statues[-1]
    # elif statues[index] <= query:
    elif query >= statues[index]:
        return find_no_repetition_right(statues, index + 1, query)
    else:
        return statues[index]
    

def main():
    # In this case the IO is easy because it is just one case

    number_of_statue = int(stdin.readline().strip()) - 1
    statues = list(map(int, stdin.readline().split()))
    _number_of_queries = int(stdin.readline().strip())
    queries = list(map(int, stdin.readline().split()))
    start = 0
    for query in queries:
        # I REALLY HATE THIS PART, there are too many if statements. I gets the job done 
        # but it is not pretty. For sure there is a better way to do this.
        lh,gh = -1,-1
        if query == statues[number_of_statue]:
            lh = find_no_repetition_left(statues, number_of_statue, query )
        elif query == statues[0]:
            gh = find_no_repetition_right(statues, 0, query )
        elif query > statues[number_of_statue]:
            lh = statues[number_of_statue]
        elif query < statues[0]:
            gh = statues[0]
        else:
            middle_index = binary_search(
                statues, number_of_statue, query, start, number_of_statue
            )
            lh = find_no_repetition_left(statues, middle_index, query )
            gh = find_no_repetition_right(statues, middle_index, query )
        print(f"{lh} {gh}")


if __name__ == "__main__":
    main()
    # generate_case()
