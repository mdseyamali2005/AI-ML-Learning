import json
with open("data.json","r") as f:
    py_disk = json.load(f)
    print(type(py_disk), py_disk)
####################
disk ={
    "babu": "khaichow",
    "age": 23,
    "i love you": True
}
with open("data.json", "w") as f:
    json.dump(disk,f, indent= 4, sort_keys= True)
####################
json_script = '{"Deya": "kahe","khana pina": true, "student": null}'
py_ob = json.loads(json_script)
print(type(json_script), type(py_ob), json_script, py_ob)
###################
disk ={
    "babu": "khaichow",
    "age": 23,
    "i love you": True
}
json_scr = json.dumps(disk)
print(type(json_scr), type(disk), json_scr)