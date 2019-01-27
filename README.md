# ASE ADA Sample Subject Implementation
```./resources/Rankings.csv``` file contains records for 190 countries around the world regarding indicators related to the business environment. The observed variables values reflect the situation for one year, 2018 (data source: World Bank: http://data.worldbank.org). The original dataset used by the professor was not available.

The observed variables are as follows:
1. Economy
2. globalRank
3. Starting a Business
4. Dealing with Construction Permits
5. Getting Electricity
6. Registering Property
7. Getting Credit
8. Protecting Minority Investors
9. Paying Taxes
10. Trading across Borders
11. Enforcing Contracts
12. Resolving Insolvency

## Requirements
1. Read the data file and upload it into a Pandas dataframe (0.75p).
2. Fill in the NA, NaN cells with the appropriate values correesponding to the meaning of the variables (0.5p).
3. Standardise the values of the resuklting numerical matrix (0.75p).
4. Determine and displayt the correlation matrix (0.75p).
5. Determine and display the eignevalues / eigenvectors of the correlation matrix of the initial data set (1.75p).
6. Determine the principal components, save and display them (1.5p).
7. Plot the variance agglutinated by each principal component as a line plot, along with an horizontal line corresponding to thje value of variance equal to 1 (1p).
8. List and describe accuratley the criteria for choosing the axes, principal components (1p).
9. Determine, save and display the matrix of scores.
10. Determine the correlation coefficient.
