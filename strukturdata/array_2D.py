# a = [[2, 3, 4, 7, 3, 9],[2, 4, 6, 8, 4, 5]]

# # print(a[0])
# # print(a[1])

# # b = a[1]
# # print(b)

# # print(a[0][2])
# # print(a[0][1])

# # b[2] = 9
# # print(b)

# # for i in range(len(a)):
# # 	for j in range(len(a[i])):
# # 		print(a[i][j], end=' ')
# # 	print()

# # # sama fungsi, dengan handy feature row dan elem
# # for row in a:
# # 	for elem in row:
# # 		print(elem, end=' ')	
# # 	print()

# # # sama fungsinya, dengan method join
# # for row in a:
# # 	print(' '.join([str(elem) for elem in row]))


# # menggunakan 2 nested loop untuk menghitung jumlah semua nomor di array 2dimensi
# s = 0
# for i in range(len(a)): # looping untuk list array pertama
# 	for j in range(len(a[i])): # looping untuk list array kedua
# 		s += a[i][j] # proses penghitungan jumlahkan semua nomor di dalam list
# print(s)

# # menjumlahkan dengan iterating by elements, bukan dengan variabel
# s = 0
# for row in a:
# 	for elem in row:
# 		s += elem
# print(s)

# # alternatif lain dengan ganti variabel
# s = 0
# for baris in a:
# 	for kolom in baris:
# 		s += kolom
# print(s)

# m = 3
# n = 4
# # a = [[0] * m] * n
# # a[0][0] = 5
# # print(a[1][0])

# # membuat dan menambah list kosong baru
# a = []
# # for i in range(n):
# # 	a.append([0] * m)
# # print(a)

# a = [[0] * m for i in range(n)]
# print(a)


# cara input 2 dimensi array
# n = int(input()) # baris pertama adalah jumlah baris dari array
# a = []
# for i in range(n):
# 	a.append([int(j) for j in input().split()])

# print(a)

# atau tanpa melakkan panggilan yg canggih
# n = int(input())
# a = []
# for i in range(n):
# 	baris = input().split()
# 	for i in range(len(baris)):
# 		baris[i] = int(baris[i])
# 	a.append(baris)

# print(a)


# # dengan method generator
# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# print(a)


# memproses larik elemen 2 dimensi array
# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
# 	for j in range(n):
# 		if i < j:
# 			a[i][j] = 0
# 		elif i > j:
# 			a[i][j] = 2
# 		else:
# 			a[i][j] = 1

# for row in a:
# 	print(' '.join([str(elem) for elem in row])
# algoritma diatas terlalu lambat, karena menggunakan 2 loop untuk tiap pair(i, j), mengeksekusi satu atau dua if intruksi

# n = 6
# a = [[0] * n for i in range(n)]
# max = -100
# for i in range(n):
# 	a[i][i] = 1

# for i in range(n):
# 	for j in range(i + 1, n):
# 		a[i][j] = 0

# for i in range(n):
# 	for j in range(0, i):
# 		a[i][j] = 2



# for i in range(n):
# 	for j in range(0, i):
# 		a[i][j] = i * 1
# 		sum = a[i+1][j+1]
# 		for x in range(6):
# 			sum += a[i][j+x] + a[i+2][j+x]
# 		if sum > max:
# 			max = sum

# 	a[i][i] = i
# 	for j in range(i + 1, n):
# 		a[i][j] = j - 1

# print(max)



# # print(a)
# for row in a:
# 	print(' '.join([str(elem) for elem in row]))

# arr = []
# max = -100
# for i in range(4):
# 	for j in range(4):
# 		sum = arr[i+1][j+1]
# 		for x in range(3):
# 			sum += arr[i][j+x] + arr[i+2][j+x]
# 		if sum > max:
# 			max = sum
# print(max)

# n = 6
# a = [[0] * n for i in range(n)]

# for i in range(n):
# 	for j in range(0, i):
# 		a[i][j] = 1
# 	a[i][i] = 1

# 	for j in range(i + 1, n):
# 		a[i][j] = 2

# # print(a)
# for row in a:
# 	print(' '.join([str(elem) for elem in row]))

# def hourglass(a):
# 	for i in range(1, 5):
# 		for j in range(1, 5):
			
# 			a.append(hsum)

# total = sum(map(hourglass, a))
# print(total)


# print(total)
# for row in a:
# 	print(' '.join([(elem) for elem in row]))

# arr = []
# prod = []
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		hsum = sum(arr[i-1][j-1: j+2] + arr[i+1][j-1: j+2]) + arr[i][j]
# 		prod.append(hsum)

# print(max(prod))

	# for i in range(len(row)-2):
	# 	for j in range(len(row)-2):
	# 		row.append(row[i][j]+row[i][j+1]+row[i][j+2]+row[i+1][j+1]+row[i+2][j]+row[i+2][j+1]+row[i+2][j+2])

	# print(max(row))

# z = [[1, 3, 4, 5, 6], [1, 8, 5, 7]]
# total = sum(map(sum, z))
# print(total)




# Each line and column has 4 hourglasses (4 x 4 = 16)
#The minimum value of hourglasses' elements is -63
# maxi = -63

# for w in range(4): #This loop change the line
#     for x in range(4): #Help to scan hourglass elements
#         for y in range(3): #Line index of hourglass [0..2]
#             for z in range(x, 3 + x): #Element index
#             	# arr[1][0] and arr[1][2] are not summed 
#                 if y == 1 and (z == x or z == x + 2): 
#                     pass
#                 else:
#                     hourglass_sum += arr[y + w][z]
#         # Find the maixum valeu of sum
#         if maxi < hourglass_sum:
#             maxi = hourglass_sum
#             hourglass_sum = 0
#         else:
#             hourglass_sum = 0           

# print(maxi)

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

prod = []
for i in range(0, 4):
	for j in range(0, 4):
		prod.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]) 
		posisi = arr[i+2][j+2] # 4 4 0 0 2 4 0
print(max(prod))
print(posisi)


# sum = []
# h = 0
# for i in range(0, 4):
# 	for j in range(0, 4):
# 		sumTemp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
# 		posisi = arr[i+2][j+2]
# 		# if sumTemp > sum: sum = sumTemp
# 		# sum = sumTemp  # ini untuk sum tetap up to date 4 2 0 0 2 4 0
# 	sum.append(sumTemp)
# print(sum)
# print(posisi)

# a = [map(int, input().split()) for i in range(6)]
# print(max(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2] for j in range(4)))