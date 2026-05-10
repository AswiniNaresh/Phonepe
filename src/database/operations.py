from typing import List, Dict, Any
import pandas as pd
from .connection import DatabaseConnection
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DatabaseOperations:
    def __init__(self):
        self.db = DatabaseConnection()

    def insert_transactions(self, df: pd.DataFrame) -> None:
        """Insert transaction data into database"""
        with self.db.connect() as conn:
            cursor = conn.cursor()
            for _, row in df.iterrows():
                query = """
                INSERT INTO transactions 
                (state, district, transaction_type, transaction_amount, 
                transaction_count, year, quarter, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, tuple(row))
            conn.commit()

    def insert_users(self, df: pd.DataFrame) -> None:
        """Insert user data into database"""
        with self.db.connect() as conn:
            cursor = conn.cursor()
            for _, row in df.iterrows():
                query = """
                INSERT INTO users 
                (state, district, registered_users, app_opens, 
                year, quarter, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, tuple(row))
            conn.commit()

    def get_transaction_data(self, **filters) -> pd.DataFrame:
        """Retrieve transaction data with filters"""
        query = "SELECT * FROM transactions"
        if filters:
            conditions = [f"{k} = %s" for k in filters.keys()]
            query += " WHERE " + " AND ".join(conditions)
        
        with self.db.connect() as conn:
            return pd.read_sql(query, conn, params=tuple(filters.values()))

    def get_user_data(self, **filters) -> pd.DataFrame:
        """Retrieve user data with filters"""
        query = "SELECT * FROM users"
        if filters:
            conditions = [f"{k} = %s" for k in filters.keys()]
            query += " WHERE " + " AND ".join(conditions)
        
        with self.db.connect() as conn:
            return pd.read_sql(query, conn, params=tuple(filters.values()))