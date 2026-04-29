import numpy as np

class TinyNN:
    def __init__(self):
        self.W1 = np.random.randn(2, 3)
        self.W2 = np.random.randn(3, 1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        self.z1 = X @ self.W1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2
        self.out = self.sigmoid(self.z2)
        return self.out

    def train_step(self, X, y, lr=0.1):
        out = self.forward(X)

        error = out - y
        dW2 = self.a1.T @ (error * out * (1 - out))
        dW1 = X.T @ ((error @ self.W2.T) * self.a1 * (1 - self.a1))

        self.W2 -= lr * dW2
        self.W1 -= lr * dW1