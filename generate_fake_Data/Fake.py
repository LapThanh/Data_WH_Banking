import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Connect to PostgreSQL
conn = psycopg2.connect(
    user="postgres",
    password="123456",
    host="host.docker.internal",
    port="5432",
    database="Bank_DB"
)
conn.autocommit = True
cur = conn.cursor()

# Initialize lists to store generated IDs
customer_ids = []
account_ids = []
transaction_ids = []

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Function to generate fake customers with errors
def generate_customers(n, error_rate):
    global customer_ids
    for _ in range(n):
        customer_id = fake.uuid4()
        email = fake.email()
        phone = fake.phone_number()
        # Add errors with a certain probability
        if random.random() < error_rate:  # Error rate for missing email
            email = None
        if random.random() < error_rate:  # Error rate for incorrect phone format
            phone = fake.word()
        cur.execute("""
            INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            customer_id,
            fake.name(),
            email,
            phone,
            fake.address(),
            fake.city(),
            fake.state_abbr(),
            fake.zipcode()
        ))
        customer_ids.append(customer_id)

# Function to generate fake accounts with errors
def generate_accounts(n):
    global account_ids
    for _ in range(n):
        account_id = fake.uuid4()
        balance = round(random.uniform(1000.00, 100000.00), 2)
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for invalid balance
            balance = -balance  # Negative balance
        cur.execute("""
            INSERT INTO accounts (account_id, customer_id, account_type, account_balance, account_open_date, account_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            account_id,
            random.choice(customer_ids),  # Use a customer_id from generated customers
            fake.random_element(elements=('Savings', 'Checking', 'Credit', 'Loan')),
            balance,
            fake.date_time_this_decade(),
            fake.random_element(elements=('Active', 'Inactive', 'Closed'))
        ))
        account_ids.append(account_id)

# Function to generate fake transactions with errors
def generate_transactions(n):
    global transaction_ids
    for _ in range(n):
        transaction_id = fake.uuid4()
        amount = round(random.uniform(10.00, 10000.00), 2)
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for invalid amount
            amount = -amount  # Negative amount
        cur.execute("""
            INSERT INTO transactions (transaction_id, account_id, transaction_type, transaction_amount, transaction_date, transaction_description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            transaction_id,
            random.choice(account_ids),  # Use an account_id from generated accounts
            fake.random_element(elements=('Deposit', 'Withdrawal', 'Transfer', 'Payment')),
            amount,
            fake.date_time_this_year(),
            fake.sentence(nb_words=6)
        ))
        transaction_ids.append(transaction_id)

# Function to generate fake branches with errors
def generate_branches(n):
    for _ in range(n):
        branch_city = fake.city()
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for missing city
            branch_city = None
        cur.execute("""
            INSERT INTO branches (branch_id, branch_name, branch_address, branch_city, branch_state, branch_zip_code)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            fake.company(),
            fake.address(),
            branch_city,
            fake.state_abbr(),
            fake.zipcode()
        ))

# Function to generate fake loans with errors
def generate_loans(n):
    for _ in range(n):
        start_date = random_date(datetime(2015, 1, 1), datetime(2024, 1, 1))
        end_date = random_date(datetime(2024, 1, 1), datetime(2030, 1, 1))
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for end_date before start_date
            end_date = random_date(start_date, start_date + timedelta(days=365))
        cur.execute("""
            INSERT INTO loans (loan_id, loan_type, customer_id, loan_amount, loan_interest_rate, loan_start_date, loan_end_date, loan_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            fake.random_element(elements=('Personal', 'Home', 'Auto', 'Education', 'Business')),
            random.choice(customer_ids),  # Use a customer_id from generated customers
            round(random.uniform(50.00, 1000.00), 2),
            round(random.uniform(1.5, 15.0), 2),
            start_date,
            end_date,
            fake.random_element(elements=('Active', 'Closed', 'Default'))
        ))

# Function to generate fake credit cards with errors
def generate_credit_cards(n):
    for _ in range(n):
        card_limit = round(random.uniform(1000.00, 100000.00), 2)
        card_balance = round(random.uniform(0.00, 100000.00), 2)
        # Add errors with a certain probability
        if card_balance > card_limit:
            card_balance = card_limit  # Ensure balance does not exceed card limit
        cur.execute("""
            INSERT INTO credit_cards (card_id, customer_id, card_number, card_expiry_date, card_limit, card_balance, card_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            random.choice(customer_ids),  # Use a customer_id from generated customers
            fake.credit_card_number(),
            fake.date_this_decade(),
            card_limit,
            card_balance,
            fake.random_element(elements=('Active', 'Inactive', 'Blocked'))
        ))

# Function to generate fake transactions history with errors
def generate_transaction_history(n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO transaction_history (history_id, account_id, transaction_id, change_description, change_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            random.choice(account_ids),  # Use an account_id from generated accounts
            random.choice(transaction_ids),  # Use a transaction_id from generated transactions
            fake.sentence(nb_words=6),
            fake.date_time_this_year()
        ))

# Function to generate fake payments with errors
def generate_payments(n):
    for _ in range(n):
        amount = round(random.uniform(10.00, 10000.00), 2)
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for amount less than 0
            amount = -amount
        cur.execute("""
            INSERT INTO payment (payment_id, order_id, payment_date, amount, payment_method, currency, status, customer_id, transaction_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            fake.uuid4(),
            fake.date_time_this_year(),
            amount,
            fake.random_element(elements=('Credit Card', 'Debit Card', 'Bank Transfer', 'Cash')),
            fake.currency_code(),
            fake.random_element(elements=('Completed', 'Pending', 'Failed')),
            random.choice(customer_ids),  # Use a customer_id from generated customers
            random.choice(transaction_ids)  # Use a transaction_id from generated transactions
        ))

# Function to generate fake investments with errors
def generate_investments(n):
    for _ in range(n):
        purchase_price = round(random.uniform(1000.00, 100000.00), 2)
        current_market_value = round(random.uniform(1000.00, 200000.00), 2)
        # Add errors with a certain probability
        if random.random() < 0.05:  # 5% chance for current_market_value less than purchase_price
            current_market_value = min(current_market_value, purchase_price - 1)
        cur.execute("""
            INSERT INTO investments (investment_id, customer_id, investment_type, purchase_price, current_market_value, investment_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            fake.uuid4(),
            random.choice(customer_ids),  # Use a customer_id from generated customers
            fake.random_element(elements=('Stocks', 'Bonds', 'Mutual Funds', 'Real Estate')),
            purchase_price,
            current_market_value,
            fake.date_time_this_decade()
        ))

n = 1000
# Generate fake data with errors
generate_customers(n, error_rate=0.1)
generate_accounts(n)
generate_transactions(n)
generate_branches(n)
generate_loans(n)
generate_credit_cards(n)
generate_transaction_history(n)
generate_payments(n)
generate_investments(n)

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Data generation with errors completed.")
