import streamlit as st
import pandas as pd
from src.database.operations import DatabaseOperations
from .plots import (
    create_choropleth,
    create_trend_chart,
    create_distribution_chart
)

def create_sidebar_filters():
    st.sidebar.title("Filters")
    
    year = st.sidebar.selectbox(
        "Select Year",
        options=[2018, 2019, 2020, 2021, 2022, 2023]
    )
    
    quarter = st.sidebar.selectbox(
        "Select Quarter",
        options=[1, 2, 3, 4]
    )
    
    transaction_type = st.sidebar.multiselect(
        "Transaction Type",
        options=["UPI", "WALLET", "CARDS", "NET_BANKING"]
    )
    
    return {
        "year": year,
        "quarter": quarter,
        "transaction_type": transaction_type
    }

def create_metrics_section(db_ops: DatabaseOperations, filters: dict):
    st.subheader("Key Metrics")
    
    # Fetch data
    df = db_ops.get_transaction_data(**filters)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total Transactions",
            f"{df['transaction_count'].sum():,}"
        )
    
    with col2:
        st.metric(
            "Total Amount",
            f"₹{df['transaction_amount'].sum():,.2f}Cr"
        )
    
    with col3:
        st.metric(
            "Average Transaction Value",
            f"₹{df['transaction_amount'].mean():,.2f}"
        )