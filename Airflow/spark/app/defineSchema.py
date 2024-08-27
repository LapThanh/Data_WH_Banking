from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, TimestampType, TextType

# Định nghĩa schema cho từng bảng

# Schema cho Customers
customers_schema = StructType([
    StructField("customer_id", StringType(), nullable=False),
    StructField("customer_name", StringType(), nullable=True),
    StructField("customer_email", StringType(), nullable=True),
    StructField("customer_phone", StringType(), nullable=True),
    StructField("customer_address", StringType(), nullable=True),
    StructField("customer_city", StringType(), nullable=True),
    StructField("customer_state", StringType(), nullable=True),
    StructField("customer_zip_code", StringType(), nullable=True),
])

# Schema cho Accounts
accounts_schema = StructType([
    StructField("account_id", StringType(), nullable=False),
    StructField("customer_id", StringType(), nullable=True),
    StructField("account_type", StringType(), nullable=True),
    StructField("account_balance", DecimalType(18, 2), nullable=True),
    StructField("account_open_date", TimestampType(), nullable=True),
    StructField("account_status", StringType(), nullable=True),
])

# Schema cho Transactions
transactions_schema = StructType([
    StructField("transaction_id", StringType(), nullable=False),
    StructField("account_id", StringType(), nullable=True),
    StructField("transaction_type", StringType(), nullable=True),
    StructField("transaction_amount", DecimalType(18, 2), nullable=True),
    StructField("transaction_date", TimestampType(), nullable=True),
    StructField("transaction_description", StringType(), nullable=True),
])

# Schema cho Branches
branches_schema = StructType([
    StructField("branch_id", StringType(), nullable=False),
    StructField("branch_name", StringType(), nullable=True),
    StructField("branch_address", StringType(), nullable=True),
    StructField("branch_city", StringType(), nullable=True),
    StructField("branch_state", StringType(), nullable=True),
    StructField("branch_zip_code", StringType(), nullable=True),
])

# Schema cho Loans
loans_schema = StructType([
    StructField("loan_id", StringType(), nullable=False),
    StructField("loan_type", StringType(), nullable=True),
    StructField("customer_id", StringType(), nullable=True),
    StructField("loan_amount", IntegerType(), nullable=True),
    StructField("loan_interest_rate", IntegerType(), nullable=True),
    StructField("loan_start_date", TimestampType(), nullable=True),
    StructField("loan_end_date", TimestampType(), nullable=True),
    StructField("loan_status", StringType(), nullable=True),
])

# Schema cho Credit Cards
credit_cards_schema = StructType([
    StructField("card_id", StringType(), nullable=False),
    StructField("customer_id", StringType(), nullable=True),
    StructField("card_number", StringType(), nullable=True),
    StructField("card_expiry_date", TimestampType(), nullable=True),
    StructField("card_limit", DecimalType(18, 2), nullable=True),
    StructField("card_balance", DecimalType(18, 2), nullable=True),
    StructField("card_status", StringType(), nullable=True),
])

# Schema cho Transaction History
transaction_history_schema = StructType([
    StructField("history_id", StringType(), nullable=False),
    StructField("account_id", StringType(), nullable=True),
    StructField("transaction_id", StringType(), nullable=True),
    StructField("change_description", StringType(), nullable=True),
    StructField("change_date", TimestampType(), nullable=True),
])

# Schema cho Payment
payment_schema = StructType([
    StructField("payment_id", StringType(), nullable=False),
    StructField("order_id", StringType(), nullable=True),
    StructField("payment_date", TimestampType(), nullable=True),
    StructField("amount", DecimalType(10, 2), nullable=True),
    StructField("payment_method", StringType(), nullable=True),
    StructField("currency", StringType(), nullable=True),
    StructField("status", StringType(), nullable=True),
    StructField("customer_id", StringType(), nullable=True),
    StructField("transaction_id", StringType(), nullable=True),
])

# Schema cho Investments
investments_schema = StructType([
    StructField("investment_id", StringType(), nullable=False),
    StructField("customer_id", StringType(), nullable=True),
    StructField("investment_type", StringType(), nullable=True),
    StructField("purchase_price", DecimalType(18, 2), nullable=True),
    StructField("current_market_value", DecimalType(18, 2), nullable=True),
    StructField("investment_date", TimestampType(), nullable=True),
])