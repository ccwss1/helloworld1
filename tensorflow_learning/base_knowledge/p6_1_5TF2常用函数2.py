import tensorflow as tf

# 求导函数
with tf.GradientTape() as tape:
    w = tf.Variable(tf.constant(3.0))
    loss = tf.pow(w, 2)
grad = tape.gradient(loss, w)
print(grad)

# 枚举函数
seq = ["one", "two", "three"]
for i, seqenum in enumerate(seq):
    print(i,seqenum)

#转换数据为one_hot形式
labels = tf.constant([1,0,2])
classes = 3
output = tf.one_hot(labels, classes)
print(output)

# softmax函数
y = tf.constant([1.01, 2.01, -0.66])
y_pro = tf.nn.softmax(y)
print("After Softmax is y_pro",y_pro)

# 更新参数的值并返回
w1 = tf.Variable(4)
w1.assign_sub(1)
print(w1)

# 返回最大值的索引
data = tf.constant([[1, 2, 3], [2, 3, 4], [5, 4,3]])
print(tf.argmax(data, axis=0))
print(tf.argmax(data,axis=1))
