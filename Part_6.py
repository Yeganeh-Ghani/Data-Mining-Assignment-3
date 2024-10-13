import math

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

# Type of Correlation Coefficient
def Correlation_Type(corr):
    if corr > 0:
        return "Positive Correlation."
    elif corr < 0:
        return "Negative Correlation."
    else:
        return "No Correlation."

################################################## OUTPUT ##################################################