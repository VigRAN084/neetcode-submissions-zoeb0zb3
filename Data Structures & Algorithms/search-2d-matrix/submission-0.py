class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        def convert1dTo2d(num: int) -> tuple[int, int]:
            row = num // len(matrix[0])
            col = num % len(matrix[0])
            return row, col

        l = 0
        r = rows * columns - 1

        while l <= r:
            m = (l + r) // 2
            mR, mC = convert1dTo2d(m)
            middleValue = matrix[mR][mC]

            if middleValue == target:
                return True
            elif target < middleValue:
                r = m - 1
            else:
                l = m + 1
        return False
