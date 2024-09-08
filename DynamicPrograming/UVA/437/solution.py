import sys


def read_list_block(current_number_of_blocks) -> list[list[int]]:
    current_list_of_blocks = []
    for _ in range(current_number_of_blocks):
        current_block = list(map(int, sys.stdin.readline().split()))
        # As each block can be rotate (3 times per block) the idea is to have a 'big'
        # list that contains all the 3 rotations of all the input blocks,
        # Such list is return sorted by the base are of the block, the idea is to solve
        # the problem using LIS then we need a sorted list to do so. Not because LIS
        # requiere a sorted list, rather because is we sort the list of blocks we make
        # 'easy' to find greatest LIS
        current_list_of_blocks += generate_all_rotations_of_block(current_block)
    current_list_of_blocks.sort(key=lambda b: b[3], reverse=True)
    return  current_list_of_blocks


def generate_all_rotations_of_block(block: list[int]) -> list[list[int]]:
    # Sorry I am lazy, this could be done in a more clever way... just three cases...
    # This problems screams to uses objects as representation of the blocks
    # correction to the last comment: I am lazy and stubborn :)

    # The first two position of the block correspond to the base of the rotation, the
    # third is the height and the last position is the area of such rotation.
    return [
        [block[0], block[1], block[2], block[0] * block[1]],
        [block[1], block[2], block[0], block[1] * block[2]],
        [block[2], block[0], block[1], block[2] * block[0]],
    ]

def block_less_than(block_1: list[int], block_2: list[int]) -> bool:
    # This function defines when block_1 < block_2 based on the two possible conditions
    # This one is a tricky one, the first is 'obvious' but the second one is because
    # you may rotate the block in the 2d plane, to solve this you could add more block
    # in the generation of rotations, or you could do this 
    return (block_1[0] < block_2[0] and block_1[1] < block_2[1]) or \
           (block_1[0] < block_2[1] and block_1[1] < block_2[0])

def lis(array):
    # This time LIS requieres a slight modification. The general problem counts the 
    # longest increasing subsequence (obviously) and return such length but now we need to
    # take the LIS and return the sum of the height of the block in the LIS 

    l = len(array)
    #  As mention before, now the bases cases are the height of the blocks
    LIS = []
    for b in array:
        LIS.append(b[2]) # another reason to use oop

    for i in range(1,l):
        for k in range(i):
            if block_less_than(array[i], array[k]):
                # Here another 'modification' to the original LIS, need to add the height
                LIS[i] =  max(LIS[i],LIS[k] + array[i][2]) # another reason to use oop
    return max(LIS) 


if __name__ == "__main__":
    # If you are looking for competitive programming like code, this is not the repo for you.
    # I made some implementations decision that a competitive programmer might hate
    # this try off is just for the seek of readability and understandability for a
    # a student new in DP.
    counter = 0
    current_number_of_blocks = int(sys.stdin.readline().strip())
    while current_number_of_blocks != 0:
        counter += 1

        current_list_blocks = read_list_block(current_number_of_blocks)
        current_result = lis(current_list_blocks)
        print(f'Case {counter}: maximum height = {current_result}')

        current_number_of_blocks = int(sys.stdin.readline().strip())
