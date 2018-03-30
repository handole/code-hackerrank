#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

# sum = [0] * 16

# for i in range(16):
# 	sum[i] += sum(arr[i//4][i%4:i%4+3]) + sum(arr[i//4+2][i%4:i%4+3]) + arr[i//4+1][i%4 + 1]
# print(max(sum))


# arr = []
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)


def sum_hourglass(a, b, m, n):
	sum = 0
	for i in range(1, 5):
		sum = sum+a[i]+ b[i]
	return sum

def hourglass(a):
	ans = []
	for i in range(1, 5):
		for j in range(1, 5):
			s = sum_hourglass(a[i-1], a[i+1], j-1, j+1)
			ans.append(s+a[i][j])
	return max(ans)

total = hourglass(arr)
	
print(total)

# total = sum_hourglass(arr)
# print(total)