class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # returns set of nums
        def possibles(i, j):
            ret = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            row_nums = {cell for cell in board[i] if cell != '.'}
            ret = ret.difference(row_nums)
            col_nums = {cell for cell in [row[j] for row in board] if cell != '.'}
            ret = ret.difference(col_nums)

            big_r = i // 3
            big_c = j // 3
            for r in range(3 * big_r, 3 * (big_r + 1)):
                for c in range(3 * big_c, 3 * (big_c + 1)):
                    if board[r][c] != '.' and board[r][c] in ret:
                        ret.remove(board[r][c])
            return ret

        def backtrack():
            target = (-1, -1)
            target_options = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    cand_set = possibles(i, j)
                    if len(cand_set) < len(target_options):
                        target_options = cand_set
                        target = (i, j)
            if target == (-1, -1):
                return True  # end

            for option in target_options:
                board[target[0]][target[1]] = option
                if backtrack():
                    return True
                board[target[0]][target[1]] = '.'

            return False  # not solvable

        backtrack()


# s = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# s.solveSudoku(board)
# for row in board:
#     print(row)
