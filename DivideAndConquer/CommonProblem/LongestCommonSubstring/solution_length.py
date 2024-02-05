# Given two strings LCS_length returns the length of the LCS of both strings


def LCSubstring_length(
    left: str, right: str, left_pointer: int = 0, right_pointer: int = 0
) -> int:
    return_value = 0
    if left_pointer >= len(left) or right_pointer >= len(right):
        return_value = acc
    elif left[left_pointer] == right[right_pointer]:
        return_value = LCSubsequence_length(
            left, right, left_pointer + 1, right_pointer + 1, acc + 1
        )
    elif left[left_pointer] != right[right_pointer]:
        return_value = max(
            LCSubsequence_length(left, right, left_pointer + 1, right_pointer),
            LCSubsequence_length(left, right, left_pointer, right_pointer + 1),
            acc
        )
    return return_value


print(LCS_length("fas0000fadffffffff1232", "0000Faffffffdf"))
