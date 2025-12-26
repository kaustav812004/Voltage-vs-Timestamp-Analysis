import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def load_data():
    df = pd.read_csv('data/Sample_Data.csv')
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], dayfirst=True)
    return df

def MA(df):
    df["MA_1000"] = df["Values"].rolling(1000).mean()
    df["MA_5000"] = df["Values"].rolling(5000).mean()
    return df

def plot_voltage(df, output_path="outputs/plots"):
    plt.figure(figsize=(12, 6))
    plt.plot(df["Timestamp"], df["Values"], color='blue')
    plt.plot(df["Timestamp"], df["MA_1000"], color='red')
    plt.plot(df["Timestamp"], df["MA_5000"], color='green')
    plt.xlabel("Timestamp")
    plt.ylabel("Voltage")
    plt.title("Values with 1000 and 5000 Value Moving Averages")
    plt.legend(["Values", "MA 1000", "MA 5000"])
    plt.tight_layout()
    plt.savefig(f"{output_path}/value_ma_plot.png")
    plt.show()
    
    
def peak(df):
    peak, _ = find_peaks(df['Values'])
    peak_df = df.iloc[peak][['Timestamp', 'Values']]
    return peak_df

def low(df):
    low, _ = find_peaks(-df['Values'])
    low_df = df.iloc[low][['Timestamp', 'Values']]
    return low_df

def below_k(df, k, path):
    below_df = df.loc[df['Values'] < k, ['Timestamp', 'Values']]
    return below_df

def downslopeAccelerate(df):
    slope = df['Values'].diff()
    slope_change = slope.diff()
    down_acc = df[(slope < 0) & (slope_change < 0)][['Timestamp']]
    return down_acc['Timestamp']
