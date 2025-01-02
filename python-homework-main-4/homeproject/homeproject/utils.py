import pandas as pd


def find_hottest_month_and_city(df, year):
    required_columns = ['dt', 'AverageTemperature']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in DataFrame: {', '.join(missing_columns)}")
    filtered_df = df[df['dt'].dt.year == year]
    if filtered_df.empty:
        return None, None
    max_temp_row = filtered_df.loc[filtered_df['AverageTemperature'].idxmax()]
    return max_temp_row['dt'].strftime('%B'), max_temp_row['City']
