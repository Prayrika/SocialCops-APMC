import pandas as pd
import matplotlib.pyplot as plt
import cleaned_dataframes as cdf
from statsmodels.tsa.seasonal import seasonal_decompose


# function to form dataframe of required cluster
def form_df(df_cleaned, APMC='None', commodity='None'):
    if commodity == 'None':
        df_reqd = df_cleaned[df_cleaned['APMC'] == APMC]
    if APMC == 'None':
        df_reqd = df_cleaned[df_cleaned['Commodity'] == commodity]
    else:
        df_reqd = df_cleaned[(df_cleaned['APMC'] == APMC) & (df_cleaned['Commodity'] == commodity)]
    return df_reqd


def plotseasonal(res,APMC, commodity):
    data_reqd = form_df(cdf.data_cleaned, APMC, commodity)
    fig, axes = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(6, 3))
    fig.suptitle('Seasonal Decomposition', fontsize=16)
    res.observed.plot(ax=axes[0],legend = False,linewidth=1, c='blue')
    axes[0].set_ylabel('Observed')
    res.trend.plot(ax=axes[1], legend=False,linewidth=1, c='blue')
    axes[1].set_ylabel('Trend')
    res.seasonal.plot(ax=axes[2], legend=False, linewidth=1, c='blue')
    axes[2].set_ylabel('Seasonal')
    res.resid.plot(ax=axes[3], legend=False, linewidth=1, c='blue')
    axes[3].set_ylabel('Residual')
    plt.tick_params(axis='both', which='major', labelsize=5)
    fig.autofmt_xdate(rotation=45)

    plt.tight_layout()
    plt.show()
    return


def detect_seasonality(APMC,commodity):
    data_reqd = form_df(cdf.data_cleaned, APMC, commodity)
    data_reqd.set_index('date', inplace=True)
    print('----Correlation Among Prices---')
    print(data_reqd.corr())
    pd.plotting.autocorrelation_plot(data_reqd['modal_price'])
    plt.title('Autocorrelation of Modal Prices')
    plt.show()

    result = seasonal_decompose(data_reqd['modal_price'], model='multiplicative', freq=3)
    plotseasonal(result,APMC,commodity)
    estimated_trend = result.trend
    estimated_seasonal = result.seasonal
    estimated_residual = result.resid
    fig= plt.figure()
    fig.suptitle('Comparison of Seasonalised Prices')
    plt.plot(data_reqd.index, estimated_trend, label = 'Deseasonalised Price')
    plt.plot(data_reqd.index,data_reqd['modal_price'])
    fig.autofmt_xdate(rotation=45)
    plt.legend()
    plt.show()
    return result


# Example
detect_seasonality('Ahmednagar','Bajri')



