# def jumlahMatrik(self):
matrikA = [[3, -2], [4, 5]]
matrikB = [[4, -2], [8, 1]]
BarMatA = int(input())
KolMatA = int(input())

for i in range(BarMatA):
	for j in range(KolMatA):
		matrikhasil[i][j] = matrikA[i][j] + matrikB[i][j]

print('Matriks A : ', matrikA)
print('Matriks B : ', matrikB)
print('Hasil : ', matrikhasil)

# def kurangMatrik(self):
# 	for i in range(self.BarMatA):
# 		for j in range(self.KolMatA):
# 			self.matrikhasil[i][j] = self.matrikA[i][j] - self.matrikB[i][j]

# def kaliMatrik(self):
# 	for i in range(self.BarMatA):
# 		for j in range(self.KolMatA):
# 			self.matrikhasil[i][j] += self.matrikA[i][j] * self.matrikB[i][j]

