import json
f1 = open("./Periodic-Table-JSON/PeriodicTableJSON.json", 'rb')
f2 = open("./Periodic-Table-JSON/new_table.json", "a+")
f1_json = json.load(f1)
json_temp = {}
for json_data in f1_json["elements"]:
    json_temp["symbol"] = json_data["symbol"]
    json_temp["name"] = json_data["name"]
    json_temp["number"] = json_data["number"]
    json_temp["row"] = json_data["ypos"]
    json_temp["column"] = json_data["xpos"]
    js = json.dumps(json_temp, indent=4, sort_keys = False)
    js1 = js + ',' + '\n'
    f2.writelines(js1)

