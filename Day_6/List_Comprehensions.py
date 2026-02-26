number = [i*i for i in range(6)]
print(number)
################
number = [i*i for i in range(6) if (i*i)%2 != 0]
print(number)
###########################
value = [-1, -4, 4, 5, 56, -2, 5, -6]
value = [0 if i<0 else i for i in value]
print(value)
########################
word= ["seyam", "ali" , "manus", "sufia"]
word= [i.upper() for i in word]
print(word)