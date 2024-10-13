import math

################################################## DATA ##################################################

Age_data = [3, 13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

################################################## FUNCTIONS ##################################################

# Caculate Mean
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

# Caculate Median
def Median(data):
    sorted_data = sorted(data)
    n = len(data)

    if n % 2 == 1:
        return sorted_data[n // 2] # median for odd lenght
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) /2 # median for even lenght

# Caculate Mode
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

################################################## OUTPUT ##################################################