__author__ = 'Mohammad'
"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which
order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative.
In other words, no matter how we parenthesize the product, the result will be the same.
For example, if we had four matrices A, B, C, and D, we would have:

(ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple
arithmetic operations needed to compute the product, or the efficiency. For example,
suppose A is a 10 x 30 matrix, B is a 30 x 5 matrix, and C is a 5 x 60 matrix. Then,

(AB)C = (10x30x5) + (10x5x60) = 1500 + 3000 = 4500 operations
A(BC) = (30x5x60) + (10x30x60) = 9000 + 18000 = 27000 operations.

Time Complexity: O(n^3)
Auxiliary Space: O(n^2)

http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
https://www.youtube.com/watch?v=vgLJZMUfnsU&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=3

"""

import sys
def MatrixChainOrder(arr, sz):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(sz)] for x in range(sz)]

    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is arr[i-1] x arr[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, sz):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, sz):
        for i in range(1, sz-L+1):
            j = i+L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][sz-1]

# Driver program to test above function
arr = [1, 2, 3 ,4]
arr = [2, 3, 6, 4, 5]
size = len(arr)

print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, size)))
# This Code is contributed by Bhavya Jain