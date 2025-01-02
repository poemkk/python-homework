import argparse
import pandas as pd
from homeproject.utils import find_hottest_month_and_city


def main():
    parser = argparse.ArgumentParser(description='Find the hottest month and city for a given year.')
    parser.add_argument('file_path', type=str, help='Path to the GlobalLandTemperaturesByMajorCity.csv file')
    parser.add_argument('year', type=int, help='Year for which to find the hottest month and city')
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.file_path)
        try:
            df['dt'] = pd.to_datetime(df['dt'])
        except pd.errors.ParserError as e:
            print(f"Error converting 'dt' column to datetime: {e}")
            return
        month, city = find_hottest_month_and_city(df, args.year)
        if month and city:
            print(f'The hottest month in {args.year} was {month} in the city of {city}')
        else:
            print(f'No data available for {args.year}')
    except FileNotFoundError:
        print(f"The file {args.file_path} was not found.")


if __name__ == '__main__':
    main()

