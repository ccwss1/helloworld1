# ASCII编码一共有256个字符，一个字符占一个字节，一个字节是8位的0/1串
# UTF-8 使用1-6个字节编码，几乎涵盖了地球上所有文字 ，python3中默认此种编码
# python2 默认使用ASCII编码，需要在代码前加入

# *-* coding:utf8 *-*
hello_str = "hello世界"
print(hello_str)