import pandas as pd
import matplotlib.pyplot as plt


def read_annual_temp_avg():
    df = pd.read_fwf('ann-tavg-normal.txt', [(0, 11), (19, 23), (23, 24)])
    df.columns = ['stnid', 'temp_f', 'flag']

    df.temp_f = (df.temp_f / 10).round()
    df['temp_c'] = fahrenheit_to_celsius(df.temp_f).round()

    return df


def fahrenheit_to_celsius(val):
    return (val - 32) * (5 / 9)


if __name__ == '__main__':
    df = read_annual_temp_avg()

    plt.suptitle('1981-2010 Avg Temp')

    plt.subplot(121)
    temp_f_val_counts = df.temp_f.value_counts()
    plt.bar(temp_f_val_counts.index, temp_f_val_counts.values)
    plt.title('fahrenheit')
    plt.ylabel('freq (days)')

    plt.subplot(122)
    temp_c_val_counts = df.temp_c.value_counts()
    plt.bar(temp_c_val_counts.index, temp_c_val_counts.values)
    plt.title('celsius')
    plt.ylabel('freq (days)')

    plt.show()
