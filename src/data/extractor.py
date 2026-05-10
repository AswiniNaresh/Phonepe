import os
import json
import pandas as pd
import git
from pathlib import Path
from datetime import datetime
import logging
from typing import Dict, List, Any, Optional
import warnings
warnings.filterwarnings('ignore')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PhonePeDataExtractor:
    """
    Class to handle data extraction from PhonePe Pulse Github repository.
    """
    
    def __init__(self, repo_url: str, local_dir: str):
        """
        Initialize the PhonePeDataExtractor.

        Args:
            repo_url (str): URL of the PhonePe Pulse Github repository
            local_dir (str): Local directory to store the cloned repository
        """
        self.repo_url = repo_url
        self.local_dir = Path(local_dir)
        self.aggregated_dir = self.local_dir / "data" / "aggregated"
        self.map_dir = self.local_dir / "data" / "map"
        self.top_dir = self.local_dir / "data" / "top"

    def clone_repository(self) -> None:
        """Clone the PhonePe Pulse Github repository if it doesn't exist."""
        try:
            if not self.local_dir.exists():
                logger.info(f"Cloning repository from {self.repo_url}")
                git.Repo.clone_from(self.repo_url, self.local_dir)
                logger.info("Repository cloned successfully")
            else:
                logger.info("Repository already exists locally")
        except Exception as e:
            logger.error(f"Error cloning repository: {str(e)}")
            raise

    def read_json_file(self, file_path: Path) -> Dict:
        """
        Read and parse a JSON file.

        Args:
            file_path (Path): Path to the JSON file

        Returns:
            Dict: Parsed JSON data
        """
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading JSON file {file_path}: {str(e)}")
            return {}

    def extract_aggregated_transaction_data(self) -> pd.DataFrame:
        """
        Extract aggregated transaction data.

        Returns:
            pd.DataFrame: DataFrame containing transaction data
        """
        transaction_data = []
        agg_trans_dir = self.aggregated_dir / "transaction" / "country" / "india" / "state"

        try:
            for state_dir in agg_trans_dir.glob("*"):
                if state_dir.is_dir():
                    state = state_dir.name
                    
                    for year_dir in state_dir.glob("*"):
                        if year_dir.is_dir():
                            year = year_dir.name
                            
                            for json_file in year_dir.glob("*.json"):
                                quarter = json_file.stem
                                data = self.read_json_file(json_file)
                                
                                if 'data' in data and 'transactionData' in data['data']:
                                    for item in data['data']['transactionData']:
                                        row = {
                                            'State': state,
                                            'Year': int(year),
                                            'Quarter': int(quarter),
                                            'Transaction_Type': item['name'],
                                            'Transaction_Count': item['paymentInstruments'][0]['count'],
                                            'Transaction_Amount': item['paymentInstruments'][0]['amount']
                                        }
                                        transaction_data.append(row)
            
            df = pd.DataFrame(transaction_data)
            return df

        except Exception as e:
            logger.error(f"Error extracting aggregated transaction data: {str(e)}")
            raise

    def extract_aggregated_user_data(self) -> pd.DataFrame:
        """
        Extract aggregated user data.

        Returns:
            pd.DataFrame: DataFrame containing user data
        """
        user_data = []
        agg_user_dir = self.aggregated_dir / "user" / "country" / "india" / "state"

        try:
            for state_dir in agg_user_dir.glob("*"):
                if state_dir.is_dir():
                    state = state_dir.name
                    
                    for year_dir in state_dir.glob("*"):
                        if year_dir.is_dir():
                            year = year_dir.name
                            
                            for json_file in year_dir.glob("*.json"):
                                quarter = json_file.stem
                                data = self.read_json_file(json_file)
                                
                                if 'data' in data:
                                    row = {
                                        'State': state,
                                        'Year': int(year),
                                        'Quarter': int(quarter),
                                        'Registered_Users': data['data']['registeredUsers'],
                                        'App_Opens': data['data'].get('appOpens', 0)
                                    }
                                    user_data.append(row)
            
            df = pd.DataFrame(user_data)
            return df

        except Exception as e:
            logger.error(f"Error extracting aggregated user data: {str(e)}")
            raise

    def extract_map_transaction_data(self) -> pd.DataFrame:
        """
        Extract map transaction data.

        Returns:
            pd.DataFrame: DataFrame containing map transaction data
        """
        map_trans_data = []
        map_trans_dir = self.map_dir / "transaction" / "hover" / "country" / "india" / "state"

        try:
            for state_dir in map_trans_dir.glob("*"):
                if state_dir.is_dir():
                    state = state_dir.name
                    
                    for year_dir in state_dir.glob("*"):
                        if year_dir.is_dir():
                            year = year_dir.name
                            
                            for json_file in year_dir.glob("*.json"):
                                quarter = json_file.stem
                                data = self.read_json_file(json_file)
                                
                                if 'data' in data and 'hoverDataList' in data['data']:
                                    for district_data in data['data']['hoverDataList']:
                                        row = {
                                            'State': state,
                                            'Year': int(year),
                                            'Quarter': int(quarter),
                                            'District': district_data['name'],
                                            'Transaction_Count': district_data['metric'][0]['count'],
                                            'Transaction_Amount': district_data['metric'][0]['amount']
                                        }
                                        map_trans_data.append(row)
            
            df = pd.DataFrame(map_trans_data)
            return df

        except Exception as e:
            logger.error(f"Error extracting map transaction data: {str(e)}")
            raise

    def extract_top_transaction_data(self) -> pd.DataFrame:
        """
        Extract top transaction data.

        Returns:
            pd.DataFrame: DataFrame containing top transaction data
        """
        top_trans_data = []
        top_trans_dir = self.top_dir / "transaction" / "country" / "india" / "state"

        try:
            for state_dir in top_trans_dir.glob("*"):
                if state_dir.is_dir():
                    state = state_dir.name
                    
                    for year_dir in state_dir.glob("*"):
                        if year_dir.is_dir():
                            year = year_dir.name
                            
                            for json_file in year_dir.glob("*.json"):
                                quarter = json_file.stem
                                data = self.read_json_file(json_file)
                                
                                if 'data' in data and 'districts' in data['data']:
                                    for district in data['data']['districts']:
                                        row = {
                                            'State': state,
                                            'Year': int(year),
                                            'Quarter': int(quarter),
                                            'District': district['entityName'],
                                            'Transaction_Count': district['metric']['count'],
                                            'Transaction_Amount': district['metric']['amount']
                                        }
                                        top_trans_data.append(row)
            
            df = pd.DataFrame(top_trans_data)
            return df

        except Exception as e:
            logger.error(f"Error extracting top transaction data: {str(e)}")
            raise

    def extract_all_data(self) -> Dict[str, pd.DataFrame]:
        """
        Extract all types of data.

        Returns:
            Dict[str, pd.DataFrame]: Dictionary containing all extracted DataFrames
        """
        try:
            # Clone repository if needed
            self.clone_repository()

            # Extract all data types
            data = {
                'aggregated_transaction': self.extract_aggregated_transaction_data(),
                'aggregated_user': self.extract_aggregated_user_data(),
                'map_transaction': self.extract_map_transaction_data(),
                'top_transaction': self.extract_top_transaction_data()
            }

            logger.info("All data extracted successfully")
            return data

        except Exception as e:
            logger.error(f"Error extracting all data: {str(e)}")
            raise

def main():
    """Main function to execute data extraction."""
    try:
        # Initialize extractor
        extractor = PhonePeDataExtractor(
            repo_url="https://github.com/PhonePe/pulse.git",
            local_dir="pulse_data"
        )

        # Extract all data
        data = extractor.extract_all_data()

        # Create output directory if it doesn't exist
        output_dir = Path("processed_data")
        output_dir.mkdir(exist_ok=True)

        # Save all DataFrames to CSV files
        for name, df in data.items():
            output_path = output_dir / f"{name}.csv"
            df.to_csv(output_path, index=False)
            logger.info(f"Saved {name} data to {output_path}")

    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()