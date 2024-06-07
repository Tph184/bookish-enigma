#https://neetcode.io/problems/search-2d-matrix
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix[0]), len(matrix)
    top, bot = 0, COLS - 1
    while top <= bot:
        target_row_index = (top + bot) // 2
        '''
        Each row in matrix is sorted in non-decreasing order.
        The first integer of every row is greater than the last integer of the previous row.
        '''
        if target > matrix[target_row_index][-1]:
            top = target_row_index + 1
        elif target < matrix[target_row_index][0]:
            bot = target_row_index - 1
        else:
            break

    if not (top <= bot):
        return False
    target_row_index = (top + bot) // 2
    '''
    Binary Search
    '''
    low,high = 0, ROWS - 1
    while low <= high:
        mid = (low + high) // 2
        if target < matrix[target_row_index][mid]:
            high = mid - 1
        elif target > matrix[target_row_index][mid]:
            low = mid + 1
        else:
            return True
    
    return False


matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
print(searchMatrix(matrix=matrix, target=10))