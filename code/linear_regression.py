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
    
    def pred(self, X):
        return (X*self.w).sum(axis = 1)
    
    def score(self, X, y):
        # https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/statistics/regression-and-correlation/coefficient-of-determination-r-squared.html
        # R^2 value
        y_hat = self.pred(X)
        y_bar = torch.mean(y)
        return 1 - torch.sum((y - y_hat)**2)/torch.sum((y - y_bar)**2)
    
    # coefs standard error
    # coefs test statistic
    # coefs p-val

    # adjusted R^2?

