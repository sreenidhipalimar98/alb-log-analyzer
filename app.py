import streamlit as st
import pandas as pd
import plotly.express as px

from parser.alb_parser import parse_logs
from parser.s3_downloader import sync_logs

st.set_page_config(
    page_title="AWS ALB Traffic Analyzer",
    layout="wide"
)

st.title("📊 AWS ALB Traffic Analyzer")
if st.button("📥 Sync From S3"):

    with st.spinner("Downloading new log files from S3..."):
        sync_logs()

    st.success("S3 Sync Completed!")

    st.rerun()

with st.spinner("Reading ALB logs..."):
    df = parse_logs()

df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.header("📅 Date Filter")

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["timestamp"].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["timestamp"].max().date()
)

df = df[
    (df["timestamp"].dt.date >= start_date) &
    (df["timestamp"].dt.date <= end_date)
]

st.success(f"Loaded {len(df):,} requests")

# ===========================
# Summary
# ===========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", f"{len(df):,}")

col2.metric("Unique APIs", df["path"].nunique())

col3.metric("Unique Clients", df["client"].nunique())

col4.metric("Avg Response Time", f"{df['response_time'].mean():.3f} sec")

st.divider()

# ===========================
# Top APIs
# ===========================

st.subheader("Top APIs")

api_df = (
    df.groupby("path")
      .size()
      .reset_index(name="Calls")
      .sort_values("Calls", ascending=False)
)

st.dataframe(api_df, use_container_width=True)

fig = px.bar(
    api_df.head(20),
    x="Calls",
    y="path",
    orientation="h",
    title="Top 20 APIs"
)

st.plotly_chart(fig, use_container_width=True)

# ===========================
# Status Codes
# ===========================

st.subheader("Status Code Distribution")

status_df = (
    df.groupby("status")
      .size()
      .reset_index(name="Count")
)

fig = px.pie(
    status_df,
    values="Count",
    names="status"
)

st.plotly_chart(fig, use_container_width=True)

# ===========================
# Requests Per Hour
# ===========================

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["hour"] = df["timestamp"].dt.floor("h")

hour_df = (
    df.groupby("hour")
      .size()
      .reset_index(name="Requests")
)

fig = px.line(
    hour_df,
    x="hour",
    y="Requests",
    markers=True,
    title="Requests Per Hour"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Export")

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Export Parsed Logs (CSV)",
    data=csv,
    file_name="alb_logs.csv",
    mime="text/csv",
)
