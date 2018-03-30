import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# print(' '.join(map(str, reversed(arr)))

#arr.reverse() # reverse ini berfungsi untuk membalik daftar list
#print(*arr)   # pada * adalah intruksi untuk membongkar daftar, yg berarti 
			  # alih2 menyediakan elemen daftar dikelompokan dan menarik masing2 
			  # elemen dalam daftar adalah output dengan format yg berbeda oleh pernyataan print()

# if (n <= 1000 and n >= 1):						
# 	if(max(arr) <= 10000 and max(arr) >= 1):
# 		arr.reverse()
# 		print(" ".join(repr(e) for e in arr))  # join berfungi untuk mengonversikan list menjadi string 
# 											   # untuk melakukan penggabungan, dan dengan " " menjadi terpisah secara spasi

print(*arr[::-1]) # lebih simple dalam membagi list, tanda * adalah intruksi untuk membongkar list

# for x in range(len(arr)):
# 	print(arr[x],)

# arr.reverse()

# for r in reversed(arr):
# 	print(r)
# n = input().split()

# n = 4
# s = input()
# for r in reversed(s):
# 	print(r)

# for n in range(0, 4, 1):
# 	list = input()
# 	for list in reversed(n):
# 		print(list)

# for list in reversed(n):
# 	print(list)