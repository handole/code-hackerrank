# menghitung nilai absolut antara jumlah diagonalnya
import sys

# n = int(input().strip())
# dSumLeft = 0
# dSumRight = 0
# for i in range(n):
# 	matrixRow = input().split(' ')
# 	dSumLeft += int(matrixRow[i])
# 	dSumRight += int(matrixRow[n-i-1])
# print(abs(dSumLeft - dSumRight))


# a = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
# jum1 = a[0][0] + a[1][1] + a[2][2]
# jum2 = a[0][2] + a[1][1] + a[2][0]
# print(jum2 - jum1)


def diagonalDifference(a):
    # Complete this function  
    sum1  = 0
    sum2  = 0
    for i in range(n):
        sum1 += int(a[i][i])
        sum2 += int(a[i][n-i-1])
    return abs(sum1 - sum2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)