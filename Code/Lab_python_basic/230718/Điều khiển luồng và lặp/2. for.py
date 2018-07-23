for x in 'Meditech':
    print (x)

qua = ['chuoi', 'tao', 'xoai']
for qua in qua:
    print (qua)

#### Cach duoi day cung tuong tu
for index in range(len(qua)):
   print ('Ban co thich an :', qua[index])

#### for and else
for num in range (10,20):
    for i in range (2,num):
        if num%i == 0:
            j = num /i
            print ('%d la bang %d * %d' % (num, i, j))
            break
    else:
        print (num, " la so nguyen to")
