name = input ('Enter file: ')
handle = open (name, 'r')
counts = dict()

for line in handle:
    words = line.split()
#    print (words)
    print (line)
#    for word in words:
#        print (word)
#        counts[words] = counts.get (word, 0) + 1
