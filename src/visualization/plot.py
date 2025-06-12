import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_time_series(traffic_df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x = traffic_df.index, y = traffic_df['flow'])
    plt.title('交通流量时间序列图')
    plt.xlabel('时间')
    plt.ylabel('交通流量(辆/小时)')
    plt.grid(True)
    plt.show()


def plot_road_level_speed(traffic_df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x = 'road_level', y = 'speed', data = traffic_df)
    plt.title('不同道路等级的平均车速箱线图')
    plt.xlabel('道路等级')
    plt.ylabel('平均车速(km/h)')
    plt.show()


def plot_poi_flow(poi_flow_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x = 'poi_type', y = 'flow', data = poi_flow_df)
    plt.title('不同POI类型周边道路的平均交通流量')
    plt.xlabel('POI类型')
    plt.ylabel('平均交通流量(辆/小时)')
    plt.show()