import json

with open("student.json", "r") as f:
    data=json.load(f)

print(f"ism {data['ism']}")
print(f"yosh {data['yosh']}")
print(f"ball {data['ball']}")