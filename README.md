Data_WH_Banking
Chào mừng bạn đến với dự án Data_WH_Banking! Đây là một dự án thiết kế và triển khai kho dữ liệu (Data Warehouse) dành cho hoạt động ngân hàng. Dự án cung cấp một khung làm việc toàn diện cho việc quản lý, chuyển đổi và phân tích dữ liệu ngân hàng, sử dụng các công cụ hiện đại như Apache Airflow, Apache Spark, PostgreSQL, và Snowflake.

Tổng Quan Dự Án
Trong môi trường ngân hàng đầy thách thức, việc sở hữu một kho dữ liệu mạnh mẽ và có khả năng mở rộng là vô cùng quan trọng để xử lý khối lượng lớn giao dịch, dữ liệu khách hàng, các khoản vay, đầu tư, và nhiều hơn nữa. Dự án này trình bày một giải pháp hoàn chỉnh từ việc tạo dữ liệu đến các quy trình ETL và cuối cùng là lưu trữ dữ liệu.

Các Tính Năng Chính
Pipeline ETL với Airflow:

Tự động hóa việc trích xuất dữ liệu từ PostgreSQL.
Chuyển đổi dữ liệu sử dụng Apache Spark.
Tải dữ liệu vào Snowflake để phục vụ cho phân tích nâng cao.
Định Nghĩa và Lược Đồ Dữ Liệu:

Lược đồ dữ liệu được định nghĩa rõ ràng cho các thực thể như Khách hàng, Tài khoản, Giao dịch, Khoản vay, Thẻ tín dụng, và Đầu tư.
Lược đồ Snowflake và các bảng dữ liệu được thiết kế để tối ưu hóa hiệu suất truy vấn.
Tạo Dữ Liệu:

Các script Python tùy chỉnh sử dụng thư viện Faker để tạo dữ liệu ngân hàng thực tế với tỷ lệ lỗi được kiểm soát, cho phép mô phỏng các kịch bản thực tế.
Môi Trường Docker Hóa:

Cấu hình Docker Compose để dễ dàng khởi chạy toàn bộ pipeline xử lý dữ liệu từ PostgreSQL đến Airflow và Spark.
Làm Sạch Dữ Liệu và Kiểm Tra Chất Lượng:

Làm sạch dữ liệu bằng Spark để đảm bảo tính toàn vẹn của dữ liệu trước khi tải vào kho dữ liệu.
Hướng Dẫn Cài Đặt
Yêu Cầu Trước
Docker & Docker Compose
Python 3.8+
PostgreSQL
Apache Airflow
