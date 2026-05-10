#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt

# Run data extraction and processing
python src/data/extractor.py

# Run the Streamlit dashboard
streamlit run main.py