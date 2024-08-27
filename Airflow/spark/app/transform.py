from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, TimestampType,DateType

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
    StructField("account_open_date", DateType(), nullable=True),
    StructField("account_status", StringType(), nullable=True),
])

# Schema cho Transactions
transactions_schema = StructType([
    StructField("transaction_id", StringType(), nullable=False),
    StructField("account_id", StringType(), nullable=True),
    StructField("transaction_type", StringType(), nullable=True),
    StructField("transaction_amount", DecimalType(18, 2), nullable=True),
    StructField("transaction_date", DateType(), nullable=True),
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
    StructField("loan_start_date", DateType(), nullable=True),
    StructField("loan_end_date", DateType(), nullable=True),
    StructField("loan_status", StringType(), nullable=True),
])

# Schema cho Credit Cards
credit_cards_schema = StructType([
    StructField("card_id", StringType(), nullable=False),
    StructField("customer_id", StringType(), nullable=True),
    StructField("card_number", StringType(), nullable=True),
    StructField("card_expiry_date", DateType(), nullable=True),
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
    StructField("change_date", DateType(), nullable=True),
])

# Schema cho Payment
payment_schema = StructType([
    StructField("payment_id", StringType(), nullable=False),
    StructField("order_id", StringType(), nullable=True),
    StructField("payment_date", DateType(), nullable=True),
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
    StructField("investment_date", DateType(), nullable=True),
])
class DataCleaner:
    def __init__(self, data_dir, snowflake_options):
        self.spark = SparkSession.builder \
            .appName("DataCleaning") \
            .getOrCreate()
        
        self.data_dir = data_dir
        self.snowflake_options = snowflake_options

    def read_csv(self, file_name, schema):
        """Đọc dữ liệu từ file CSV với schema đã định nghĩa."""
        try:
            df = self.spark.read.option("header", "true").schema(schema).csv(self.data_dir + file_name)
            return df
        except Exception as e:
            print(f"Lỗi khi đọc file {file_name}: {e}")
            return None

    def write_to_snowflake(self, df, table_name):   
        """Ghi DataFrame vào bảng Snowflake."""
        try:
            df.write \
                .format("snowflake") \
                .options(**self.snowflake_options) \
                .option("dbtable", table_name) \
                .mode("overwrite") \
                .save()
            print(f"Dữ liệu đã được ghi vào bảng {table_name} trên Snowflake.")
        except Exception as e:
            print(f"Lỗi khi ghi dữ liệu vào bảng {table_name}: {e}")

    def clean_customers(self):
        try:
            df = self.read_csv("customers.csv", customers_schema)
            if df is not None:
                df = df.withColumn("customer_email", when(col("customer_email").isNull(), lit("unknown@example.com")).otherwise(col("customer_email")))
                df = df.withColumn("customer_phone", when(col("customer_phone").rlike(r"^\d{10,15}$"), col("customer_phone")).otherwise(lit("0000000000")))
                self.write_to_snowflake(df, "Bank_Schema.customers")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng customers: {e}")

    def clean_accounts(self):
        try:
            df = self.read_csv("accounts.csv", accounts_schema)
            if df is not None:
                df = df.withColumn("account_balance", when(col("account_balance").cast(DecimalType(18, 2)) < 0, lit(0.0)).otherwise(col("account_balance")))
                self.write_to_snowflake(df, "Bank_Schema.accounts")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng accounts: {e}")

    def clean_transactions(self):
        try:
            df = self.read_csv("transactions.csv", transactions_schema)
            if df is not None:
                df = df.withColumn("transaction_amount", when(col("transaction_amount").cast(DecimalType(18, 2)) < 0, lit(0.0)).otherwise(col("transaction_amount")))
                self.write_to_snowflake(df, "Bank_Schema.transactions")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng transactions: {e}")

    def clean_branches(self):
        try:
            df = self.read_csv("branches.csv", branches_schema)
            if df is not None:
                df = df.withColumn("branch_city", when(col("branch_city").isNull(), lit("Unknown City")).otherwise(col("branch_city")))
                self.write_to_snowflake(df, "Bank_Schema.branches")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng branches: {e}")

    def clean_loans(self):
        try:
            df = self.read_csv("loans.csv", loans_schema)
            if df is not None:
                df = df.withColumn("loan_end_date", when(col("loan_end_date") < col("loan_start_date"), col("loan_start_date").cast(DateType())).otherwise(col("loan_end_date")))
                self.write_to_snowflake(df, "Bank_Schema.loans")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng loans: {e}")

    def clean_credit_cards(self):
        try:
            df = self.read_csv("credit_cards.csv", credit_cards_schema)
            if df is not None:
                df = df.withColumn("card_balance", when(col("card_balance").cast(DecimalType(18, 2)) > col("card_limit").cast(DecimalType(18, 2)), col("card_limit")).otherwise(col("card_balance")))
                self.write_to_snowflake(df, "Bank_Schema.credit_cards")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng credit_cards: {e}")

    def clean_investments(self):
        try:
            df = self.read_csv("investments.csv", investments_schema)
            if df is not None:
                df = df.withColumn("current_market_value", when(col("current_market_value").cast(DecimalType(18, 2)) < col("purchase_price").cast(DecimalType(18, 2)), col("purchase_price")).otherwise(col("current_market_value")))
                self.write_to_snowflake(df, "Bank_Schema.investments")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng investments: {e}")

    def clean_transaction_history(self):
        try:
            df = self.read_csv("transaction_history.csv", transaction_history_schema)
            if df is not None:
                self.write_to_snowflake(df, "Bank_Schema.transaction_history")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng transaction_history: {e}")

    def clean_payment(self):
        try:
            df = self.read_csv("payment.csv", payment_schema)
            if df is not None:
                self.write_to_snowflake(df, "Bank_Schema.payment")
        except Exception as e:
            print(f"Lỗi khi làm sạch dữ liệu bảng payment: {e}")
    
    def clean_all(self):
        """Gọi hàm làm sạch dữ liệu cho tất cả các bảng."""
        self.clean_customers()
        self.clean_accounts()
        self.clean_transactions()
        self.clean_branches()
        self.clean_loans()
        self.clean_credit_cards()
        self.clean_investments()
        self.clean_transaction_history()
        self.clean_payment()

    def stop(self):
        """Dừng Spark Session."""
        self.spark.stop()

# Cấu hình thông tin kết nối Snowflake
snowflake_options = {
    "sfURL": "https://oumjqhi-bmb56296.snowflakecomputing.com",
    "sfUser": "THanh",
    "sfPassword": "Thanh1234",
    "sfDatabase": "Bank_DW_DB",
    "sfSchema": "Bank_Schema",
    "sfWarehouse": "Bank_DW",
}

# Sử dụng lớp DataCleaner trong DAG hoặc script khác
if __name__ == "__main__":
    data_cleaner = DataCleaner("/data/", snowflake_options)
    data_cleaner.clean_all()
    data_cleaner.stop()