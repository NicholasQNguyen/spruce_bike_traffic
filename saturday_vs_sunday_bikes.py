import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator


def main():
    saturday = 2
    sunday = 3
    columns = ["AM8", "AM9", "AM10", "AM11",]
    dataframe = pd.read_csv("17_and_spruce_bike_traffic.csv")
    saturday_bikes = dataframe.iloc[saturday]
    sunday_bikes = dataframe.iloc[sunday]
    saturday_bikes_between_8_and_11 = sum(saturday_bikes[columns])
    sunday_bikes_between_8_and_11 = sum(sunday_bikes[columns])
    days = ["Saturday", "Sunday"]
    day_vs_day_bikes = [saturday_bikes_between_8_and_11, sunday_bikes_between_8_and_11]
    """
    plt.bar(days, day_vs_day_bikes)
    plt.title("Number of bikes between 18th and 19th and Spruce \n between 8am and 11am on Saturday vs Sunday (2021)")
    plt.savefig("18th_and_19th_spruce_bikes.png")
    plt.show()
    """

    times = dataframe.columns[1:25]
    print("TIMES", times)
    just_saturday_bikes = saturday_bikes[1:25]
    just_sunday_bikes = sunday_bikes[1:25]
    print(just_sunday_bikes)
    plt.title("Bike over time on Saturday vs Sunday")
    plt.plot(times, just_saturday_bikes, label="Saturday Bikes")
    plt.plot(times, just_sunday_bikes, label="Sunday Bikes")
    plt.legend()
    plt.gca().xaxis.set_major_locator(AutoLocator())
    plt.savefig("bikes_over_time.png")
    plt.show()




if __name__ == '__main__':
    main()