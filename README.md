# SocialCops-APMC
## Components of this Repository :

### 1)CODE FILES:
####  - 1. cleaned_dataframes.py: 
        The interactive script performs three tasks : 
        - (i) scales each of the prices, namely, minimum price, maximum price and modal price by using MinMax scaler from scikit library (function: scale_data), 
        - (ii) cleans data by filtering outliers from  the scaled data by usinf One Class SVM with gamma = 0.05 and nu=.05 (function: clean_data), 
        - (iii) returns back filtered datapoints in a csv file format. 
####  - 2. Detect_seasonality.py: 
      The interactive script performs three tasks : 
      - (i) forms the dataframe for the cluster of APMC and crop required to be analysed (function: form_data), 
      - (ii) helps to analyse the behaviour of prices over a monthly span sothat additive or multiplicative nature of the seasonality be deduced, 
      - (iii) Once detected, it gives a seasonal decomposition plot representation of the data and compares the raw data with         deseasonalised trend in prices (functions: plot seasonal, detect_seasonality). 

### 2) GRAPH IMAGES : 
       -Image files corresponding to various observations used for analysis.

### 3) CLEANED DATA FILE:
       -Dataset free of outlier - Cleaned_MandiData.csv
The entire methodology is explained in the wiki page
