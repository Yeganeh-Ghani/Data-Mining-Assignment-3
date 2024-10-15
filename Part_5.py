import math
import numpy as np
from colorama import Fore, Style, init

init()

################################################## DATA ##################################################

Age_data = [3, 13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

################################################## FUNCTIONS ##################################################

# Calculate  Mean
def Arthmetic_Mean(d): # d-> data
    return sum(d) / len(d)

def Geometric_Mean(d): #d-> data
    product = 1 # Multiply the data
    count = len(d)

    for value in d:
        product *= value # multiply of all data
    
    mean = product ** (1 / count) # n-th rooh

    return mean

def Harmonic_Mean(d): #d-> data
    reciprocal_sum = 0 # sum of reverse data

    for value in d:
        reciprocal_sum += 1 / value # reverse each data
    
    mean = len(d) / reciprocal_sum

    return mean

# Calculate  Median
def Median(data):
    sorted_data = sorted(data)
    n = len(data)

    if n % 2 == 1:
        return sorted_data[n // 2] # median for odd lenght
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) /2 # median for even lenght

# Calculate  Mode
def Mode(d):
    freq_dict = {}
    for value in d:
        if value in freq_dict:
            freq_dict[value] +=1 # increase the repeatation
        else:
            freq_dict[value] = 1
    
    max_count = max(freq_dict.values())
    mode_values = [key for key, count in freq_dict.items() if count == max_count]

    if len(mode_values) == len(Age_data):
        return None # if all the same data were repeated
    
    return mode_values

# Calculate  Quartile with numpy library
def Quartile_lib(d):
    Q1 = np.percentile(d, 25)
    Q2 = np.percentile(d, 50) # median
    Q3 = np.percentile(d, 75)

    IQR = Q3 - Q1 # Quartile divation

    return Q1, Q2, Q3, IQR

# Calculate  Quartile without numpy library
def Quartile(d):
    d.sort()
    n = len(d)

    # find median = Q2
    if n % 2 == 0:
        Q2 = (d[n // 2 - 1] + d[n // 2]) // 2
    else:
        Q2 = d[n // 2]

    # devide data into 2 half
    Lower_half = d[:n // 2]
    Upper_half = d[(n + 1) // 2:]

    # find Q1
    n_lower = len(Lower_half)
    if n_lower % 2 == 0:
        Q1 = (Lower_half[n_lower // 2 - 1] + Lower_half[n_lower // 2]) / 2
    else:
        Q1 = Lower_half[n_lower // 2]

    # find Q2
    n_upper = len(Upper_half)
    if n_upper % 2 == 0:
        Q3 = (Upper_half[n_upper // 2 - 1] + Upper_half[n_upper // 2]) / 2
    else:
        Q3 = Upper_half[n_upper // 2]

    # find IQR
    IQR = Q3 - Q1

    return Q1, Q2, Q3, IQR

# Identify Outliers with numpy library
def Identify_Outliers_lib(data):
    mean = np.mean(data)
    st_Dev = np.std(data)

    # Calculate upper and lower bound
    lower_bound = mean - 2 * st_Dev
    upper_bound = mean + 2 * st_Dev

    # Identify Outliers
    outliers = [x for x in data if x < lower_bound or x > upper_bound]

    return outliers, lower_bound, upper_bound, mean, st_Dev

################################################## OUTPUT ##################################################

mean = Arthmetic_Mean(Age_data)
median = Median(Age_data)
mode = Mode(Age_data)
n = len(Age_data)
R = max(Age_data) - min(Age_data)
K = round(1 + 3.3 * math.log(n)) # Count of groups
D = round(R / K) # Distance between Groups

print(Fore.BLUE, "Mean : ", Fore.WHITE, mean)
print(Fore.BLUE, "Median : ", Fore.WHITE, median)
print(Fore.BLUE, "Mode : ", Fore.WHITE, mode)

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

q1, q2, q3, iqr = Quartile(Age_data)

print(Fore.BLUE, "Quartile 1 : ", Fore.WHITE, q1)
print(Fore.BLUE, "Quartile 2 : ", Fore.WHITE, q2)
print(Fore.BLUE, "Quartile 3 : ", Fore.WHITE, q3)
print(Fore.BLUE, "Quartile Deviation : ", Fore.WHITE, iqr)

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

outliers, lower, upper, mean1, std = Identify_Outliers_lib(Age_data)

print(Fore.BLUE, "Outlier : ", Fore.WHITE, outliers)
print(Fore.BLUE, "Lower Bound : ", Fore.WHITE, lower)
print(Fore.BLUE, "Upper Bound : ", Fore.WHITE, upper)
print(Fore.BLUE, "Mean : ", Fore.WHITE, mean1)
print(Fore.BLUE, "Standard Deviation : ", Fore.WHITE, std)

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

print(Fore.BLUE, "Number of Groups : ", Fore.WHITE, K) # 12
print(Fore.BLUE, "Distance between Groups : ", Fore.WHITE, D) # 6

list_1 = (3) # mean = 3
list_2 = (13, 15, 16, 16) # mean = 15
list_3 = (19, 20, 20, 21, 22, 22) # mean = 20.6 = 21
list_4 = (25, 25, 25) # mean = 25
list_5 = (30) # mean = 30
list_6 = (33, 33) # mean = 33
list_7 = (35, 35, 35, 35) # mean = 35
list_8 = (36) # mean = 36
list_9 = (40) # mean = 40
list_10 = (45, 46) # mean = 68
list_11 = (52) # mean = 52
list_12 = (70) # mean = 70

final_list = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10, list_11, list_12]

print(Fore.BLUE, "First Binning by Calculate K in 12 Groups (Slide 27, 28) : ", Fore.WHITE)
for i in final_list:
    print(i)

error = 0 + math.fabs(13-15) + 1 + 1 + math.fabs(19-21) + math.fabs(20-21) + math.fabs(20-21) + 1 + 1 + math.fabs(45-68) + math.fabs(46-68)

print(Fore.BLUE, "Error in Group 1 : ", Fore.WHITE, error) # 55

t_1 = (3) # mode = 3, mean = 3
t_2 = (13, 15, 16, 16, 19) # mode = 16, mean = 15.8 = 16
t_3 = (20, 20, 21, 22, 22, 25, 25, 25) # mode = 25, mean = 22.5 = 25
t_4 = (30, 33, 33, 35, 35, 35, 35, 36) # mode = 35, mean = 29.5 = 30
t_5 = (40, 45, 46) # mode = 4, 45, 46, mean = 43.6 = 44
t_6 = (52) # mdoe = 52, mean = 52
t_7 = (70) # mode = 70, mean = 70

final_list1 = [t_1, t_2, t_3, t_4, t_5, t_6, t_7]

print(Fore.BLUE, "\nSecond Binning by Mean in 12 Groups (Slide 29) : ", Fore.WHITE)
for i in final_list1:
    print(i)

error1 = math.fabs(13-16) + math.fabs(15-16) + (19-16) + math.fabs(20-25) + math.fabs(20-25)
+ math.fabs(21-25) + math.fabs(22-25) + math.fabs(22-25) + (33-30) + (33-30) + (35-30) + (35-30) + (35-30) + (35-30)
+ math.fabs(40-44) + math.fabs(45-44) + math.fabs(46-44) 

print(Fore.BLUE, "Error in Group 2 : ", Fore.WHITE, error1) # 17