import sys


def find_lis_sequence(
    array: list[int],
    lis_pointers: list[int],
    current_pointer: int,
    acc_response: list[int],
    lis_value: int
):
    # This could be a iterative function instead of a recursive one, but I like recursion...
    return_value = []
    array_current_pointer = array[current_pointer]
    value = acc_response + [array_current_pointer]
    if lis_pointers[current_pointer] == -1 and len(acc_response) == lis_value:
        return_value = acc_response
    elif lis_pointers[current_pointer] == -1 :
        return_value = value
    else:
        return_value = find_lis_sequence(
            array,
            lis_pointers,
            lis_pointers[current_pointer],
            value,
            lis_value
        )
    return return_value


def lis(array):
    l = len(array)
    LIS = [1] * l
    LIS_pointer = [-1] * l
    for i in range(1, l):
        current_pointer = 0
        max_lis_sub = 0
        for k in range(i):
            if array[k] < array[i]:
                if max_lis_sub <= LIS[k]:
                    current_pointer = k
                    max_lis_sub = LIS[k]
        LIS[i] = 1 + max_lis_sub
        LIS_pointer[i] = current_pointer
    lis_value = max(LIS)
    index_of_max_lis = LIS.index(lis_value)
    lis_sequence = find_lis_sequence(array, LIS_pointer, index_of_max_lis, [], lis_value )
    return (lis_value, lis_sequence) 


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    first_blank_line = sys.stdin.readline().strip()
    for _ in range(number_of_cases):
        heights_list = []
        current_heights = sys.stdin.readline().strip()
        while current_heights != "":
            heights_list.append(int(current_heights))
            current_heights = sys.stdin.readline().strip()
        number, sequence = (lis(heights_list))
        print(f'Max hits: {number}')
        for num in range(len(sequence) - 1, -1, -1) : 
            print(sequence[num])
        sys.stdout.write('\n')
