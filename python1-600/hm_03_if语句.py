# age = int(input("请输入你的年龄："))
#
# if age >= 18:
#     print("你可以进网吧嗨皮了")
# else :
#     print("赶紧回家写作业")
#
#
# # 逻辑运算符 and or not
# age = 1000
# if age >= 0 and age <= 120:
#     print("年龄正确")
#
# is_empolyee = True
# if not is_empolyee :
#     print("不允许入内")

# elif 语句 希望判断多个条件
# age = 40
#
# if age >= 0 and age <= 120 :
#     print("您的年龄正确")
# elif age > 50 :
#     print("你真长寿")
# else :
#     print("emmm")

has_ticket = bool(input("请输入是否有车票："))
knife_length=int(input("请输入刀的长度："))

if has_ticket :
    print("您已买票，可以安检")
    if knife_length <= 20 :
        print("安检完成，祝您旅途愉快")
    else :
        print("携带危险物品，刀的长度为 %d 公分，不能上车" % knife_length)

else :
    print("请先买票")