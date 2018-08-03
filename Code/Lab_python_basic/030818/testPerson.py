from person import Person
 
# Tạo một đối tượng Person.
aimee = Person("Aimee", 21, "Female")
 
 
aimee.showInfo()
 
print (" --------------- ")
 
# age, gender mặc định.
alice = Person( "Alice" )
 
alice.showInfo()
 
print (" --------------- ")
 
# gender mặc định.
tran = Person("Tran", 37)
 
tran.showInfo()

tran.age = 36

tran.showInfo()