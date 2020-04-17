# 文件被分为文本文件，可以直接被文本编辑器打开，例如txt
# 二进制文件，提供给其他软件使用,例如图片，音频
# 本质上都是二进制文件存在硬盘里
# 打开open文件，读read写write文件，关闭close文件


# 读写数据
# file = open("readme", "w")
# file = open("readme", "r")
# # 文件指针 标记从哪个位置开始读取数据
# text = file.read()  # 一次读取全部
# print(text)
# print("-"*50)
# file.write("nihao")
# retext = file.read()
# print(retext)
# file.close()


# # readline 一次读取一行
# file = open("readme")
#
# while True:
#     text = file.readline()
#     if text:
#         print(text)
#     else:
#         break
#
# file.close()


# 复制小文件
# file_read = open("readme")
# file_write = open("readme[cp]", "w")
# text = file_read.read()
# file_write.write(text)
# file_read.close()
# file_write.close()


# 复制大文件，可以一行一行的操作
file_read = open("readme")
file_write = open("readme[cp]", "w")
while True:
    text = file_read.read()
    if not text:
        break
    file_write.write(text)
file_read.close()
file_write.close()
