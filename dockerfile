# Dockerfile for Airflow
FROM apache/airflow:latest

# Cài đặt Java
USER root

# Cài đặt OpenJDK-11 và ant
RUN apt update && \
    apt-get install -y default-jdk ant && \
    apt-get clean

# Thiết lập JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Đặt lại quyền sở hữu cho thư mục Airflow nếu cần
RUN chown -R airflow: ${AIRFLOW_HOME}

USER airflow

# Xác nhận Java đã được cài đặt
RUN java -version
