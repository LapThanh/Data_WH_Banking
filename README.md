Data_WH_Banking


Đây là một dự án thiết kế và triển khai kho dữ liệu (Data Warehouse) dành cho hoạt động ngân hàng. Dự án cung cấp một khung làm việc toàn diện cho việc quản lý, chuyển đổi và phân tích dữ liệu ngân hàng, sử dụng các công cụ hiện đại như Apache Airflow, Apache Spark, PostgreSQL, và Snowflake.

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

Tổng quan về dự :


Dự án này sẽ dùng faker để sinh dữ 1 triệu dòng dữ liệu giả lập cho ngân hàng, data sẽ được chuẩn hóa và đưa vào hệ quản trị cơ sở dữ liệu PostgesSql.Đồng thời, project này cũng được sinh ra 1 số lỗi để thực hiện trong quá trình transform, tất cả sẽ tích hợp trong phần foler GENERATE_FAKE_DATA
![image](https://github.com/user-attachments/assets/0561eb70-e2c6-452f-acb6-b5b3049b741a)

 


![image](https://github.com/user-attachments/assets/41eead71-c152-4fff-82d5-9cb7436c2e5a)

Sau khi data được sinh ra, mình sẽ dùng pandas để đọc đữ liệu, đồng thời chuyển hóa thành các file csv trong folder data để có thể theo dõi raw data, sau đó Spark sẽ thực hiện làm sạch dữ liệu và load vào snowflake 

![image](https://github.com/user-attachments/assets/62422551-b4d4-4cfd-a1af-4b9d0bc78f0e)



Data warehouse sẽ được thiết kế theo mô hình schema và phương pháp của kimball :


![image](https://github.com/user-attachments/assets/160f7da9-b848-4390-a5b5-2b03caf26025)



sau khi đã được load vào warehouse mình sẽ phân tích dữ liệu bằng tableu 


![image](https://github.com/user-attachments/assets/00dc1ab7-ef14-4b16-a280-0a4175c2ad76)



và mọi thứ sẽ được lập lịch bằng airflow mỗi ngày, bao gồm việc sinh ra 1 triệu record mỗi bảng:

![image](https://github.com/user-attachments/assets/357517dd-5f62-4322-b3d8-017b730fa033)


![image](https://github.com/user-attachments/assets/11bf4274-911c-4fac-a4c3-0e12935ef007)







