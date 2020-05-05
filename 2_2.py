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



print(P)