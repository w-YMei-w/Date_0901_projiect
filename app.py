# app.py
import streamlit as st

st.set_page_config(page_title="纽约自行车数据分析", layout="wide")

st.title("🚲 纽约公共自行车数据分析与可视化系统")
st.markdown("---")

st.write("欢迎使用！本项目基于纽约Citi Bike公开数据进行分析与可视化。")

# 左侧菜单示例
option = st.sidebar.selectbox(
    "选择分析模块",
    ["数据概览", "时间趋势", "用户对比", "聚类分析"]
)

st.sidebar.write(f"当前选择：{option}")
st.sidebar.markdown("---")
st.sidebar.caption("小组项目 | 2026")