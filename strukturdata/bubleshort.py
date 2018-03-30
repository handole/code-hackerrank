import sys

n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# n_swap = 0

# # Write Your Code Here
# for i in range(len(a) - 1):
#     for j in range(0, len(a) - i - 1):
#         if (a[j] > a[j+1]):
#             a[j], a[j+1] = a[j+1],a[j]
#             n_swap += 1

# print('Array is sorted in '+ str(n_swap) + ' swaps.')
# print('First Element: '+ str(a[0]))
# print('Last Element: ' + str(a[-1]))

# # def bubleshort(arr):
# # 	n = len(arr)

# # 	for i in range(n):
# # 		for j in range(0, n-i-1):

# # 			if arr[j] > arr[j+1]:
# # 				arr[j], arr[j+1] = arr[	j+1], arr[j]

# # n = list(input().strip())
# # arr = list(map(int, input().strip().split(' ')))
# # bubleshort(arr)

# # print("Shorted array is : ")
# # for i in range(len(arr)):
# # 	print("%d" %arr[i]),

# # # bublesort(arr)
# # print("Array is sorted in {} swaps".format(i))
# # print("First element: {}".format(arr[0]))
# # print("Las elemen: {}".format(arr[]))


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swapcount = 0
for passnum in range(len(a) - 1, 0, -1):
	for i in range(passnum):
		if a[i] > a[i+1]:
			temp = a[i]
			a[i] = a[i+1]
			a[i+1] = temp
			swapcount += 1
# return swapcount



# bublesort(a)
# numswap = bublesort(temp)
# print(numswap)
print("Array is sorted in {} swaps.".format(swapcount))
# for j in range(len(a)):
# 	# print("%d" %a[j])
print("First element: {}".format(a[0]))
print("Last element: {}".format(a[-1]))


# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# # Write Your Code Here
# numSwaps = 0

# for i in range(n):
#     for j in range(i+1, n):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
#             numSwaps += 1

# print('Array is sorted in', numSwaps, 'swaps.')
# print('First Element:', a[0])
# print('Last Element:', a[-1])