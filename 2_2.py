import numpy as np
import sys
np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision=1)
# Weight matrix
P=np.asmatrix(np.zeros((33, 33)))

row_start=0
row_end=3
col_start=0
col_end=3

#Observation l_1
sigma0=0.3673
Q11=0.00000013
Q12=0.00000001
Q22=0.00000007
Q13=0.00000011
Q23=0.00000002
Q33=0.00000041

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_2
sigma0=0.3502
Q11=0.00000019
Q12=0.00000001
Q22=0.00000011
Q13=0.00000015
Q23=0.00000005
Q33=0.00000059

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_3
sigma0=0.3928
Q11=0.00000027
Q12=0.00000005
Q22=0.00000019
Q13=0.00000035
Q23=0.00000016
Q33=0.00000157

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_4
sigma0=0.7908
Q11=0.00000026
Q12=0.00000005
Q22=0.00000019
Q13=0.00000035
Q23=0.00000015
Q33=0.00000160

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_5
sigma0=0.3342
Q11=0.00000026
Q12=0.00000005
Q22=0.00000019
Q13=0.00000035
Q23=0.00000015
Q33=0.00000162

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_6
sigma0=0.3908
Q11=0.00000025
Q12=0.00000005
Q22=0.00000019
Q13=0.00000033
Q23=0.00000015
Q33=0.00000154

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_7
sigma0=0.4238
Q11=0.00000044
Q12=0.00000002
Q22=0.00000017
Q13=0.00000047
Q23=-0.00000001
Q33=0.00000146

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_8
sigma0=0.3767
Q11=0.00000007
Q12=0.00000001
Q22=0.00000005
Q13=0.00000007
Q23=0.00000002
Q33=0.00000029

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_9
sigma0=0.3234
Q11=0.00000006
Q12=0.00000001
Q22=0.00000004
Q13=0.00000006
Q23=0.00000002
Q33=0.00000024

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_10
sigma0=0.6160
Q11=0.00000031
Q12=0.00000005
Q22=0.00000024
Q13=0.00000028
Q23=0.00000018
Q33=0.00000124

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#Observation l_11
sigma0=0.4560
Q11=0.00000012
Q12=0.00000001
Q22=0.00000007
Q13=0.00000011
Q23=0.00000001
Q33=0.00000040

Q = np.asmatrix([[Q11, Q12, Q13],
                 [Q12, Q22, Q23],
                 [Q13, Q23, Q33]])
p = np.linalg.inv(np.multiply(sigma0*sigma0, Q))
P[row_start:row_end, col_start:col_end]=p
row_start+=3
row_end+=3
col_start+=3
col_end+=3

#############################################################################################

A = np.asmatrix([[ 1, 0, 0, 0, 0, 0],
                 [ 0, 1, 0, 0, 0, 0],
                 [ 0, 0, 1, 0, 0, 0],
                 [ 1, 0, 0, 0, 0, 0],
                 [ 0, 1, 0, 0, 0, 0],
                 [ 0, 0, 1, 0, 0, 0],
                 [ 0, 0, 0, 1, 0, 0],
                 [ 0, 0, 0, 0, 1, 0],
                 [ 0, 0, 0, 0, 0, 1],
                 [ 0, 0, 0, 1, 0, 0],
                 [ 0, 0, 0, 0, 1, 0],
                 [ 0, 0, 0, 0, 0, 1],
                 [ 0, 0, 0, 1, 0, 0],
                 [ 0, 0, 0, 0, 1, 0],
                 [ 0, 0, 0, 0, 0, 1],
                 [ 0, 0, 0, 1, 0, 0],
                 [ 0, 0, 0, 0, 1, 0],
                 [ 0, 0, 0, 0, 0, 1],
                 [-1, 0, 0, 1, 0, 0],
                 [ 0,-1, 0, 0, 1, 0],
                 [ 0, 0,-1, 0, 0, 1],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0]])
 
################################################################################
f = np.asmatrix([[2815018.3582,
                  517204.4022,
                  5680875.0702,
                  2815018.3467,
                  517204.4036,
                  5680875.0580,
                  2814502.3010,
                  516784.8094,
                  5681168.9393,
                  2814502.2857,
                  516784.8123,
                  5681168.9214,
                  2814502.2850,
                  516784.8152,
                  5681168.9297,
                  2814502.2914,
                  516784.8116,
                  5681168.9251,
                  -516.0604,
                  -419.5919,
                  293.8671,
                  0.0124,
                  -0.0034,
                  0.0102,
                  0.0094,
                  -0.0016,
                  0.0094,
                  0.0042,
                  -0.0030,
                  0.0069,
                  0.0010,
                  0.0071,
                  -0.023]])

f = f.transpose()
np.set_printoptions(precision=8)


# the vector of estimated coefficients
x = (np.linalg.inv(A.transpose()*P*A))*A.transpose()*P*f

print("the estimated coordinates")
print(x)

# Estimated corrections
v = (A*x-f)

n = 33 # Observations
e = 6 # unknowns

# Standard deviation
sigma0 = np.sqrt((v.transpose()*P*v)/(n-e))

# Co-factor matrix
Q = np.linalg.inv(A.transpose()*P*A)

# Variance-covariance matrix
C = np.multiply(sigma0*sigma0, Q)

print("the variance-covariance matrix")
print(C)
