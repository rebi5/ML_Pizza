# This file contains the functions used by linear regression, but not the code
# that runs them. Import these functions with 'import linear_regression', and
# use them with 'linear_regression.function_name()'.

import numpy as np


def predict(X, w, b):
    return X * w + b


def loss(X, Y, w, b):
    return np.average((predict(X, w, b) - Y) ** 2)

def gradient(X, Y, w, b):
        w_gradient = 2 * np.average(X * (predict(X, w, b) - Y))
        b_gradient = 2 * np.average(predict(X, w, b) - Y)
        return (w_gradient, b_gradient)


def train(X, Y, iterations, lr):
    w = b = 0

    for i in range(iterations):
        print("Iteration %4d => Loss: %.6f" % (i, loss(X, Y, w, b)))

        w_gradient, b_gradient = gradient(X, Y, w, b)
        w -= w_gradient * lr
        b -= b_gradient * lr
        
    return w, b
