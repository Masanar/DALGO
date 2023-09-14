#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import stdin, stdout


def conquer(distance: int, years: list[int], start_left: int,
            start_right: int) -> list[int]:
    _len = len(years)
    left_pointer = start_left
    right_pointer = start_right
    flag = True
    ans = [1, 0, 0]
    while (left_pointer < start_right and right_pointer < _len) and flag:
        current_distance = years[right_pointer] - years[left_pointer]
        number_of_kings = right_pointer - left_pointer + 1
        if current_distance < distance and right_pointer < _len:
            if number_of_kings >= ans[0]:
                ans = [number_of_kings, left_pointer, right_pointer]
            right_pointer += 1
        elif left_pointer < start_right - 1:
            left_pointer += 1
        else:
            flag = False
        
    return ans


def divide(years_d: int, king_years: list[int], start: int,
           end: int) -> list[int]:
    if start == end:
        return [1, start, end]
    if abs(start - end) < 2:
        if king_years[end] - king_years[start] <= years_d:
            return [2, start, end]
        else:
            return [1, start, end]
    mid = (start + end) // 2
    left = divide(years_d, king_years, start, mid - 1)
    right = divide(years_d, king_years, mid + 1, end)
    crossing = conquer(years_d, king_years, start, mid + 1)
    results = [left, right, crossing]
    results.sort(key=lambda x: x[1])
    return max(results, key=lambda x: x[0])


def main():
    Years = stdin.readline().strip()
    while Years != '':
        New_King_years = []
        Kings = int(stdin.readline().strip())
        for _ in range(0, Kings):
            year = int(stdin.readline().strip())
            New_King_years.append(year)

        result = divide(int(Years), New_King_years, 0, Kings - 1)
        # I don't like the next three lines
        results = [
            result[0], New_King_years[result[1]], New_King_years[result[2]]
        ]
        results_str = ' '.join(str(x) for x in results)
        print(results_str)
        #  stdout.write(' '.join(str(x) for x in result))
        Years = stdin.readline().strip()
        Years = stdin.readline().strip()


if __name__ == '__main__':
    main()
