import pandas as pd
from sqlalchemy import create_engine

def read_table_from_postgresql(engine, table_name):
    try:
        # Đọc dữ liệu từ bảng PostgreSQL vào DataFrame
        df = pd.read_sql_table(table_name, engine)
        return df
    except Exception as e:
        print(f"Lỗi khi đọc bảng {table_name}: {e}")
        return None

def write_dataframe_to_csv(df, path):
    try:
        # Ghi dữ liệu vào file CSV
        df.to_csv(path, index=False)
        print(f"Dữ liệu đã được lưu vào {path}")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu vào {path}: {e}")

def main():
    # Cấu hình kết nối PostgreSQL
    db_url = "postgresql://postgres:123456@host.docker.internal/Bank_DB"
    engine = create_engine(db_url)

    # Danh sách các bảng cần đọc
    tables = [
        'customers',
        'accounts',
        'transactions',
        'branches',
        'loans',
        'credit_cards',
        'transaction_history',
        'payment',
        'investments'
    ]

    # Đọc dữ liệu từ từng bảng và lưu vào định dạng CSV
    for table in tables:
        df = read_table_from_postgresql(engine, table)
        if df is not None:
            write_dataframe_to_csv(df, f"/data/{table}.csv")

if __name__ == "__main__":
    main()
