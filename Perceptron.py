# Implemenatation of the perceptron....
import numpy as np

class Perceptron(object):
    """Perceptron classifier..
    parameters
    ----------------------------
    eta  : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int 
        Random number generator seed for random weight.
        initialization

    Attributes 
    ----------------
    w_ : id-array
        Weights after fitting.
    errors_ : list

        Number of misclassification (updates) in each epoch.
    
    """
    def ___init__(self, eta =  0.01, n_iter=50, random_state=1):
        self.eta  = eta
        self.n_iter =  n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit trainging data.
        
        parameters
        -------------------------------------
        X : {array-like}, shape = [n_samples, n_fetures]
        Training vectors, where n_samples is the number of samples and n_features is the number of features.
        y  : array-like , shape = [n_samples]
            Target values.

            Returns
         ---------------
         self  : object   

        """    
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0

            for xi , target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0) 
                self.errors_.append(errors)
        return self

def net_input(self, X):
    """Calculate net input"""
    return np.dot(X, self.w_[1:]) + self.w_[0]

def predict(self, X):
    """Return  Class label after unit atep.."""
    return np.where(self.net_input(X) >= 0.0, 1, -1)


# The .dot is used to calculate the dot product.....