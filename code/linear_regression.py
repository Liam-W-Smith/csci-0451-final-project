# Import packages
import torch

# Define ridge regression class
class RidgeRegression:

    def __init__(self):
        self.w = None 

    def fit(self, X, y, lam = 1.0):
        p = X.size(1)
        w_hat = torch.inverse(X.T@X + lam*torch.eye(p))@X.T@y
        self.w = w_hat

    def mse(self, X, y):
        return ((X@self.w - y)**2).mean()