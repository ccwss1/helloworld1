xiaoming = {"name": "xiaoming", "age": 18, "gender": True, "height": 1.75}
print(xiaoming["name"])
xiaoming["age"] = 24
print(xiaoming)
xiaoming["weight"] = 75
print(xiaoming)
xiaoming.pop("gender")
print(xiaoming)
print(len(xiaoming))
temp_dict = {"like": "reading"}
xiaoming.update(temp_dict)
print(xiaoming)

for k in xiaoming:
    print("%s :%s"% (k, xiaoming[k]))

# 字典和列表的组合，将多个字典放在一个列表中，在进行遍历
card_list = [{"name": "xiaoming", "qq": "79989", "age": 18}, {"name": "zhangsan", "qq": "90909", "age": 24}]
for card_info in card_list:
    print(card_info)
