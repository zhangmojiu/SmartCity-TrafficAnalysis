import pandas as pd
import numpy as np
from datetime import datetime
import os
from statsmodels.tsa.arima.model import ARIMA


class DataPreprocessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data_dict = {}

    def load_data(self):
        # 加载交通流量数据
        traffic_path = os.path.join(self.data_dir, 'traffic_flow.csv')
        if os.path.exists(traffic_path):
            self.data_dict['traffic'] = pd.read_csv(traffic_path)
            print(f"加载交通流量数据: {self.data_dict['traffic'].shape[0]}条记录")

        # 加载公交数据
        bus_path = os.path.join(self.data_dir, 'bus_data.csv')
        if os.path.exists(bus_path):
            self.data_dict['bus'] = pd.read_csv(bus_path)
            print(f"加载公交数据: {self.data_dict['bus'].shape[0]}条记录")

        # 加载气象数据
        weather_path = os.path.join(self.data_dir, 'weather_data.csv')
        if os.path.exists(weather_path):
            self.data_dict['weather'] = pd.read_csv(weather_path)
            print(f"加载气象数据: {self.data_dict['weather'].shape[0]}条记录")

        return self.data_dict

    def fill_missing_values(self, traffic_df):
        # 速度字段采用双向滚动均值填充
        traffic_df['speed'] = traffic_df['speed'].fillna(traffic_df['speed'].rolling(window = 60, min_periods = 1, center = True).mean())

        # 流量字段使用ARIMA预测填充，异常时用均值填充
        missing_idx = traffic_df[traffic_df['flow'].isnull()].index
        for idx in missing_idx:
            before = traffic_df.loc[:idx].tail(100)
            after = traffic_df.loc[idx:].head(100)
            combined = pd.concat([before, after])
            try:
                model = ARIMA(combined['flow'], order=(5, 1, 0))
                model_fit = model.fit()
                forecast = model_fit.forecast(steps = 1)
                traffic_df.loc[idx, 'flow'] = forecast[0]
            except:
                traffic_df.loc[idx, 'flow'] = combined['flow'].mean()
        return traffic_df

    def handle_outliers(self, traffic_df):
        # 速度异常值通过IQR方法检测并修正
        q1 = traffic_df['speed'].quantile(0.25)
        q3 = traffic_df['speed'].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        traffic_df['speed_outlier'] = False
        traffic_df.loc[traffic_df['speed'] < lower_bound, 'speed_outlier'] = True
        traffic_df.loc[traffic_df['speed'] > upper_bound, 'speed_outlier'] = True

        traffic_df.loc[traffic_df['speed'] < 0, 'speed'] = 0
        traffic_df.loc[traffic_df['speed'] > 120, 'speed'] = 120
        return traffic_df