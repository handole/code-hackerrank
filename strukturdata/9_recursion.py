import sys

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     # Complete this function

# if __name__ == "__main__":
#     n = int(input().strip())
#     result = factorial(n)
#     print(result)


def main():
	num = int(input("Silahkan masukan bilangan bulat non negatif : " ))
	fact = factorial(num)
	print("faktorial dari ", num, "adalah : ", fact)

def factorial(num):
	if num == 0:
		return 1
	else:
		return num  * factorial(num - 1)

main()



# def faktorial2(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		res = n * faktorial2(n - 1)
# 		print("hasil untuk antara ", n, "* faktorial (", n-1, "):", res)
# 		return res

# print(faktorial2(3))

# def iteratif_faktorial(n):
# 	hasil = 1
# 	for i in range(2, n+1):
# 		hasil *= 1
# 	return hasil

# # print(faktorial2(5))
# print(iteratif_faktorial(3))

# def fib(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	else:
# 		return fib(n-1) + fib(n-2)

# n = int(input("Ini dari bilangan fibonaci = "))
# print(fib(n))

# from timeit import Timer
# from fibo import fib

# t1 = Timer("fib (10)", "dari fibo import fib")

# for i in range(1, 41):
# 	s = "fib (" + str(i) + ")"
# 	t1 = Timer (s, "dari fibo import fib ")
# 	time1 = t1.timeit(3)
# 	s = "fibi (" + str (i) + ")"
# 	t2 = Timer(s, "dari fibo import fibi ")
# 	time2 = t2.timeit(3)
# 	print("n =% 2d, fib:% 8.6f, fibi:% 7.6f, persen:% 10.2f" % (i, time1, time2, time1/time2))