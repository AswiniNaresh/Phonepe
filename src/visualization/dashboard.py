import streamlit as st
import plotly.express as px
from src.database.operations import DatabaseOperations
from .components import (
    create_sidebar_filters,
    create_metrics_section,
    create_map_section,
    create_trends_section
)

class Dashboard:
    def __init__(self):
        self.db_ops = DatabaseOperations()

    def run(self):
        st.set_page_config(
            page_title="PhonePe Pulse Dashboard",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        st.title("PhonePe Pulse Data Visualization")

        # Sidebar filters
        filters = create_sidebar_filters()

        # Layout
        col1, col2 = st.columns([2, 1])

        with col1:
            create_map_section(self.db_ops, filters)
        
        with col2:
            create_metrics_section(self.db_ops, filters)

        create_trends_section(self.db_ops, filters)