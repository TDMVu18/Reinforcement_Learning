f = open('nenxau.inp','r')
g = open('nenxau.out','w')

newstring = ''
count = 1
string = f.readline()

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        newstring += str(count) + string[i - 1]
        count = 1

newstring += str(count) + string[-1]

print(string)
print(newstring)
print(newstring, file=g)

f.close()
g.close()