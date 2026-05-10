from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    id: int
    state: str
    district: str
    transaction_type: str
    transaction_amount: float
    transaction_count: int
    year: int
    quarter: int
    timestamp: datetime

@dataclass
class User:
    id: int
    state: str
    district: str
    registered_users: int
    app_opens: int
    year: int
    quarter: int
    timestamp: datetime