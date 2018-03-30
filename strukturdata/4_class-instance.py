class Person:
	
	def __init__(self, initialAge):
		# self.age = 0
		self.age = initialAge
		if self.age < 0:
			print("Age is not valid")
			self.age = 0
		# else:
		# 	initialAge = age

	def amIOld(self):
		if self.age in range(13):
			print("You are young.")
		elif self.age in range(13, 18):
			print("You are a teenager.")
		else:
			print("Youu are old.")


	# def amIOld(self):
	# 	if self.age < 13:
	# 		print("You are young")
	# 	elif 13 <= self.age < 18:
	# 		print("You are teenager")
	# 	else:
	# 		print("You are old")
			# Do some computations in here and print out the correct statement to the console

	def yearPasses(self):
		self.age += 1
		
		# Increment the age of the person in here   

t = int(input("masukan sampel: "))
for i in range(0, t):
	age = int(input("Usia : "))
	p = Person(age)
	p.amIOld()
	for j in range(0, 3):
		p.yearPasses()
	p.amIOld()
	print(" ")
		