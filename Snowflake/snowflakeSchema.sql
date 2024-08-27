// tạo DW và DB bằng role accountadmin
use role accountadmin;
create database Bank_DW_DB;
create warehouse Bank_DW with warehouse_size = 'large';
// tạo role spark_role với quyền usage để connect với spark
create role spark_role;
grant usage on warehouse Bank_DW to role spark_role;
grant usage on database BANK_DW_DB to role spark_role;
SHOW GRANTS ON SCHEMA BANK_DW_DB.BANK_OLTP_SCHEMA;

show grants on warehouse Bank_DW;
//tạo schemas
BANK_DW_DB.BANK_OLTP_SCHEMA.ACCOUNTS
CREATE SCHEMA  Bank_OLTP_Schema

-- Tạo bảng Customers trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.customers (
    customer_id VARCHAR PRIMARY KEY,
    customer_name VARCHAR,
    customer_email VARCHAR,
    customer_phone VARCHAR,
    customer_address VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR,
    customer_zip_code VARCHAR
);

-- Tạo bảng Accounts trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.accounts (
    account_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES Bank_OLTP_Schema.customers(customer_id),
    account_type VARCHAR,
    account_balance NUMERIC,
    account_open_date TIMESTAMP,
    account_status VARCHAR
);

-- Tạo bảng Transactions trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.transactions (
    transaction_id VARCHAR PRIMARY KEY,
    account_id VARCHAR REFERENCES Bank_OLTP_Schema.accounts(account_id),
    transaction_type VARCHAR,
    transaction_amount NUMERIC,
    transaction_date TIMESTAMP,
    transaction_description TEXT
);

-- Tạo bảng Branches trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.branches (
    branch_id VARCHAR PRIMARY KEY,
    branch_name VARCHAR,
    branch_address VARCHAR,
    branch_city VARCHAR,
    branch_state VARCHAR,
    branch_zip_code VARCHAR
);

-- Tạo bảng Loans trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.loans (
    loan_id VARCHAR PRIMARY KEY,
    loan_type VARCHAR,
    customer_id VARCHAR REFERENCES Bank_OLTP_Schema.customers(customer_id),
    loan_amount NUMERIC,
    loan_interest_rate NUMERIC,
    loan_start_date TIMESTAMP,
    loan_end_date TIMESTAMP,
    loan_status VARCHAR
);

-- Tạo bảng Credit Cards trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.credit_cards (
    card_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES Bank_OLTP_Schema.customers(customer_id),
    card_number VARCHAR UNIQUE,
    card_expiry_date TIMESTAMP,
    card_limit NUMERIC,
    card_balance NUMERIC,
    card_status VARCHAR
);

-- Tạo bảng Transactions History trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.transaction_history (
    history_id VARCHAR PRIMARY KEY,
    account_id VARCHAR REFERENCES Bank_OLTP_Schema.accounts(account_id),
    transaction_id VARCHAR REFERENCES Bank_OLTP_Schema.transactions(transaction_id),
    change_description TEXT,
    change_date TIMESTAMP
);

-- Tạo bảng Payment trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.payment (
    payment_id VARCHAR PRIMARY KEY,
    order_id VARCHAR,
    payment_date TIMESTAMP,
    amount NUMERIC(10, 2),
    payment_method VARCHAR,
    currency VARCHAR,
    status VARCHAR,
    customer_id VARCHAR REFERENCES Bank_OLTP_Schema.customers(customer_id),
    transaction_id VARCHAR REFERENCES Bank_OLTP_Schema.transactions(transaction_id)
);

-- Tạo bảng Investments trong schema Bank_OLTP_Schema
CREATE TABLE IF NOT EXISTS Bank_OLTP_Schema.investments (
    investment_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES Bank_OLTP_Schema.customers(customer_id), 
    investment_type VARCHAR,
    purchase_price NUMERIC(18, 2), 
    current_market_value NUMERIC(18, 2),
    investment_date TIMESTAMP
);

