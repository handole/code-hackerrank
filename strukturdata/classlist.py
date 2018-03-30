class Student:
	def __init__(self, firstName, lastName, idNum, kelas):
		self.firstName = firstName
		self.lastName = lastName
		self.idNum = idNum
		self.kelas = kelas

	def print_student(self):
		print("Name : {} {}".format(self.firstName, self.lastName))
		print("ID : {}".format(self.idNum))
		print("Kelas : {}".format(self.kelas))


class Mapel(Student):
	def __init__(self, mapel):
		super(Mapel, self).__init__(self, firstName, lastName, idNum, kelas)
		self.mapel = {}

	def addmapel(self, pelajaran, nilai):
		self.mapel[str(pelajaran)] = float(nilai)

	def printmapel(self):
		print('{} : {}'.format(self.pelajaran, self.nilai))
		
		

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
kelas = line[3]

s = Student(firstName, lastName, idNum, kelas)
s.print_student()
print(s)

mapel = dict(line.strip().split(" ") for line in range(input()))
