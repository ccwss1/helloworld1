name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[0])
print(len(name_list))
print(name_list.count("zhangsan"))
name_list.append("chenliu")
print(name_list)
print(name_list.index("zhangsan"))
name_list[0] = "lalla"
print(name_list)
name_list.insert(1, "小明")
print(name_list)
temp_list = ["shashidi", "zhuerge", "youdage"]
name_list.extend(temp_list)
print(name_list)
name_list.remove("lalla")
print(name_list)
pop1=name_list.pop(3)
print(pop1)
print(name_list)
del name_list[0]
print(name_list)
name = "xiaoming"
# del 删除变量，后面不能在使用
del name
name_list.sort()
print(name_list)
name_list.reverse()
print(name_list)
a = name_list
print(a)
a.reverse()
print(a)
print(name_list)
import keyword
print(keyword.kwlist)

# 迭代遍历 顺序的从列表中依次获取数据，并保存在name变量中
for name in name_list:
    print("我的名字是 %s" % name)

print(type(name_list))