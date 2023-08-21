import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
# from sklearn import linear_model

def cost(x):
	m = A.shape[0]
	return 0.5/m * np.linalg.norm(A.dot(x) - Y, 2)**2

def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x)-Y)

def gradient_descent(x_init, learning_rate, iteration):
	x_list = [x_init]
	m = A.shape[0]

	for i in range(iteration):
		x_new = x_list[-1] - learning_rate*grad(x_list[-1])
		# if np.linalg.norm(grad(x_new))/m < 0.5: # when to stop GD
		# 	break
		x_list.append(x_new)

	return x_list

# Data

Y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
X = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# Change row vector to column vector
X = np.array([X]).transpose()
Y = np.array([Y]).transpose()

# Draw data
fig1 = plt.figure("GD for Linear Regression")
ax = plt.axes(xlim=(-5,30), ylim=(-1,50)) 
plt.plot(X,Y, 'ro')
x0_gd = np.linspace(1,25,10000)

# Create X square
X_square = np.array([X[:,0]**2]).transpose()
X_square = np.concatenate((X_square, X), axis =1)

# Add one to A
ones = np.ones((X.shape[0],1), dtype=np.int8)
A = np.empty((X_square.shape[0],2))
A = np.concatenate((X_square, ones), axis =1)

print(A)

# Random initial line
x_init = np.array([[ -2.1],
       [ 5.1],
       [-2.1]])
y0_init = x_init[0][0]*x0_gd*x0_gd + x_init[1][0]*x0_gd + x_init[2][0]
plt.plot(x0_gd,y0_init, color="black")

# Run gradient descent
iteration = 100
learning_rate = 0.000001

x_list = gradient_descent(x_init, learning_rate, iteration)

# Draw x_list (solution by GD)
for i in range(len(x_list)):
	y0_x_list = x_list[i][0]*x0_gd*x0_gd + x_list[i][1]*x0_gd + x_list[i][2]
	plt.plot(x0_gd,y0_x_list, color="black")

plt.show()

# Plot cost per iteration to determine when to stop 
cost_list = []
iter_list = [] 
for i in range(len(x_list)):
	iter_list.append(i)
	cost_list.append(cost(x_list[i]))

plt.plot(iter_list, cost_list)
plt.xlabel('Iteration')
plt.ylabel('Cost value')

plt.show()