import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# random data
Y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
X = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# Change row vector to column vector
X = np.array([X]).transpose()
Y = np.array([Y]).transpose()

# Create X square
X_square = np.array([X[:,0]**2]).transpose()
X_square = np.concatenate((X_square, X), axis =1)

# Create vector 1
ones = np.ones((X.shape[0],1), dtype=np.int8)

# Combine 1 and X
A = np.empty((X_square.shape[0],2))
A = np.concatenate((X_square, ones), axis =1)

# Use fomular
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(Y)

# Test data to draw
x0 = np.linspace(1,25,10000)
y0 = x[0][0]*x0*x0+ x[1][0]*x0 + x[2][0]

# Visualize data
plt.plot(X,Y,'ro')
plt.plot(x0,y0)

# Test predicting data
x_predict = 12
y_predict = x_predict*x_predict*x[0][0]+x[1][0]*x_predict+x[2][0]

mse = 0
for i in range (0, X.shape[0]):
    mse += abs(X[i][0]*x[0][0] + x[1][0] - Y[i][0])
    print(str(Y[i][0]) + "  " + str(X[i][0]))
print("mse: " + str(mse**2/X.shape[0]))
print("y_predict: " + str(y_predict))
plt.show()