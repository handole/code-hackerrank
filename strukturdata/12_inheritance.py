# class Person:
# 	def __init__(self, first, last, id):
# 		self.first_name = first
# 		self.last_name = last
# 		self.id = str(id)

# 	def name(self):
# 		return self.last_name + ", " + self.first_name + ", " + self.id

# class Student(Person):
# 	def __init__(self, first, last, id):
# 		super().__init__(first, last, id)

# 	def grades(self):
# 		self.grade = []


# 	def get_student(self):
# 		return self.name() + ", " + self.grades()
	

# a = Person("Jya", "hesu", "001")
# b = Student("Luke", "Swan", "002", 90, 70)
# print(a.name())
# print(b.get_student())

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name: ", self.lastName + ", " + self.firstName)
		print("ID: ", self.idNumber)


class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		super(Student, self).__init__(firstName, lastName, idNumber)
		self.scores = scores
		

	def calculate(self):
		num = sum(self.scores)/len(self.scores)
		if num >= 90:
			return "O"
		elif num >= 80:
			return "E"
		elif num >= 70:
			return "A"
		elif num >= 55:
			return "P"
		elif num >= 40:
			return "D"
		else:
			return "T"



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]

numScore = int(input())  # tidak dibutuhkan di python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
