# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:25:15 2022

@author: Ooi Kok Yih
"""
import csv
import numpy as np
import matplotlib.pyplot as plot

with open("plot1Data.csv") as file_name:
    plot1 = np.loadtxt(file_name, delimiter=",")
    
with open("plot2Data.csv") as file_name:
    plot2 = np.loadtxt(file_name, delimiter=",")

# with open("keyByteList.csv") as file_name:
#     keyByteList = np.genfromtxt(file_name, delimiter=",")[:, 1:]

keyByteList = [[0.9694174,0.8654746,0.67611104,0.6274521,0.60417134,0.6025458,0.60154843,0.57589626,0.6030942,0.60759395],
[0.9723265,0.8576734,0.8670959,0.86666906,0.85466886,0.85418934,0.82853544,0.83260137,0.82280403,0.82655466],
[0.9730504,0.8356844,0.68387175,0.62430805,0.59560776,0.5680744,0.5714561,0.5738089,0.5895808,0.6003905],
[0.9678453,0.8562425,0.7612356,0.65450764,0.6257932,0.6701143,0.6957103,0.6949437,0.70650005,0.7180114],
[0.96488523,0.84959006,0.66714585,0.61047417,0.56380296,0.534796,0.5390815,0.5246465,0.52324235,0.5292877],
[0.97950834,0.8333018,0.7244466,0.79021555,0.7573134,0.7518499,0.7418113,0.74624115,0.74812174,0.77065194],
[0.97272074,0.8321844,0.6921162,0.678096,0.6147907,0.57065874,0.56784934,0.54957473,0.55202246,0.54866004],
[0.9654067,0.9153779,0.71024144,0.67194617,0.6624782,0.63902956,0.638086,0.64834374,0.6339995,0.62855667],
[0.96035516,0.82227707,0.7751861,0.6489707,0.5745028,0.5533603,0.53821355,0.54219925,0.5586497,0.5398927],
[0.9716903,0.85844797,0.8234538,0.7493696,0.74238956,0.73087656,0.6762075,0.68752116,0.69528747,0.71584463],
[0.9764051,0.80950415,0.7287706,0.6145279,0.5866454,0.62767637,0.62617296,0.61997175,0.60571957,0.5883557],
[0.9760037,0.9011001,0.7940305,0.6552004,0.7138095,0.7331276,0.6889158,0.6869525,0.690813,0.68899304],
[0.9688009,0.8340872,0.77821916,0.6227822,0.6394545,0.6314456,0.6525626,0.66079897,0.66408306,0.66053104],
[0.9878379,0.820943,0.747517,0.6483519,0.67071086,0.7050651,0.7295696,0.6996962,0.6909836,0.69391507],
[0.9809525,0.89341754,0.7677534,0.7036474,0.65086347,0.6399708,0.6452007,0.6184785,0.5991941,0.5839761],
[0.98600197,0.84013945,0.72870094,0.70340896,0.6633948,0.5927069,0.591978,0.60035175,0.6254066,0.6201159]]
    
    
# print(plot1)
# print("####################################################################################")
# print(plot2)
#print(keyByteList)

for i in range(0, 16, 1): #byte 0 to 15
    plot.figure()
    plot.plot(plot1[i])  # plot1 correlation values for key from 0x00 to 0xFF for current byte
    plot.xlabel("Possible Key Bytes")
    plot.ylabel("Correlation Values")
#     #plot.savefig(f'correlation_plot1_for_byte_{index//2}')
    

# step_list = [i for i in range(10, 110, 10)]

# l = 0    
# for j in range(0, 160, 10):
#     plot2list = []
#     for k in range(0,10,1):
#         plot2list.append(plot2[j+k])
#         print(plot2list)
    
#     plot.figure()
#     plot.plot(step_list, plot2list, 'o', color='blue')  # plot2 correlation values for all the bytes from trace = 10 to trace = 110 except correct key byte
#     plot.plot(step_list, keyByteList[l], 'o', color='red')  # plot2 correlation values for correct key bytes from trace = 10 to trace = 100
#     plot.xlabel("No. of traces")
#     plot.ylabel("Correlation Values")
#     l+=1
    