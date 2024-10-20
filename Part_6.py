import math
from colorama import Fore, Style, init

init()

################################################## data ##################################################

Age_data = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
Fat_data =[9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

################################################## FUNCTIONS ##################################################

def Arthmetic_Mean(d): # d-> data
    return sum(d) / len(d)

def Variance(data):
    mean = Arthmetic_Mean(data)
    squered_diff_sum = sum((x - mean) ** 2 for x in data) # The sum of the squared deviations

    return squered_diff_sum / (len(data) - 1)

def Standard_Deviation(data):
    return Variance(data) ** 0.5 # The root of the variance

def Covariance(data1, data2):
    mean1 = Arthmetic_Mean(data1)
    mean2 = Arthmetic_Mean(data2)
    cov_sum = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(len(data1)))
    
    return cov_sum / (len(data1) - 1)

def Correlation_Coefficient(data1, data2):
    cov = Covariance(data1, data2)
    std_dev1 = Standard_Deviation(data1)
    std_dev2 = Standard_Deviation(data2)

    return cov / (std_dev1 * std_dev2)

# Type of Correlation Coefficient
def Correlation_Type(corr):
    if corr > 0:
        return "Positive Correlation."
    elif corr < 0:
        return "Negative Correlation."
    else:
        return "No Correlation."

def Count_Digits_With_Log(n):
    if n == 0: return 0
    return math.floor(math.log10(n)) + 1

def Normalize_Range_Conversion(data):
    _min = min(data)
    _max = max(data)

    normalized_data = [round(((x - _min) / (_max - _min)), 3) for x in data]
    return normalized_data

def Normalize_Range_Conversion_New(data, newMin, newMax):
    _min = min(data)
    _max = max(data)

    normalized_data = [round(( ((x - _min) / (_max - _min)) * (newMax - newMin) + newMin ), 3) for x in data]
    return normalized_data

def Normalize_Decimal_Point_Movement(data):
    if math.fabs(max(data)) > math.fabs(min(data)): _max = math.fabs(max(data)) 
    else: _max = math.fabs(max(data)) 

    num = Count_Digits_With_Log(_max)

    normalized_data = [round(((x / math.pow(10, num))), 3) for x in data]
    return normalized_data

def Normalize_Mean_Standard_Deviation(data):
    mean = Arthmetic_Mean(data)
    std = Standard_Deviation(data)

    normalized_data = [round(((x - mean) / std), 3) for x in data]
    return normalized_data

################################################## OUTPUT ##################################################

corr = Correlation_Coefficient(Age_data, Fat_data)

print(Fore.BLUE, "Correlation Coefficient : ", Fore.WHITE, corr)
print(Fore.BLUE, "Determine the Type of Correlation : ", Fore.WHITE, Correlation_Type(corr))

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

Fat_data.sort()

# Normalize Range Conversion
print(Fore.BLUE, "Normalize Range Conversion Age Data : ", Fore.WHITE, Normalize_Range_Conversion(Age_data))
print(Fore.BLUE, "Normalize Range Conversion Fat Data : ", Fore.WHITE, Normalize_Range_Conversion(Fat_data))

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

# Normalize Range Conversion based on Slide 35 Formular
print(Fore.BLUE, "Normalize Range Conversion Age Data (based on Slide 35 Formular) : ", Fore.WHITE, Normalize_Range_Conversion_New(Age_data, 25, 60))
print(Fore.BLUE, "Normalize Range Conversion Fat Data (based on Slide 35 Formular) : ", Fore.WHITE, Normalize_Range_Conversion_New(Fat_data, 15, 40))

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

# Normalize Decimal Point Movement
print(Fore.BLUE, "Normalize Decimal Point Movement Age Data : ", Fore.WHITE, Normalize_Decimal_Point_Movement(Age_data))
print(Fore.BLUE, "Normalize Decimal Point Movement Fat Data : ", Fore.WHITE, Normalize_Decimal_Point_Movement(Fat_data))

print(Fore.LIGHTBLACK_EX, "----------------------------------------------------------------------------------------------------")

# Normalize Mean Standard Deviation
print(Fore.BLUE, "Normalize Mean Standard Deviation Age Data : ", Fore.WHITE, Normalize_Mean_Standard_Deviation(Age_data))
print(Fore.BLUE, "Normalize Mean Standard Deviation Fat Data : ", Fore.WHITE, Normalize_Mean_Standard_Deviation(Fat_data))

Fat_data.sort()
Age_data.sort()

print("\n")

print(Variance(Fat_data))