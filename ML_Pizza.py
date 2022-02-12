import numpy as np
import linear_regression as lr

# Import the dataset
X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)

# Train the system with a learning rate of 1
w, b = lr.train(X, Y, iterations=20000, lr=0.001)
print("\nw=%.3f, b=%.3f" % (w, b))

# Predict the number of pizzas
print("Prediction: x=%d => y=%.2f" % (20, lr.predict(20, w, b)))
