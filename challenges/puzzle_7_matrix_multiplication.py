import numpy as np
from collections import namedtuple

class MatrixMultiplication:
    """ 
        The trivial solution to the matrix multiplication puzzle, of course it 
        won't pass the tests as it takes too much time. 
        https://www.topcoder.com/challenges/403cd499-d38e-4088-a6c6-b6de931a27b4
    """
    def __init__(self, n_rows, max_value):
        self.n_rows = n_rows
        self.max_value = max_value
        self.num_elements = self.n_rows ** 2

    def is_unique(self, matrix):
        return self.num_elements == len(set(matrix.flatten()))

    def rec(self, index, matrix):
        if index == self.num_elements:
            yield matrix
            return

        i = index // self.n_rows
        j = index % self.n_rows

        for value in range(1, self.max_value + 1):
            matrix[i, j] = value
            yield from self.rec(index + 1, matrix)

    def run(self):
        A = np.zeros((self.n_rows, self.n_rows), dtype=int)
        B = np.zeros((self.n_rows, self.n_rows), dtype=int)
        min_A, min_B, min_C, min_sum = None, None, None, 10 ** 6

        for sample_A in self.rec(0, A):
            for sample_B in self.rec(0, B):
                C = np.matmul(sample_A, sample_B)
                if self.is_unique(C):
                    c_sum = np.sum(C)
                    if c_sum < min_sum:
                        min_sum = c_sum
                        min_C = C
                        min_A = np.copy(sample_A)
                        min_B = np.copy(sample_B)

        Result = namedtuple("Result", ["min_A", "min_B", "min_C", "min_sum"])
        result = Result(min_A=min_A, min_B=min_B, min_C=min_C, min_sum=min_sum)

        return result

challenge = MatrixMultiplication(n_rows=2, max_value=3)
result = challenge.run()

min_A = result.min_A
min_B = result.min_B
min_C = result.min_C
min_sum = result.min_sum
print( f"A:\n{min_A}\n\n"
        f"B:\n{min_B}\n\n"
        f"C:\n{min_C}\n\n" 
        f"Sum:{min_sum}")