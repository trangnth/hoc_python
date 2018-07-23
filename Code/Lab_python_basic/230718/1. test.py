hello = "Hello World!"
print(hello)

x = round(10 / 3, 1)
print(x)

x = "ha"
y = "hi"
print ('%s %s %d' % (x,y,10))

################# join()
join_str = "Meditech"
print (" ".join(join_str))

print (" ".join(reversed(join_str)))

join_list = ["toi", "la", "Trang"]
print (join_list)
print (" ".join(join_list))

################# split () ## Phan biet chu hoa va chu thuong
split_str = "ten toi la trang"
print (split_str.split(" "))
print (join_list[0].split("o"))
