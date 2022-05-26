import json

json_data = {"interface" : {"name" : "Gigabitethernet 0/0/1", "description" : "to JBias-CR1 Gi1/0/2", "ipv4": {"address" : {"ip" : "192.168.1.1", "netmaks" : "255.255.255.0"}}}}

with open("C:\\Users\\toolg\\Documents\json_example.json", "w") as data:
    json.dump(json_data, data, indent = 4)

