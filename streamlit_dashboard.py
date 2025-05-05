import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import matplotlib.dates as mdates

def tidy_date_axis(ax, every=3, fmt='%b %d'):
    """整理时间轴：每 `every` 天显示 1 个刻度。"""
    locator = mdates.DayLocator(interval=every)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    ax.figure.autofmt_xdate()


st.set_page_config(page_title="E-commerce Dashboard", layout="wide")
st.title("📊 E-commerce User Behavior Dashboard")

# -------------------------------
# Data Loading
# -------------------------------
data_path = Path("output/cleaned_data_sample.csv")  # or full file
if data_path.exists():
    df = pd.read_csv(data_path, parse_dates=["event_time"])
else:
    st.error("❌ Sample data not found. Please check the path.")
    st.stop()

# Ensure event_time is datetime
df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')
df = df.dropna(subset=['event_time'])

# -------------------------------
# Sidebar: Date Filter
# -------------------------------
min_date = df['event_time'].min().date()
max_date = df['event_time'].max().date()

start_date, end_date = st.sidebar.date_input(
    "📆 Select date range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

mask = (df['event_time'].dt.date >= start_date) & (df['event_time'].dt.date <= end_date)
df_filtered = df.loc[mask]

# -------------------------------
# KPI Cards
# -------------------------------
dau = df_filtered.groupby(df_filtered['event_time'].dt.date)['user_id'].nunique()
wau = df_filtered.groupby(df_filtered['event_time'].dt.to_period('W'))['user_id'].nunique()
total_users = df_filtered['user_id'].nunique()
total_events = len(df_filtered)
total_purchases = (df_filtered['event_type'] == 'purchase').sum()
total_cart = (df_filtered['event_type'] == 'cart').sum()

col1, col2, col3 = st.columns(3)
col1.metric("🧑‍💻 Unique Users", f"{total_users:,}")
col2.metric("🛒 Total Purchases", f"{total_purchases:,}")
col3.metric("📦 Total Events", f"{total_events:,}")

# -------------------------------
# DAU & WAU
# -------------------------------
st.subheader("Daily & Weekly Active Users")
fig, ax = plt.subplots()
dau.plot(ax=ax)
ax.set_title("DAU over Time")
ax.set_ylabel("Unique Users")
tidy_date_axis(ax, every=3)
st.pyplot(fig)

fig2, ax2 = plt.subplots()
wau.plot(ax=ax2)
ax2.set_title("WAU over Time")
ax2.set_ylabel("Unique Users")
tidy_date_axis(ax, every=2)   
st.pyplot(fig)

# -------------------------------
# Event Trend
# -------------------------------
st.subheader("Event Type Trends")
event_counts = df_filtered.groupby([df_filtered['event_time'].dt.date, 'event_type']).size().unstack().fillna(0)
fig3, ax3 = plt.subplots()
event_counts.plot(ax=ax3)
ax3.set_title("Event Volume by Type")
ax3.set_ylabel("Count")
tidy_date_axis(ax, every=2)   
st.pyplot(fig)

# -------------------------------
# Funnel Conversion
# -------------------------------
st.subheader("Conversion Funnel")
funnel = df_filtered.groupby(df_filtered['event_time'].dt.date)['event_type'].value_counts().unstack().fillna(0)
funnel['view_to_cart'] = funnel['cart'] / funnel['view']
funnel['cart_to_buy'] = funnel['purchase'] / funnel['cart']

fig4, ax4 = plt.subplots()
funnel[['view_to_cart', 'cart_to_buy']].plot(ax=ax4)
ax4.set_title("Conversion Rates")
ax4.set_ylabel("Rate")
tidy_date_axis(ax, every=3)  
st.pyplot(fig)

# -------------------------------
# RFM Segment (Demo from preprocessed)
# -------------------------------
st.subheader("User Segments (RFM)")
rfm_path = Path("output/rfm_segments.csv")
if rfm_path.exists():
    df_rfm = pd.read_csv(rfm_path)
    seg_counts = df_rfm['Segment'].value_counts()
    fig5, ax5 = plt.subplots()
    seg_counts.sort_values().plot(kind='barh', ax=ax5)
    ax5.set_title("RFM Segments Distribution")
    st.pyplot(fig5)
else:
    st.info("RFM 分群数据未找到。请先生成并保存文件：output/rfm_segments.csv")

# -------------------------------
# Footer
# -------------------------------
st.caption("Data Source: E-commerce Behavior Dataset (Kaggle)")
