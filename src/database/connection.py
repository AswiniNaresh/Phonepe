import mysql.connector
from mysql.connector import Error
from src.config import Config
import logging

logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self):
        self.config = {
            'host': Config.DB_HOST,
            'port': Config.DB_PORT,
            'database': Config.DB_NAME,
            'user': Config.DB_USER,
            'password': Config.DB_PASSWORD
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            logger.info("Successfully connected to MySQL database")
            return self.connection
        except Error as e:
            logger.error(f"Error connecting to MySQL database: {e}")
            raise

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("Database connection closed")

    def __enter__(self):
        self.connect()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
