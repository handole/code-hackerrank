import sys

# perbandingan nilai a dan b dalam array, jika a0 > b0 maka a dapat point 1 dan jika a0 < b0 maka b dapat poit 1
def solve(a0, a1, a2, b0, b1, b2):
	# a = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
	# b = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
	# return (a, b)
	nilai = [0, 0] 
	a = [a0, a1, a2]
	b = [b0, b1, b2]
	for i in range(3):  # looping nilai
		if a[i] > b[i]:
			nilai[0] += 1
		if a[i] < b[i]:
			nilai[1] += 1

	return nilai

    # Complete this function

a0, a1, a2 = input("Masukan nilai a:").strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input("masukan nilain b:").strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))