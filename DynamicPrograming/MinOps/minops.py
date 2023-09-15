#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import stdin, stdout


def min_operation_DC(w1, w2, pointer1, pointer2):
    if pointer1 == 0:
        result = pointer2 + 2
    elif pointer2 == 0:
        result = pointer1 + 2
    else:
        if w1[pointer1] == w2[pointer2]:
            result = min_operation_DC(w1, w2, pointer1 - 1, pointer2 - 1)
        else:
            insert = min_operation_DC(w1, w2, pointer1, pointer2 - 1) + 1
            delete = min_operation_DC(w1, w2, pointer1 - 1, pointer2) + 1
            result = min(insert, delete)
    return result


def main():
    number = int(stdin.readline().strip())
    original_number = number
    while number > 0:
        current_len = int(stdin.readline().strip())
        current_len -= 1
        w1 = [''] + stdin.readline().split()
        w2 = [''] + stdin.readline().split()
        result = min_operation_DC(w1, w2, current_len, current_len)
        current_case = original_number - number + 1
        print(f'Caso-{current_case}: {result}')
        number -= 1


if __name__ == '__main__':
    main()
