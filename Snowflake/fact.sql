CREATE OR REPLACE TABLE FactTransaction (
    transaction_id VARCHAR PRIMARY KEY,
    transaction_date DATE,
    account_id VARCHAR,
    branch_id VARCHAR,
    product_id VARCHAR,
    transaction_amount NUMERIC,
    transaction_type VARCHAR,
    FOREIGN KEY (account_id) REFERENCES DimAccount(account_id),
    FOREIGN KEY (branch_id) REFERENCES DimBranch(branch_id),
    FOREIGN KEY (product_id) REFERENCES DimProduct(product_id),
    FOREIGN KEY (transaction_date) REFERENCES DimDate(date_id)
);
CREATE OR REPLACE TABLE FactLoan (
    loan_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    product_id VARCHAR,
    loan_amount NUMERIC,
    loan_interest_rate NUMERIC,
    loan_start_date DATE,
    loan_end_date DATE,
    loan_status VARCHAR,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(customer_id),
    FOREIGN KEY (product_id) REFERENCES DimProduct(product_id),
    FOREIGN KEY (loan_start_date) REFERENCES DimDate(date_id),
    FOREIGN KEY (loan_end_date) REFERENCES DimDate(date_id)
);
CREATE OR REPLACE TABLE FactInvestment (
    investment_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    product_id VARCHAR,
    investment_amount NUMERIC,
    investment_date DATE,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(customer_id),
    FOREIGN KEY (product_id) REFERENCES DimProduct(product_id),
    FOREIGN KEY (investment_date) REFERENCES DimDate(date_id)
);
CREATE OR REPLACE TABLE FactPayment (
    payment_id VARCHAR PRIMARY KEY,
    order_id VARCHAR,
    payment_date DATE,
    amount NUMERIC,
    payment_method VARCHAR,
    currency VARCHAR,
    status VARCHAR,
    customer_id VARCHAR,
    transaction_id VARCHAR,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(customer_id),
    FOREIGN KEY (payment_date) REFERENCES DimDate(date_id)
);
