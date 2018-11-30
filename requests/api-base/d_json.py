import json

d = dict(name="红楼梦",total=10,lend=10)
print(d)

d_json = json.dumps(d)

print(d_json)


d2 = json.loads(d_json)

print(d2)
