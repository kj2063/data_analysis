import json

d = {"name" : "권준"}
print(d["name"])

d_json = json.dumps(d,ensure_ascii=False)
d_dict = json.loads(d_json)

print(d_json)
print(d_dict)