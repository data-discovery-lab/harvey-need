import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
t = sess.run(a + b)
print("My text:", t)
sess.close()