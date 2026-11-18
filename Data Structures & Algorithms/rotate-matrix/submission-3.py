class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        k = n // 2

        for layer in range(k):
            for j in range(layer, n - 1 - layer):
                temp = matrix[j][n - 1 - layer]
                matrix[j][n - 1 - layer] = matrix[layer][j]

                _temp = matrix[n - 1 - layer][n - 1 - j]
                matrix[n - 1 - layer][n - 1 - j] = temp

                temp = matrix[n - 1 - j][layer]
                matrix[n - 1 - j][layer] = _temp

                matrix[layer][j] = temp