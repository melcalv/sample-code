# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:11:41 2020

@author: mcwa
"""

import numpy
from matplotlib import pyplot as plt
import time

### BUY AND HOLD STRATEGY ###
# At the start of the first day, split wealth into A and B
# No Intervention

### CONSTANT REBALANCING STRATEGY ###
# At the start of the first day, split wealth into A and B
# At the start of each subsequent day, reallocate wealth into initial proportions

# Starting with a $1.00 investment, test both strategies
# Partition equally ($0.50 each) to begin with

valueA = 0.5
valueB = 0.5

# Read the values of the stock each day
# In the CSV: actual share price
# CSV lengths are the same size

stockA = numpy.loadtxt("priceA.csv")
stockB = numpy.loadtxt("priceB.csv")

orig_shareA = valueA / stockA[0]
orig_shareB = valueB / stockB[0]
shareA = orig_shareA
shareB = orig_shareB

# Compare the change in price each day and change the value of the holdings

bh_values = [valueA + valueB] # buy-and-hold values every day
cr_values = [valueA + valueB] # constant rebalancing values every day

for k in range(stockA.size - 1):
    # add 1 to the index to stat after the first day
    i = k + 1
    # store the value for buy and hold
    bh_values.append((orig_shareA * stockA[i]) + (orig_shareB * stockB[i]))
    # find the value of your shares
    valueA = shareA * stockA[i]
    valueB = shareB * stockB[i]
    total_value = valueA + valueB
    # store the value for constant rebalancing
    cr_values.append(total_value)
    # rebalance if necessary
    if valueA != valueB:
        shareA = total_value / (2 * stockA[i])
        shareB = total_value / (2 * stockB[i])
        
# plot the wealth as a function of days

plt.figure()     
plt.plot(bh_values, linewidth=1.0, label = "Buy and Hold")
plt.plot(cr_values, linewidth=1.0, label = "Constant Rebalancing")
plt.legend(loc='upper right')
plt.xlim(0,5034)
plt.title("Investment Value Over Time in Days")
plt.show()


### INVESTMENT C ###
# Fixed income investment earning 5% interest every day
# Investment * 1.05 every day

### INVESTMENT D ###
# On a given day, Investment changes by alpha or beta
# Investment * alpha OR Investment * beta
# alpha = 0.7875
# beta = 1.4


# start with $1 investment and n = 20

# for investment C, just multiply
# for investment D, take all the previous possible values and multiply by alpha and beta, doubling the size of the array
# at the end, average all the values?
    
    
def c_and_d(n):
    
    # make all of the possible investment D combinations
    num = ['']

    for i in range(n):
        new_num = []
        for k in num:
            new_num.append(k+'1')
            new_num.append(k+'0')
        num = new_num
    
    halves = []
    
    for item in num:
        tot = 0
        for letter in item:
            if letter == '1':
                tot += 1
        if tot == 5:
            halves.append(item)
            
    
    # start with $.5 in each investment
    
    original_percentage = 0.5
    original_investment = 1
    
    orig_valueC = original_investment * original_percentage
    orig_valueD = original_investment - orig_valueC
    
    bh_valueC = orig_valueC
    bh_valueD_pos = []
    
    cr_valueC_pos = []
    cr_valueD_pos = []
    cr_total_wealth = []
    
    # just do buy and hold, first
    
    bh_valueC = bh_valueC * (1.05 ** n)
    
    for sequence in num:
        valueD = orig_valueD
        for letter in sequence:
            if letter == '1':
                valueD = valueD * 1.4
            else:
                valueD = valueD * 0.7875
        bh_valueD_pos.append(valueD)
        
    # do constant rebalancing
    
    for sequence in num:
        valueD = orig_valueD
        valueC = orig_valueC
        for letter in sequence:
            valueC = valueC * 1.05
            if letter == '1':
                valueD = valueD * 1.4
            else:
                valueD = valueD * 0.7875
            if valueC != valueD:
                total = valueC + valueD
                valueC = total / 2
                valueD = total - valueC
        cr_valueC_pos.append(valueC)
        cr_valueD_pos.append(valueD)
        cr_total_wealth.append(valueC + valueD)
    
    # Which strategy has a higher average?
    
    bh_average = bh_valueC + (sum(bh_valueD_pos)/len(bh_valueD_pos))
    cr_average = (sum(cr_total_wealth)/len(cr_total_wealth))
    
    # print(bh_average) # $4.32
    # print(cr_average) # $4.01
    
    
    # Compare the D values for the two strategies.
    
    pos = len(bh_valueD_pos)
    
    cr_wins = 0
    
    for i in range(pos):
        bh = bh_valueC + bh_valueD_pos[i]
        cr = cr_valueC_pos[i] + cr_valueD_pos[i]
        if bh > cr:
            cr_wins += 1
            
    # print(cr_wins/pos) # 0.26
    
   
def c_and_d_even(n):
    
    # make all of the possible investment D combinations
    num = ['']

    for i in range(n):
        new_num = []
        for k in num:
            new_num.append(k+'1')
            new_num.append(k+'0')
        num = new_num
    
    halves = []
    
    for item in num:
        tot = 0
        for letter in item:
            if letter == '1':
                tot += 1
        if tot == (n*.5):
            halves.append(item)
            
    
    # start with $.5 in each investment
    
    original_percentage = 0.5
    original_investment = 1
    
    orig_valueC = original_investment * original_percentage
    orig_valueD = original_investment - orig_valueC
    
    bh_valueC = orig_valueC
    bh_valueD_pos = []
    
    cr_valueC_pos = []
    cr_valueD_pos = []
    cr_total_wealth = []
    
    # just do buy and hold, first
    
    bh_valueC = bh_valueC * (1.05 ** n)
    
    for sequence in halves:
        valueD = orig_valueD
        for letter in sequence:
            if letter == '1':
                valueD = valueD * 1.4
            else:
                valueD = valueD * 0.7875
        bh_valueD_pos.append(valueD)
        
    # do constant rebalancing
    
    for sequence in halves:
        valueD = orig_valueD
        valueC = orig_valueC
        for letter in sequence:
            valueC = valueC * 1.05
            if letter == '1':
                valueD = valueD * 1.4
            else:
                valueD = valueD * 0.7875
            if valueC != valueD:
                total = valueC + valueD
                valueC = total / 2
                valueD = total - valueC
        cr_valueC_pos.append(valueC)
        cr_valueD_pos.append(valueD)
        cr_total_wealth.append(valueC + valueD)
    
    # Which strategy has a higher average?
    
    bh_average = bh_valueC + (sum(bh_valueD_pos)/len(bh_valueD_pos))
    cr_average = (sum(cr_total_wealth)/len(cr_total_wealth))
    
    # print(bh_average) # $4.32
    # print(cr_average) # $4.01
    
    
    # Compare the D values for the two strategies.
    
    pos = len(bh_valueD_pos)
    
    cr_wins = 0
    
    for i in range(pos):
        bh = bh_valueC + bh_valueD_pos[i]
        cr = cr_valueC_pos[i] + cr_valueD_pos[i]
        if bh > cr:
            cr_wins += 1
            
    # print(cr_wins/pos) # 0.26
            
    
    # Calculate the doubling rate of each strategy
    
    # print(numpy.log2(bh_average) / 20) # 0.0704
    # print(numpy.log2(cr_average) / 20) # 0.0853
    
    
# c_and_d(20) 


### Time the code

# times = []

# for i in range(20):
#     start_time = time.time()
#     c_and_d(i)
#     times.append(time.time() - start_time)
    

# plt.figure()     
# plt.plot(times, linewidth=1.0)
# plt.title("Run Time of part (c) from n=1 to n=20")
# plt.yscale("log")
# plt.xscale("linear")
# plt.xlim(0, 20)
# plt.show()

# print(times) # [0.0, 0.0, 0.0, 0.0009684562683105469, 0.0, 0.0, 0.0, 0.0, 0.0010251998901367188, 0.000997304916381836, 0.00395655632019043, 0.006026744842529297, 0.014950752258300781, 0.031922101974487305, 0.06780862808227539, 0.1436169147491455, 0.30720019340515137, 0.6561925411224365, 1.3770713806152344, 2.9049551486968994]
    

### Calculate the doubling rate when growth = loss for n = 20
            
# c_and_d_even(20)
