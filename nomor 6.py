#No.6
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1,12, 5, 9]
c = a[0:7]
d = b[2:9]

i = 0
e = []
for x in c :
    hasil = (c[i] + d[i])
    e.append(hasil)
    i += 1
print(e)
