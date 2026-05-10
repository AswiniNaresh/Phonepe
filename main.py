#import streamlit as st
#from src.visualization.dashboard import Dashboard
#from src.config.config import load_config
#from src.database.connection import DatabaseConnection
#from src.utils.logger import setup_logging
#
#def main():
#    # Set up logging
#    setup_logging()
#    
#    # Load configuration
#    config = load_config()
#    
#    # Initialize database connection
#    db = DatabaseConnection(config['database'])
#    
#    # Create and run dashboard
#    dashboard = Dashboard(db)
#    dashboard.run()
#
#if __name__ == "__main__":
#    main()


import streamlit as st
from src.visualization.dashboard import Dashboard
from src.utils.logger import setup_logging
from src.config import Config

def main():
    # Set up logging
    setup_logging()
    
    # Create and run dashboard
    dashboard = Dashboard()
    dashboard.run()

if __name__ == "__main__":
    main()    