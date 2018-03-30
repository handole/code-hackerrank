import sys

N = int(input().strip())

if N >= 1 and N <= 100:
	if N % 2 != 0:
		print("weird")
	elif N % 2 == 0 and (N >= 2 and N <= 5):
		print("not weird")
	elif N % 2 == 0 and (N >= 6 and N <= 20):
		print("weird")
	elif N % 2 == 0 and N > 20:
		print("not weird")


# print('weird' if N % 2 != 0 or 6 <= N <= 20 else 'not weird')

# print("Not " * (lambda x: x % 2 == (5 < x < 21)) (input()) + "weird")

# ans = 'weird'

# if n % 2 == 0 and not  6 <= n <=20:
# 	ans = 'Not ' + ans

# print(ans)



# for num in range(1, 20, 2):
	# print('{} weird'.format(n))

# for n in range(2, 5, 2):
# 	print('{} not weird'.format(n))

# for n in range(6, 20, 2):
# 	print('{} weird'.format(n))

# for n in range(20, 100, 2):
# 	print('{} not weird'.format(n))

# if n == 'weird':
# 	for n in range(1, 20, 2):
# 		print('{} weird'.format(n))