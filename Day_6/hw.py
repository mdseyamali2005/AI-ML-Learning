##q1########
with open("name.txt", "w") as f:
    f.write("Seyam\nsufia\nkhatun\nali\nMira\n")
#####q2########
with open("log.txt","a") as f:
    f.write("\nProgram run successfully")
with open("log.txt","r") as f:
    print(f.read())