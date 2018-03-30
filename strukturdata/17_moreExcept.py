
class Calculator:

	# def power(self, n, p):
	# 	self.n = n
	# 	self.p = p
	# 	if self.n < 0 or self.p < 0:
	# 		raise Exception("n and p should be non-negative") # raise Exception buat lempar error handling jika tidak terpenuhi
	# 	else:
	# 		return self.n ** self.p

	def power(self, n, p):
		if n < 0 or p < 0:
			raise Exception("n and p should be non-negative")  # raise Exception buat lempar error handling jika tidak terpenuhi
		return n ** p


myCalculator = Calculator()
T=int(input())
for i in range(T):
	n, p = map(int, input().split())  # map() berfungsi mengambil data berurutan(ex: tipe list), semua nilai yg ada langsung 
									  # dioperasikan pada suatu fungsi dan hasilnya langsung disimpan dalam bentuk iterator 
	try:
		ans=myCalculator.power(n, p)
		print(ans)
	except Exception as e:
		print(e)

