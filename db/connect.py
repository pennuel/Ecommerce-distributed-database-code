import pymysql
import psycopg2
from pymysql import OperationalError as MySQLOperationalError
from psycopg2 import OperationalError as PostgreSQLOperationalError

# MySQL Connection Parameters
mysql_config = {
    'host': 'Paul-s-macbook',
    'user': 'root',
    'password': 'root',
    'database': 'e_commerce_site1_customers'
}

# PostgreSQL Connection Parameters
postgresql_config = {
    'user': 'root',
    'password': 'root',
    'host': '192.168.52.128',  # Assuming PostgreSQL is on this VM
    'port': '5432',
    'database': 'e_commerce_site2'
}

# MariaDB Connection Parameters
mariadb_config = {
    'host': '192.168.52.129',  # Assuming MariaDB is on this VM
    'user': 'rootuser1',
    'password': 'root',
    'database': 'e_commerce_site3_payment_order'
}


def connect_mysql():
    try:
        connection = pymysql.connect(**mysql_config)
        # print("mysql windows connected")
        return connection
    except MySQLOperationalError as e:
        print(f"MySQL Connection Error: {e}")
        return None


def connect_mariadb():
    try:
        connection = pymysql.connect(**mariadb_config)
        # print("mariadb connected")
        return connection
    except MySQLOperationalError as e:
        print(f"mariadb Connection Error: {e}")
        return None


def connect_postgresql():
    try:
        connection = psycopg2.connect(**postgresql_config)
        # print("postgres connected")
        count=1
        return connection
    except PostgreSQLOperationalError as e:
        print(f"PostgreSQL Connection Error: {e}")
        return None