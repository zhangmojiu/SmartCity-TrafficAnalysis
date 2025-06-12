import pandas as pd
import seaborn as sns


def analyze_time_distribution(traffic_df):
    # 早晚高峰、平峰时段分析，这里简单示例统计，可进一步完善
    traffic_df['time'] = pd.to_datetime(traffic_df['time'])
    traffic_df['hour'] = traffic_df['time'].dt.hour
    morning_peak = traffic_df[(traffic_df['hour'] >= 7) & (traffic_df['hour'] < 9)]
    evening_peak = traffic_df[(traffic_df['hour'] >= 17) & (traffic_df['hour'] < 19)]
    off_peak = traffic_df[~((traffic_df['hour'] >= 7) & (traffic_df['hour'] < 9) | (traffic_df['hour'] >= 17) & (traffic_df['hour'] < 19))]

    morning_peak_flow = morning_peak['flow'].mean()
    evening_peak_flow = evening_peak['flow'].mean()
    off_peak_flow = off_peak['flow'].mean()

    print(f"早高峰（7:00 - 9:00）平均流量：{morning_peak_flow}辆/小时")
    print(f"晚高峰（17:00 - 19:00）平均流量：{evening_peak_flow}辆/小时")
    print(f"平峰时段平均流量：{off_peak_flow}辆/小时")

    return morning_peak_flow, evening_peak_flow, off_peak_flow


def analyze_road_level(traffic_df):
    # 不同道路等级交通状况分析
    road_level_stats = traffic_df.groupby('road_level').agg({'speed': 'mean', 'flow': 'mean'}).reset_index()
    print("不同道路等级交通状况统计：")
    print(road_level_stats)

    # 可进一步添加可视化代码，这里先简单返回统计结果
    return road_level_stats


def analyze_poi_impact(traffic_df):
    # POI类型对交通的影响分析
    poi_flow = traffic_df.groupby('poi_type')['flow'].mean().reset_index()
    print("不同POI类型周边道路平均交通流量：")
    print(poi_flow)

    # 可进一步添加可视化代码，这里先简单返回统计结果
    return poi_flow