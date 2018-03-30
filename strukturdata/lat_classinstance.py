class Pets:
	name = "Pet animals"

	@classmethod
	def about(cls):
		print("This class is about {}!".format(cls.name))

class Dogs(Pets):
	name = "'a man's best friends' (Frederick II)"

class Cats(Pets):
	name = "cats"

p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()







# class Fraction(object):

# 	def __init__(self, n,d):
# 		self.numerator, self.denominator = Fraction.reduce(n, d)

# 	@staticmethod
# 	def gcd(a, b):
# 		while b != 0:
# 			a, b = b, a%b
# 		return a

# 	@classmethod
# 	def reduce(cls, n1, n2):
# 		g = cls.gcd(n1, n2)
# 		return (n1 // g, n2 // g)

# 	def __str__(self):
# 		return str(self.numerator)+'/'+str(self.denominator)


# x = Fraction(8, 24)
# print(x)



# class Robot:
# 	__counter = 0

# 	def __init__(self):
# 		type(self).__counter += 1

# 	@classmethod
# 	def RobotIntsance(cls):
# 		return cls, Robot.__counter

# if __name__ == '__main__':
# 	print(Robot.RobotIntsance())
# 	x = Robot()
# 	print(x.RobotIntsance())

# 	y = Robot()
# 	print(y.RobotIntsance())
# 	print(Robot.RobotIntsance())

# Robot.RobotIntsance()

# x = Robot()
# x.RobotIntsance()


# 	Three_laws = (
# """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
# """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
# """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
# 		)

# 	def __init__(self, name, build, build_year):
# 		self.name = name
# 		self.build_year = build_year


# for number, text in enumerate(Robot.Three_laws):
# 	print(str(number+1) + ":\n" + text)

# class C:
# 	counter = 0

# 	def __init__(self):
# 		type(self).counter += 1

# 	def __del__(self):
# 		type(self).counter -= 1

# if __name__ == '__main__':
# 	x = C()
# 	print("Number of instance: x : " + str(C.counter))
# 	y = C()
# 	print("Number of instance: y : " + str(C.counter))
# 	del x
# 	print("Number of instance: x : " + str(C.counter))
# 	del y
# 	print("Number of instance: y : " + str(C.counter))
