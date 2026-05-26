word = input("What you want to fined: ")
data = True
line = 1
with open("sample.txt", "r") as f:
    while data:
        data = f.readline()
        if (word in data):
            print(f"{word} is found in {line}")
            break
        line +=1
