import numpy as np
import matplotlib.pyplot as plt

class Metrics(object):
    """
    Methods for computing useful regression metrics
    
    sse: Sum of squared errors
    sst: Total sum of squared errors (actual vs avg(actual))
    r_squared: Regression coefficient (R^2)
    adj_r_squared: Adjusted R^2
    mse: Mean sum of squared errors
    
    """
    def sse(self):
        '''returns sum of squared errors (model vs actual)'''
        squared_errors = (self.resid_) ** 2
        self.sq_error_ = np.sum(squared_errors)
        return self.sq_error_
        
    def sst(self):
        '''returns total sum of squared errors (actual vs avg(actual))'''
        avg_y = np.mean(self.target_)
        squared_errors = (self.target_ - avg_y) ** 2
        self.sst_ = np.sum(squared_errors)
        return self.sst_
    
    def r_squared(self):
        '''returns calculated value of r^2'''
        self.r_sq_ = 1 - self.sse()/self.sst()
        return self.r_sq_
    
    def adj_r_squared(self):
        '''returns calculated value of adjusted r^2'''
        self.adj_r_sq_ = 1 - (self.sse()/self.dfe_) / (self.sst()/self.dft_)
        return self.adj_r_sq_
    
    def mse(self):
        '''returns calculated value of mse'''
        self.mse_ = np.mean( (self.predict(self.data) - self.target_) ** 2 )
        return self.mse_
    
    def pretty_print_stats(self):
        '''returns report of statistics for a given model object'''
        items = (
                ('sse:', self.sse()), 
                ('sst:', self.sst()),
                ('mse:', self.mse()), 
                ('r^2:', self.r_squared()),
                ('adj_r^2:', self.adj_r_squared())
                )
        for item in items:
            print('{0:8} {1:.4f}'.format(item[0], item[1]))


class MyLinearRegression(Metrics):

    def __init__(self, fit_intercept=True):
        # attributes (a variable-like object attached to a class)
        self.coef_ = None
        self.intercept_ = None
        self._fit_intercept = fit_intercept

    def __repr__(self):
        return "I am a Linear Regression model!"

    # first method
    def fit(self, X, y):
        """Fit model foefficients

        Args:
            X (_type_): 1D or 2D numpy array
            y (_type_): 1D numpy array
        """
        # training data & ground truth data
        self.data = X
        self.target_ = y
        
        # degrees of freedom population dep. variable variance 
        self.dft_ = X.shape[0] - 1  
        # degrees of freedom population error variance
        self.dfe_ = X.shape[0] - X.shape[1] - 1

        if len(X.shape) == 1:
            X = X.reshape(-1,1)

        # add bias (a vector of 1s) if fit_intercept is True
        if self._fit_intercept:
            X_bias = np.c_[np.ones(X.shape[0]), X]
        else: 
            X_bias = X

        # closed form solution
        xTx = np.dot(X_bias.T, X_bias)
        xTx_inv = np.linalg.inv(xTx)
        xTy  = np.dot(X_bias.T, y)
        coef = np.dot(xTx_inv, xTy)

        #set attributes
        if self._fit_intercept:
            self.intercept_ = coef[0]
            self.coef_ = coef[1:]
        else:
            self.intercept_ = 0
            self.coef_ = coef
        
        
        # Predicted/fitted y
        self.fitted_ = np.dot(X, self.coef_) + self.intercept_
        
        # Residuals
        residuals = self.target_ - self.fitted_
        self.resid_ = residuals


    def plot_fitted(self, reference_line=True):
        """
        Plots fitted values against the true output values from the data

        Args:
            reference_line (bool, optional): A Boolean switch to draw a 45-degree reference line on the plot
        """

        plt.title("True vs Fitted values", fontsize=14)
        plt.scatter(y, self.fitted_, s=100, alpha=0.75, color="red", edgecolor="k")
        if reference_line:
            plt.plot(y,y, c="k", linestyle="dotted")
        plt.xlabel("True values")
        plt.ylabel("Fitted values")
        plt.grid(True)
        plt.show()
        

    def predict(self, X):
        """
        Fit model coefficients

        Args:
            X (): 1D or 2D numpy array
            y (_type_): 1D numpy array
        """

        # check if X is 1D or 2D array
        if len(X.shape) == 1:
            X = X.reshape(-1,1)
        self.predicted_ = self.intercept_ + np.dot(X, self.coef_)
        
        return self.predicted_


    def plot(self, x, y, 
            title = None,
            reference_line=True):
        """
        This function should do pretty much the same plotting as in plot_fitted
        but to be more generalized

        Args:
            y (no.array): input array to be plotted on Y axis
            x (np.array): input array to be plotted on X axis
            title (str, optional): title of the plot. Defaults to None.
            reference_line (bool, optional): _description_. Defaults to True.
        """

        plt.title (title, fontsize=14)
        plt.scatter(x, y, s=100, alpha=0.75, color="red", edgecolor="k")
        if reference_line:
            plt.plot(y,y, c="k", linestyle="dotted")
        
        plt.xlabel("True values")
        plt.ylabel("Fitted/Predicted values")
        plt.grid(True)
        plt.show()


