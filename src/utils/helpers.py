from typing import Any, Dict, List
import pandas as pd
from pathlib import Path

def ensure_directory(path: Path) -> None:
    """Ensure directory exists"""
    path.mkdir(parents=True, exist_ok=True)

def validate_dataframe(df: pd.DataFrame, required_columns: List[str]) -> bool:
    """Validate DataFrame has required columns"""
    return all(col in df.columns for col in required_columns)

def save_to_csv(df: pd.DataFrame, path: Path, filename: str) -> None:
    """Save DataFrame to CSV file"""
    ensure_directory(path)
    full_path = path / f"{filename}.csv"
    df.to_csv(full_path, index=False)