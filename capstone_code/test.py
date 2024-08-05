import numpy as np
import matplotlib.pyplot as plt
import math

c = 0.720
d = 0.150
l1 = 1.600
l2 = 0.314
l3 = 1.182
l4 = 1.910
phi2_degree_list = []
phi3_degree_list = []
y_crossbar_list = []
for phi1 in range(5,57,1):
    radian_phi1 = np.deg2rad(phi1)
    sin_phi1 = np.sin(radian_phi1)
    cos_phi1 = np.cos(radian_phi1)

    k1 = (-2*l2*((l1*sin_phi1)+d))
    k2 = (2*l2*((l1*cos_phi1)-c))
    k3 = (l1**2 + l2**2 - l3**2 + c**2 + d**2 + (2*l1*d*sin_phi1) - (2*c*l1*cos_phi1))

    phi2 = 2 * np.arctan((-k1 - (math.sqrt(k1**2 + k2**2 - k3**2))) / (k3 - k2) )
    phi2_degree = np.rad2deg(phi2)
    phi2_degree_list.append(phi2_degree)
    print(phi2_degree)
    
    sin_phi2 = np.sin(phi2)
    cos_phi2 = np.cos(phi2)
    phi3 = np.arctan(((l1*sin_phi1) - (l2*sin_phi2) + d) / ((l1*cos_phi1) + (l2*cos_phi2) - c))
    phi3_degree = np.rad2deg(phi3)
    phi3_degree_list.append(phi3_degree)
    print(phi3_degree)

    alpha = 73
    radian_alpha = np.deg2rad(alpha)
    
    x_crossbar = ((-l1*cos_phi1) + (l4*(np.cos(phi2 - radian_alpha))))
    y_crossbar = ((l1*sin_phi1) + (l4*(np.sin(phi2 - radian_alpha))))
    y_crossbar_list.append(y_crossbar)
    
    print(x_crossbar)
    print(y_crossbar)

phi1_list = list(range(5, 57, 1))

plt.subplot(311)
plt.xlabel('phi-1', fontsize=10)
plt.ylabel('phi-2', fontsize=8)
plt.plot(phi1_list, phi2_degree_list)

plt.subplot(312)
plt.xlabel('phi-1', fontsize=10)
plt.ylabel('phi-3', fontsize=8)
plt.plot(phi1_list, phi3_degree_list)

plt.subplot(313)
plt.xlabel('phi-1', fontsize=10)
plt.ylabel('height of the pantograph', fontsize=8)
plt.plot(phi1_list, y_crossbar_list)

plt.tight_layout()
plt.show()
