import numpy as np
from dynamics_utils import Phase

from interactions import interactions
from math_utils import math_utils

PhaseData = [Phase(3, 3)]*10
inter = interactions()

C_Frict_l = 0.05
V_Frict_l = 0.63
Acc_l = 4.16
p_l = 3.2
R_0_l = 85.3
Dim_l = 3

for i in range(3):
     PhaseData[0].Coordinates[0][i] = i+1
     PhaseData[0].Coordinates[1][i] = i*2
     PhaseData[0].Coordinates[2][i] = i*3

     PhaseData[0].Velocities[i] = 3



# B = inter.RepulsionLin(PhaseData[0], 7, 0.4, 4, 0, 3, 0)



C = inter.FrictionLinSqrt(PhaseData[0], C_Frict_l, V_Frict_l, Acc_l, p_l, R_0_l, 0, Dim_l)
print(C)
# a = np.zeros([1,3])


# for i in range(0, 3):
#     a[0][i] = i+1
# print(a)
# math_utils.UnitVect(a[0], 3)
# print(a)

