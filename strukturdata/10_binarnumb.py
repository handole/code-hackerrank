  # n = int(input())
# s = 0
# t = 0
# while (n > 0):
# 	remain = n % 2
# 	n = n / 2
# 	if remain == 1:
# 		s += 1
# 		if s >= t:
# 			t=s
# 	else:
# 		s=0


# print("00000010", 2)
# print("00000011", 2)

# n = int(input().strip())
# binary = []
# while n > 0:
# 	sisa = n % 2
# 	binary.append(sisa)
# 	n = n // 2
# print(binary)


# n = int(input().strip())
# binary = []
# while n > 0:
# 	sisa = n % 2
# 	binary.append(sisa)
# 	n = n // 2

# print(binary)

# def func(num):
# 	return num[2:]

# n = int(input().strip())
# a = max(func(bin(n)).split('0')).count('1')
# print(a)

# n = int(input())
# count = 0
# while n:
# 	n &= n << 1
# 	count += 1

# print(count)


# print(len(max(bin(n)[2:].split('0'))))


# n = int(input())
# remain = n % 2
# n = n / 2
# if remain == 1:
# 	s += 1
# 	if s >= t:
# 		t = s
# else:
# 	s = 0

# print(remain)
# print(n)

# n = int(input().strip())
# t = "{0:b}".format(n)
# print(max(map(len, t.split("0"))))

import sys

# def binsearch(n):
# 	c = 0
# 	ca = []
# 	for i in bin(n)[2:]:
# 		if i == "1":
# 			c += 1
# 		else:
# 			ca.append(c)
# 			c = 0
# 	ca.append(c)
# 	return max(ca)

# n = int(input().strip())
# print(binsearch(n))

n = int(input().strip())
c = 0
ca = []
for i in bin(n)[2:]:
	if i == "1":
		c += 1
	else:
		ca.append(c)
		c = 0
ca.append(c)

print(c)
# print(n)
