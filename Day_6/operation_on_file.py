f = open("sample.txt", "r") #here r is for read mode and w is for write mode and a is for append mode
# da = f.read()
# print(da)
data = f.readline()
print(data)
data1 = f.readline()
print(data1)
f.close()
##############
f = open("sample.txt") #r is default 
da = f.read()
print(da)
############# write mode ################(its will overwrite the existing data in the file)
f = open("sample.txt", "w") #here r is for read mode and w is for write mode and a is for append mode
f.write("this is my first line\nI am learning python.")
f.close()
############# append mode(a) ################(its will add the data in the file in last)
f = open("sample.txt", "a")
f.write("\nThis is new line\nI learn append mode")
f.close()
############### create new file mode x ##############
f = open("newfile.txt", "x") #it will create new file if file is already exist then it will give error
f.write("this is new file")
f.close()
#rb and wb are used for reading and writing binary files like images, videos, etc. and rt and wt are used for reading and writing text files. 
# and we dont need to use rt because text mode is default mode
############################ multiple mode use ######################### like r+ for r and w , w+ for w and r , a+ for a and r