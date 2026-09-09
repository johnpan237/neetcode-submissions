class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            row_smallest = matrix[row][0]
            row_largest = matrix[row][-1]

            if target > row_largest:
                top = row + 1
            elif target < row_smallest:
                bot = row - 1
            else:
                break
        
        row = (top + bot) // 2

        l, r = 0, COLS - 1

        while l <= r:
            middle_index = (l + r) // 2
            middle_number = matrix[row][middle_index]
            if target > middle_number:
                l = middle_index + 1
            elif target < middle_number:
                r = middle_index - 1
            else:
                return True
        
        return False

        # Time Complexity: O(log(m * n)) where m is the number of rows, and n is the number of columns
        # Space Complexity: O(1)
