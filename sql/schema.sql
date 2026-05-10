-- sql/schema.sql
CREATE DATABASE IF NOT EXISTS phonepe_pulse;
USE phonepe_pulse;

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    transaction_type VARCHAR(50),
    transaction_amount DECIMAL(15,2),
    transaction_count INT,
    year INT,
    quarter INT,
    timestamp DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    registered_users INT,
    app_opens INT,
    year INT,
    quarter INT,
    timestamp DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- sql/indexes.sql
-- Indexes for transactions table
CREATE INDEX idx_transactions_state ON transactions(state);
CREATE INDEX idx_transactions_year_quarter ON transactions(year, quarter);
CREATE INDEX idx_transactions_type ON transactions(transaction_type);

-- Indexes for users table
CREATE INDEX idx_users_state ON users(state);
CREATE INDEX idx_users_year_quarter ON users(year, quarter);