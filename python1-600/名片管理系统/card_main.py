import card_tools
# 显示功能菜单,todo可以提示将要完成的任务
card_tools.show_menu()
while True:
    action = int(input("请输入希望执行的操作："))
    print("您选择的操作是【%d】" % action)

    if action in [1, 2, 3]:
        # TODO 新增名片
        if action == 1:
            card_tools.new_card()
        # TODO 显示全部
        elif action == 2:
            card_tools.show_all()
        # TODO 查询名片
        elif action == 3:
            card_tools.search_card()
    elif action == 0:
        # 如果不希望立刻编写分支内部的代码，可以使用pass关键字
        # pass表示一个占位符，不会执行任何操作，为了报证代码结构正确
        # pass
        print("本次已退出，欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请重新选择")
