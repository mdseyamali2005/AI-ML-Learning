f = open("sample.txt", "r") #here r is for read mode and w is for write mode and a is for append mode
# da = f.read()
# print(da)
data = f.readline()
print(data)
data1 = f.readline()
print(data1)
f.close()