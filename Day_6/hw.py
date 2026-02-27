##q1########
with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter a name: ")
        f.write(name + "\n")
with open("names.txt", "r") as f:
    print("Names in file:")
    print(f.read())
#####q2########
with open("log.txt","a") as f:
    f.write("\nProgram run successfully")
with open("log.txt","r") as f:
    print(f.read())
#########q3##########
number =  [5, 10, 15, 20, 25]
number = [val for val in number if val>15]
print(number)

#########q4###########
import json
city = {
    "Dhaka": 34234,
    "Rangpur": 56354,
    "Barishal": 34523453
}
with open("cities.json", "w") as f:
    json.dump(city, f, indent = 4, sort_keys = True)
###
import json
with open("cities.json", "r") as f:
    disk = json.load(f)
    print(disk)
####
import json
try:
    with open("cities.json", "r")as f:
        data= json.load(f)
except:
    data={}

finally:
    print(data)

inp = input("You want to give input write yes or no: ")
if inp == "yes":
    ci = input("enter the city name: ")
    nu = int(input("Enter the number: "))
    data[ci] = nu
    with open("cities.json","w") as f:
        json.dump(data,f, indent = 4, sort_keys = True)
else:
    print("No data entered.")
#############q5####################
try:
    with open("dea.txt", "r") as f:
        hga = f.read()
        print(f"file is exist{hga}")
except:
    print(f"file dose not extst")
