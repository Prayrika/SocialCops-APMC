import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


# Scale data using MinMaxScaler
def scale_data(df):
    global MMS
    MMS= MinMaxScaler()
    df_copy = df.copy()
    df_copy = MMS.fit_transform(df_copy)
    return df_copy

# Obtaining cleaned annual data
def clean_data(df_scaled,df_price,nu_estimate):
    copy_df = df_scaled.copy()
    auto_detection = svm.OneClassSVM(kernel='rbf', gamma=0.05, degree=1, nu=nu_estimate)
    auto_detection.fit(copy_df)
    evaluation = auto_detection.predict(copy_df)
    percent_outliers = len(copy_df[evaluation == -1]) * 100 / len(copy_df)
    # print('PERCENTAGE OF OUTLIERS:', percent_outliers, '%')
    copy_df= pd.DataFrame(MMS.inverse_transform(copy_df),columns=df_scaled.columns)
    df_cleaned = df_price[evaluation != -1]
    # plt.scatter(copy_df.index,copy_df['modal_price'], c=evaluation)
    # plt.legend(loc='upper left')
    # plt.show()
    return df_cleaned


data = pd.read_csv('Monthly_data_cmo.csv')
data_14 = pd.DataFrame()
data_15 = pd.DataFrame()
data_16 = pd.DataFrame()
data_14 = data_14.append(data[data['Year'] == 2014],ignore_index=True)
data_14_prices = data_14[['modal_price', 'max_price', 'min_price']]
data_15 = data_15.append(data[data['Year'] == 2015], ignore_index=True)
data_15_prices = data_15[['modal_price', 'max_price', 'min_price']]
data_16 = data_16.append(data[data['Year'] == 2016], ignore_index=True)
data_16_prices = data_16[['modal_price', 'max_price', 'min_price']]

data_14_scaled = pd.DataFrame(scale_data(data_14_prices), columns=data_14_prices.columns)
data_15_scaled = pd.DataFrame(scale_data(data_15_prices), columns=data_15_prices.columns)
data_16_scaled = pd.DataFrame(scale_data(data_16_prices), columns=data_16_prices.columns)


# # Plotting the Scatter Matrix:
# # To observe the dependence of two variables on each other
# # to observe distribution of data
# scatter_matrix(data_14_scaled)
# plt.show()

data_14_cleaned = clean_data(data_14_scaled,data_14_prices,.05)
data_15_cleaned = clean_data(data_15_scaled,data_15_prices,.05)
data_16_cleaned = clean_data(data_16_scaled,data_16_prices,.05)

# Final cleaned files
data_14_cleaned=pd.concat([data_14[['APMC']],data_14[['date']],data_14[['Commodity']],data_14_cleaned], axis=1 )
data_15_cleaned=pd.concat([data_15[['APMC']],data_15[['date']],data_15[['Commodity']],data_15_cleaned], axis=1 )
data_16_cleaned=pd.concat([data_16[['APMC']],data_16[['date']],data_16[['Commodity']],data_16_cleaned], axis=1 )
data_cleaned = pd.concat([data_14_cleaned,data_15_cleaned,data_16_cleaned],ignore_index=True)
print(data_cleaned.head())
data_cleaned.to_csv('Cleaned_MandiData.csv')
