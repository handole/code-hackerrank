# pencarian hitung dan cetak jumlah elemen dalam array, ingatlah bahwa beberapa bilangan bulat tersebut mungkin berukuran cukup besar.
import sys

def aVeryBigSum(n, ar):
	return reduce(lambda x, y: x + y, ar, 0)

def reduce(func, arr, s):
	for v in arr:
		s = func(s, v)
	return s
	

    # Complete this function

n = int(input('masukan nilai n:').strip())
ar = list(map(int, input('masukan nilai ar:').strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

