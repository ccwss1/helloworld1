str1 = "hello python"
# 一般用“ ”，如果字符串里有“”，可以用‘’定义字符串
print(len(str1))
print(str1[6])
for char in str1:
    print(char)
print(str1.count("he"))
print(str1.index("py"))
print(str1.isupper())
print(str1.islower())

# 1.是否空白字符,空格，制表符也属于空白字符
space_str = "  \n\t\r"
print(space_str.isspace())

# 2.判断字符串中是否只包含数字,从上到下范围越来越大
# 都不能判断小数
# unicode 字符串 num_str = "\u00b2"
# num_str = "一千零一"
num_str = "1"
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 3.查找和替换
hello_str = "hello world"
# 是否以hello开始字符串，结束字符串，查找，替换
print(hello_str.startswith("hello"))
print(hello_str.endswith("world"))
print(hello_str.find("llo", 1, 4))  # 不存在会返回-1，index不存在会返回error
print(hello_str.replace("world", "python"))  # replace后会返回一个新的字符串，不会修改原始的字符串
print(hello_str)
print(hello_str.rfind("llo"))
print(hello_str.index("ld"))
print(hello_str.rindex("ld"))  # 从右边开始查找

# 4.文本对齐演练
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"]
for sentence in poem:
    # 5.去除空白字符,strip方法
    print("|%s|" % sentence.strip().center(10, " "))

# 6.字符串拆分和连接
poem_str = "\t\n登鹳雀楼\t 王之涣 \t \n 白日依山尽 黄河入海流 \t \n 欲穷千里目 更上一层楼"
print(poem_str)
poem_list = poem_str.split()
print(poem_list)
print(" ".join(poem_list))

# 7.切片,左闭右开
python_str = "0123456789"
print(python_str[2:6])
print(python_str[2:])
print(python_str[:6])
print(python_str[:])
print(python_str[::2])
print(python_str[1::2])
print(python_str[-1])
print(python_str[2:-1])
print(python_str[-2:])
print(python_str[::-1])


