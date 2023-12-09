import numpy as np
from oop_linear_regression import MyLinearRegression
from oop_linear_regression import Metrics


X = 10*np.random.random(size=(20,2))
y = 3.5*X.T[0]-1.2*X.T[1]+2*np.random.randn(20)

mlr = MyLinearRegression()
mlr.fit(X,y)

print("We have fitted the data. We can print the regression coefficients now")
print(f"Regression coefficients:, {mlr.coef_}")
print(f"The intercept term is given by: , {mlr.intercept_}")

#mlr.plot_fitted()
#mlr.plot(y, mlr.fitted_)

# Generate test data
num_test_samples = 10
X_test = 10*np.random.random(size=(num_test_samples,2))
y_test = 3.5*X_test.T[0]-1.2*X_test.T[1]+2*np.random.randn(num_test_samples)
print(X_test.shape, y_test.shape)

y_pred = mlr.predict(X_test)
print(f"Predicted values: {y_pred}")
#mlr.plot(y_test, y_pred)

print(f'Error Value: {mlr.pretty_print_stats()}')


