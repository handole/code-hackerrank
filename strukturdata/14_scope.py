class Difference:
	def __init__(self, a):
		self.__elements = a

	# add function
	def computeDifference(self):
		# maxElement = max(self.__elements)
		# minElement = min(self.__elements)
		self.maximumDifference = (max(self.__elements) - min(self.__elements)) # mengambil nilai terbesar dan terkecil dalam list lalu dikurangi



# end of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)