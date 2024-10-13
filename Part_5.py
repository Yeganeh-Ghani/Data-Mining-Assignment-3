import math
import numpy as np

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