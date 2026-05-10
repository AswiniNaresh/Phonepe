import pandas as pd

def format_currency(amount: float) -> str:
    """Format amount in Indian currency format"""
    return f"₹{amount:,.2f}"

def calculate_growth(current: float, previous: float) -> float:
    """Calculate growth percentage"""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100

def add_growth_metrics(df: pd.DataFrame, value_column: str) -> pd.DataFrame:
    """Add growth metrics to DataFrame"""
    df['growth'] = df[value_column].pct_change() * 100
    return df