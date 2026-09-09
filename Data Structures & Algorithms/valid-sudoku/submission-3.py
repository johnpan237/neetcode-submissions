class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_number = board[r][c]
                if current_number == '.':
                    continue
                if (current_number in cols[c] or
                    current_number in rows[r] or
                    current_number in squares[(r//3, c//3)]):
                    return False
                cols[c].add(current_number)
                rows[r].add(current_number)
                squares[(r//3, c//3)].add(current_number)
        
        return True