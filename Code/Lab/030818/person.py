class Person:
	"ihaha"
	def __init__(self, name, age=1, gender="Male"):
		self.name=name
		self.age=age
		self.gender=gender

	def showInfo(self):
		print("Name:", self.name)
		print("Age:", self.age)
		print("Gender:", self.gender)
		