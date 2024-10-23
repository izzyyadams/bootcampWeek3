class Solution(object):
    def setZeroes(self, matrix):
        rowIndices = []
        columnIndices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowIndices.append(i)
                    columnIndices.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowIndices:
                    matrix[i][j] = 0
                if j in columnIndices:
                    matrix[i][j] = 0

        
