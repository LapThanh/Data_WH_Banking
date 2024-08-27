import psycopg2

# Kết nối đến PostgreSQL
conn = psycopg2.connect(
    user="postgres",
    password="123456",
    host="localhost",
    port="5432",
    database="Bank_DB"
)
conn.autocommit = True

cur = conn.cursor()

# Tạo bảng Customers
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR PRIMARY KEY,
    customer_name VARCHAR,
    customer_email VARCHAR ,
    customer_phone VARCHAR,
    customer_address VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR,
    customer_zip_code VARCHAR
);
""")

# Tạo bảng Accounts
cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    account_type VARCHAR,
    account_balance NUMERIC,
    account_open_date TIMESTAMP,
    account_status VARCHAR
);
""")

# Tạo bảng Transactions
cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR PRIMARY KEY,
    account_id VARCHAR REFERENCES accounts(account_id),
    transaction_type VARCHAR,
    transaction_amount NUMERIC,
    transaction_date TIMESTAMP,
    transaction_description TEXT
);
""")

# Tạo bảng Branches
cur.execute("""
CREATE TABLE IF NOT EXISTS branches (
    branch_id VARCHAR PRIMARY KEY,
    branch_name VARCHAR,
    branch_address VARCHAR,
    branch_city VARCHAR,
    branch_state VARCHAR,
    branch_zip_code VARCHAR
);
""")


# Tạo bảng Loans
cur.execute("""
CREATE TABLE IF NOT EXISTS loans (
    loan_id VARCHAR PRIMARY KEY,
    loan_type VARCHAR,
    customer_id VARCHAR REFERENCES customers(customer_id),
    loan_amount int,
    loan_interest_rate int,
    loan_start_date TIMESTAMP,
    loan_end_date TIMESTAMP,
    loan_status VARCHAR
);
""")

# Tạo bảng Credit Cards
cur.execute("""
CREATE TABLE IF NOT EXISTS credit_cards (
    card_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    card_number VARCHAR UNIQUE,
    card_expiry_date TIMESTAMP,
    card_limit NUMERIC,
    card_balance NUMERIC,
    card_status VARCHAR
);
""")

# Tạo bảng Transactions History
cur.execute("""
CREATE TABLE IF NOT EXISTS transaction_history (
    history_id VARCHAR PRIMARY KEY,
    account_id VARCHAR REFERENCES accounts(account_id),
    transaction_id VARCHAR REFERENCES transactions(transaction_id),
    change_description TEXT,
    change_date TIMESTAMP
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS payment (
    payment_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    payment_date TIMESTAMP,
    amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    currency VARCHAR(10),
    status VARCHAR(20),
    customer_id VARCHAR(50),
    transaction_id VARCHAR(50)
);""")
cur.execute("""
CREATE TABLE IF NOT EXISTS investments (
    investment_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id), 
    investment_type VARCHAR(100),
    purchase_price DECIMAL(18, 2), 
    current_market_value DECIMAL(18, 2),
    investment_date TIMESTAMP 
);
            """)

# Commit các thay đổi
conn.commit()

# Đóng cursor và kết nối
cur.close()
conn.close()
