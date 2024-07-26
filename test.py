import json
my_list = ['SuperHammerD','Frank','SuperHammerB', 'SuperHammerA']

# 将列表转换为 JSON 字符串
json_data = json.dumps(my_list)


print(json_data, type(json_data))
after = json.loads(json_data)
print(after, type(after))