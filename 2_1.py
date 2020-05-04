import numpy as np

#np.set_printoptions(precision=4)

# The H-h vector
f = np.asmatrix([[-81.1581,
                  -81.1422,
                  -82.9131,
                  -82.8905,
                  -82.8979,
                  -82.8963,
                   -1.7519,
                   -0.0144,
                   -0.0124, 
                   -0.0078,
                    0.0197]])

f = f.transpose()
print(f)

# The weight matrix
p = np.asmatrix([[1.0000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0.4444, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0.1600, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 4.0000, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0.2500, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0.1600, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0.1600, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1.0000, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1.0000, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0816, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0816]])
print("the weight matrix")
print(p)

# The design matrix
A = np.asmatrix([[-1,  0],
                 [-1,  0],
                 [ 0, -1],
                 [ 0, -1],
                 [ 0, -1],
                 [ 0, -1],
                 [ 1, -1],
                 [ 0,  0],
                 [ 0,  0],
                 [ 0,  0],
                 [ 0,  0]])



print("the design matrix")
print(A)

# the vector of estimated coefficients
x = (np.linalg.inv(A.transpose()*p*A))*A.transpose()*p*f

print("the estimated heights")
print(x)

# Estimated corrections
v = (A*x-f)

n = 21 # Observations
e = 6 # unknowns

# Standard deviation
sigma0 = np.sqrt((v.transpose()*p*v)/(n-e))

print("the standard deviation of the unit weight")
print(sigma0)

# Co-factor matrix
Q = np.linalg.inv(A.transpose()*p*A)

# Variance-covariance matrix
C = np.multiply(sigma0*sigma0, Q)

print("the variance-covariance matrix")
print(C)


