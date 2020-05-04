import numpy as np

np.set_printoptions(precision=3)

# The H-h vector
f = np.asmatrix([[39.632,
                 39.572,
                 39.565,
                 39.520,
                 39.434,
                 39.606,
                 39.665,
                 39.545,
                 39.585, 
                 39.545,
                 39.535,
                 39.553,
                 40.055,
                 40.120, 
                 39.778,
                 39.870,
                 39.318,
                 39.337,
                 39.548,
                 39.148,
                 39.555]])

f = f.transpose()

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

print(x)

# Estimated corrections
v = (A*x-f)

n = 21 # Observations
e = 6 # unknowns

# Standard deviation
sigma0 = np.sqrt((v.transpose()*p*v)/(n-e))

# Co-factor matrix
Q = np.linalg.inv(A.transpose()*p*A)

# Variance-covariance matrix
C = np.multiply(sigma0*sigma0, Q)

print(C)


