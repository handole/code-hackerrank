S1 = ['H', 'a', 'c', 'k', 'e', 'r']
S2 = ['R', 'a', 'n', 'k']

for N in range(int(input())):  # input N untuk banyaknya list yg akan diinput
	S = input()   # untuk input string
	print(S[::2], S[1::2])  # S pertama menyatakan jangkauan perulangan diawali 0, diakhir tak terhingga, dengan nilai langkah 2
							# S kedua menyatakan diawali 1 diakhiri tak terhingga, dengan nilai langkah 2
	# print(S[1::3])