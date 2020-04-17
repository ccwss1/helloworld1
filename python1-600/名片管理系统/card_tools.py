def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("*" * 50)


card_list = []


def new_card():
    """ 新增名片 """
    print("-" * 50)
    print("新增名片")
    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    # 2. 使用用户信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone,
                 "QQ": qq,
                 "email": email}
    # 3. 将名片添加到列表中
    card_list.append(card_dict)
    print(card_dict)
    # 4.提示用户添加成功
    print("您已成功添加名片")


def show_all():
    """ 显示所有名片 """
    print("-" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("没有名片记录，将返回")
        # return可以返回一个函数的返回值，下方的代码不会被执行
        # return后面没有任何内容，则会返回到函数调用的位置，不会返回任何结果
        return
    # 打印表头
    for name in ["name", "phone", "QQ", "email"]:
        print(name, end="\t\t")
    print("")
    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["email"]))


def search_card():
    """ 查询名片
    """
    # 1.提示用户要搜索的名字
    search_name = input("请输入想查询的名片名字")
    # 2. 遍历名片列表
    for card1 in card_list:
        if search_name == card1["name"]:
            print("找到了")
            print("name\t\tphone\t\tQQ\t\temail")
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card1["name"],
                                                card1["phone"],
                                                card1["QQ"],
                                                card1["email"]))
            #  针对找到的名片进行修改和删除操作
            deal_card(card1)
            break
    else:
        print("%s 没有找到" % search_name)
    print("-" * 50)
    print("查询名片")


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict:查找到的名片
    """
    action1 = input("请输入您希望的操作：1 修改名片，2 删除名片，0 返回上一级菜单")
    if action1 == "1":
        revise_info = input("请输入需要修改的项：1 name 2 phone 3 QQ 4 email")
        if revise_info == "1":
            find_dict["name"] = input_card_info(find_dict["name"],"name:")
        elif revise_info == "2":
            find_dict["phone"] = input_card_info(find_dict["phone"],"phone")
        elif revise_info == "3":
            find_dict["QQ"] = input_card_info(find_dict["QQ"],"QQ")
        else:
            find_dict["email"] = input("email")
        print("修改名片成功")
    elif action1 == "2":
        card_list.remove(find_dict)
        print("删除成功")


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return:
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.输入判断，如果输入了直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果没有输入返回字典中原有的值
    else:
        return dict_value
