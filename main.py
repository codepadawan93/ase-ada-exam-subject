import pandas as pan
import numpy as np

# replace Na, NaN with column average
def replace_na(values):
    avgs = np.nanmean(values, axis=0)
    pos = np.where(np.isnan(values))
    values[pos] = avgs[pos[1]]
    return values

# work on z-scores instead of values : value - mean / stddev
def standardise(values):
    means = np.mean(values, axis=0)
    stds = np.std(values, axis=0)
    standardised_values = (values - means) / stds
    return standardised_values

# read dataframe
data_frame = pan.read_csv("./resources/Rankings.csv", index_col=0)
print("Values and index", data_frame.values, data_frame.index)

# clean nan, na
cleaned_values = replace_na(data_frame.values)
print("Cleaned values", cleaned_values)

# compute z-scores
standardised_values = standardise(cleaned_values)
print("Standardised", standardised_values)

# compute correlation matrix
correlation_matrix = np.corrcoef(data_frame.values, rowvar=False)
print("Correlation matrix", correlation_matrix)

#read it into a dataframe
# correlation_data_frame = pan.DataFrame(correlation_matrix, data_frame.index, data_frame.index)

# get the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(correlation_matrix)
print("Eigenvalues and eigenvectors", eigenvalues, eigenvectors)

reversed_eigenvalues = [k for k in reversed(np.argsort(eigenvalues))]
a = eigenvectors[reversed_eigenvalues]
alpha = eigenvectors[:, reversed_eigenvalues]

pc = standardised_values @ a
print(pc)