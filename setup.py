from setuptools import setup, find_packages

setup(
    name="phonepe-pulse",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'mysql-connector-python',
        'streamlit',
        'plotly',
        'python-dotenv',
        'gitpython'
    ],
)