# Logistic Regression

### Concept

**Logistic Regression:** is a type of supervised machine learning algorithm be used to classify. It use sigmoid function to estimate the probability (true|false ; yes|no) of object 

### Prove


### Formula
Sigmoid function:
$$
y = \frac{1}{1 + \mathrm{e}^{-z}}
$$
where:
* **y** is the output of the logistic regression model for a particular example.

* $$z = b + w_1*x_1 + w_2*x_2 + w_3*x_3 + ... + w_n*x_n$$
*  * The **w** values are the model's learned weights, and **b** is the bias.
* * The **x** values are the feature values for a particular example.

The result of sigmoid function is from 0 to 1.
* $$When\  z = -\infty \  => y = 0$$
*  $$When\  z = 0 \  => y = 0,5$$
*  $$When\  z = +\infty \  => y = 1$$

if the result y > 0,5  => p = 1

if the result y < 0,5  => p = 0

### Loss function for Logistic Regression
$$\text{Log Loss} = \sum_{(x,y)\in D} -y\log(y') - (1 - y)\log(1 - y')$$
