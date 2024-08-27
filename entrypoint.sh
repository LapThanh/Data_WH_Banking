#!/bin/bash
set -e

if [ -e "/usr/local/requirements.txt" ]; then
  $(command python) pip install --upgrade pip
  $(command -v pip) install  -r /usr/local/requirements.txt
fi

if [ ! -f "/usr/local/airflow.db" ]; then
  airflow db init && \
  airflow users create \
    --username Lapthanh \
    --firstname lap \
    --lastname thanh \
    --role Admin \
    --email Thanh@123.com \
    --password 123
fi

$(command -v airflow) db upgrade

exec airflow webserver