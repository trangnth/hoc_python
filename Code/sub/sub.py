f = open('sub.txt', 'r')
g = open('sub1.txt', 'w')
while (str):
	str = f.readline()
	if str != '' and str[0].isalpha():
		g.write(str)
f.close()
g.close()
#target = open('se.txt', 'w')
#with open("sub.txt", "r") as ins:
 #   for line in ins:
  #  	if line[0].isalpha():
   #     	target.write(line)
#target.close()