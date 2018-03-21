import tensorflow as tf
import numpy as np
import math as m
tf.set_random_seed(777)


def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7)

xy = np.loadtxt('user_dataset.csv', delimiter=',', dtype=np.float32)

x_data = xy[:,1:5]
y_data = xy[:,[0]]

print(x_data)
print(y_data)

nb_classes = 5

X = tf.placeholder(tf.float32, [None, 4])
Y = tf.placeholder(tf.int32, [None, 1])
Y_one_hot = tf.one_hot(Y, nb_classes)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])

W1 = tf.get_variable("W1", shape=[4, 20],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([20]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.get_variable("W2", shape=[20, 20],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([20]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.get_variable("W3", shape=[20, nb_classes],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([5]))
hypothesis = tf.matmul(L2, W3) + b3

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=hypothesis, labels=Y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 50 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict={
                                 X: x_data, Y: y_data})
            print("Step: {:5}\tCost: {:.3f}\tAcc: {:.2%}".format(
                step, loss, acc))

    pred = sess.run(prediction, feed_dict={X: x_data})
    pred = sess.run(prediction, feed_dict={X: [[3,1,2,1]]})
    print("Test:",pred)

    fr = np.loadtxt('restaurant_dataset.csv', delimiter=',', dtype=np.str)
    pred_string=np.str(pred[0])
    print(fr)
    print(pred_string)
    f_rname = fr[fr[:,1]==pred_string, [0]]
    f_data = fr[fr[:,1]==pred_string, 2:4]
    fd = float(f_data[0,0])
    f_x = []
    f_y = []
    minindex = 0
    f_x.insert(0,float(f_data[0,0]))
    print(f_x)
    for i in range(len(f_data)):
        f_x.insert(i,float(f_data[i,0]))
        f_y.insert(i,float(f_data[i,1]))
        
    user_location = [100, 100]

    min_distance_x = pow((f_x[0] - user_location[0]),2)
    min_distance_y = pow((f_y[0] - user_location[1]),2)
    min_distance = min_distance_x + min_distance_y

    for i in range(len(f_data)):
        distance_x = pow((f_x[i] - user_location[0]),2)
        distance_y = pow((f_y[i] - user_location[1]),2)
        if(min_distance > distance_x + distance_y):
           min_distance_x = distance_x + distance_y
           minindex = i 
           
    min_distance = m.sqrt(min_distance)

    print(f_rname[minindex] + "을 추천합니다")
    
        
