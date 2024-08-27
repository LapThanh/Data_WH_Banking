CREATE OR REPLACE TABLE DimCustomer (
    customer_id VARCHAR PRIMARY KEY,
    customer_name VARCHAR,
    customer_email VARCHAR,
    customer_phone VARCHAR,
    customer_address VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR,
    customer_zip_code VARCHAR
);
CREATE OR REPLACE TABLE DimAccount (
    account_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    account_type VARCHAR,
    account_balance NUMERIC,
    account_open_date TIMESTAMP,
    account_status VARCHAR,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(customer_id)
);
CREATE OR REPLACE TABLE DimBranch (
    branch_id VARCHAR PRIMARY KEY,
    branch_name VARCHAR,
    branch_address VARCHAR,
    branch_city VARCHAR,
    branch_state VARCHAR,
    branch_zip_code VARCHAR
);
CREATE OR REPLACE TABLE DimProduct (
    product_id VARCHAR PRIMARY KEY,
    product_type VARCHAR,
    product_name VARCHAR
);
CREATE OR REPLACE TABLE DimDate (
    date_id DATE PRIMARY KEY,
    date STRING,
    month INT,
    quarter INT,
    year INT
);

-- TAO DU LIEU CHO DIM DATE TRONG SNOWFLAKE 
CREATE OR REPLACE TEMPORARY TABLE TempDates AS
SELECT
    DATEADD(day, seq4(), '2000-01-01') AS date_id
FROM TABLE(GENERATOR(ROWCOUNT => 11323)); -- Tổng số ngày từ 2000-01-01 đến 2030-12-31
INSERT INTO DimDate (date_id, date, month, quarter, year)
SELECT
    date_id,
    EXTRACT(DAY FROM date_id) AS date,
    EXTRACT(MONTH FROM date_id) AS month,
    EXTRACT(QUARTER FROM date_id) AS quarter,
    EXTRACT(YEAR FROM date_id) AS year
FROM TempDates;