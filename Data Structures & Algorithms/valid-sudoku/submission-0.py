class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            columnCount = defaultdict(int)
            for column in row:
                if column != "." and columnCount[column]==1:
                    return False
                columnCount[column]+=1

        for column in range(9):
            rowCount = defaultdict(int)
            for row in board:
                if row[column] != "." and rowCount[row[column]]==1:
                    return False
                rowCount[row[column]] += 1

        squareCount= defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in squareCount[(row//3,col//3)]):
                    return False
                squareCount[(row//3,col//3)].add(board[row][col])
        return True