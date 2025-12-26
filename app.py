import streamlit as st
import matplotlib.pyplot as plt

from analysis import load_data, MA, plot_voltage, peak, low, below_k, downslopeAccelerate


st.set_page_config(page_title="Voltage Analysis", layout="wide")

st.title("Voltage Time-Series Analysis")
st.write("Green Mobility Assignment")

df = load_data()
df = MA(df)

st.subheader("Voltage with Moving Averages")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Timestamp"], df["Values"], label = "Values", color='blue')
ax.plot(df["Timestamp"], df["MA_1000"], label = "MA 1000", color='red')
ax.plot(df["Timestamp"], df["MA_5000"], label = "MA 5000", color='green')
ax.set_xlabel("Timestamp")
ax.set_ylabel("Voltage")
ax.set_title("Values with 1000 and 5000 Value Moving Averages")
ax.legend()
st.pyplot(fig)

peak_df = peak(df)
low_df = low(df)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Peaks in Voltage Data")
    st.dataframe(peak_df)
with col2:
    st.subheader("Lows in Voltage Data")
    st.dataframe(low_df)

st.subheader("Values Below Threshold")
threshold = st.number_input("Set Threshold Value:", value=100)
below_df = below_k(df, threshold, None)
st.dataframe(below_df)

st.subheader("Timestamps with Downward Accelerating Values")
down_timestamp = downslopeAccelerate(df)
st.write("Timestamps wehere downward acceleration occurs:")
st.dataframe(down_timestamp)
