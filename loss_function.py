import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

X = np.array([1., 2., 3.])
Y = np.array([1., 2., 3.])
m = len(X)
W = tf.placeholder(tf.float32)

#hypothesis = tf.mul(W, X)
hypothesis = W*X
cost = tf.reduce_sum(tf.pow(hypothesis-Y, 2)) / m

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# 그래프로 표시하기 위해 데이터를 누적할 리스트
W_val, cost_val = [], []

# 0.1 단위로 증가할 수 없어서 -30부터 시작. 그래프에는 -3에서 5까지 표시됨.
# -5에서 20 사이, -0.5에서 2 사이 0.1씩 증가하면 총 25개의 점 확인
for i in range(-5, 20): # -30, 50
    xPos = i*0.1                                    # x 좌표. -3에서 5까지 0.1씩 증가
    yPos = sess.run(cost, feed_dict={W: xPos})      # x 좌표에 따른 y 값
    print('{:3.1f}, {:3.1f}'.format(xPos, yPos))
    # 그래프에 표시할 데이터 누적. 단순히 리스트에 갯수를 늘려나감
    W_val.append(xPos)
    cost_val.append(yPos)
sess.close()
# ------------------------------------------ #
print('size(W_val=)', np.size(W_val))
print('W_val=', W_val)
print('cost_val=', cost_val)
plt.plot(W_val, cost_val, 'ro')
plt.ylabel('Cost')
plt.xlabel('W')
plt.grid()
plt.show()

# size(W_val=) 80
# W_val= [-3.0, -2.9000000000000004, -2.8000000000000003, -2.7, -2.6, -2.5, -2.4000000000000004, -2.3000000000000003, -2.2, -2.1, -2.0, -1.9000000000000001, -1.8, -1.7000000000000002, -1.6, -1.5, -1.4000000000000001, -1.3, -1.2000000000000002, -1.1, -1.0, -0.9, -0.8, -0.7000000000000001, -0.6000000000000001, -0.5, -0.4, -0.30000000000000004, -0.2, -0.1, 0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9, 1.0, 1.1, 1.2000000000000002, 1.3, 1.4000000000000001, 1.5, 1.6, 1.7000000000000002, 1.8, 1.9000000000000001, 2.0, 2.1, 2.2, 2.3000000000000003, 2.4000000000000004, 2.5, 2.6, 2.7, 2.8000000000000003, 2.9000000000000004, 3.0, 3.1, 3.2, 3.3000000000000003, 3.4000000000000004, 3.5, 3.6, 3.7, 3.8000000000000003, 3.9000000000000004, 4.0, 4.1000000000000005, 4.2, 4.3, 4.4, 4.5, 4.6000000000000005, 4.7, 4.800000000000001, 4.9]
# cost_val= [74.66667, 70.98001, 67.386665, 63.88667, 60.479992, 57.166668, 53.94668, 50.82, 47.786674, 44.84666, 42.0, 39.246666, 36.586662, 34.020004, 31.546667, 29.166668, 26.880001, 24.686666, 22.58667, 20.58, 18.666668, 16.846666, 15.120001, 13.486667, 11.946669, 10.5, 9.146666, 7.886667, 6.7200003, 5.6466665, 4.666667, 3.7800002, 2.9866672, 2.2866664, 1.6800001, 1.1666667, 0.7466666, 0.42000008, 0.18666664, 0.04666671, 0.0, 0.04666671, 0.18666676, 0.4199999, 0.74666655, 1.1666667, 1.6800003, 2.2866673, 2.9866662, 3.7799995, 4.666667, 5.6466665, 6.720001, 7.8866653, 9.146668, 10.5, 11.946666, 13.48667, 15.119998, 16.84667, 18.666668, 20.579998, 22.58667, 24.686666, 26.880005, 29.166668, 31.546661, 34.020004, 36.586662, 39.246674, 42.0, 44.84666, 47.786663, 50.820007, 53.94668, 57.166668, 60.479992, 63.886658, 67.38667, 70.98001]

# size(W_val=) 25
# W_val= [-0.5, -0.4, -0.30000000000000004, -0.2, -0.1, 0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9, 1.0, 1.1, 1.2000000000000002, 1.3, 1.4000000000000001, 1.5, 1.6, 1.7000000000000002, 1.8, 1.9000000000000001]
# W_val= array([-0.5, -0.4, -0.3, -0.2, -0.1,  0. ,  0.1,  0.2,  0.3,  0.4,  0.5,
#         0.6,  0.7,  0.8,  0.9,  1. ,  1.1,  1.2,  1.3,  1.4,  1.5,  1.6,
#         1.7,  1.8,  1.9])

# cost_val= [10.5, 9.146666, 7.886667, 6.7200003, 5.6466665, 4.666667, 3.7800002, 2.9866672, 2.2866664, 1.6800001, 1.1666667, 0.7466666, 0.42000008, 0.18666664, 0.04666671, 0.0, 0.04666671, 0.18666676, 0.4199999, 0.74666655, 1.1666667, 1.6800003, 2.2866673, 2.9866662, 3.7799995]
# cost_val= array([10.5       ,  9.146666  ,  7.886667  ,  6.7200003 ,  5.6466665 ,
#         4.666667  ,  3.7800002 ,  2.9866672 ,  2.2866664 ,  1.6800001 ,
#         1.1666667 ,  0.7466666 ,  0.42000008,  0.18666664,  0.04666671,
#         0.        ,  0.04666671,  0.18666676,  0.4199999 ,  0.74666655,
#         1.1666667 ,  1.6800003 ,  2.2866673 ,  2.9866662 ,  3.7799995 ]

# print('{:3.1f}, {:3.1f}'.format(W_val, cost_val))
