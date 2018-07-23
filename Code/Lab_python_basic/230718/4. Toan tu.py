# Toan tu membership: in va not in
# Kiem tra xem mot bien co nam trong day khong. Voi in, neu co trong day thi return true, khong thi return false

a = 20
b = 20
list=[10,20,30,40,50]

if (a in list):
    print ("a co trong list")
else: 
    print("a khong nam trong list")

if (b not in list):
    print ("b khong trong list da cho")
else:
    print ("b trong list da cho")



# Toan tu identify: is va is not
# Voi is, tra ve true neu cac bien o hai ben gia tri deu tro toi cung mot doi tuong, nguoc lai la false

if (a is b):
    print ('a,b co cung identity')
else:
    print ('a, b la khac nhau')

c = 10
if (a is c):
    print ('a, c co cung identity')
else:
    print ('a, c la khac nhau')



