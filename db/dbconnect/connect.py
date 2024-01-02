# Import necessary libraries for database connections
import pymysql
import psycopg2

# Import specific exceptions for Operational Errors from both libraries
from pymysql import OperationalError as MySQLOperationalError
from psycopg2 import OperationalError as PostgreSQLOperationalError
from db.dbconnect.config_db import dbconfig


# Import database configuration parameters from the config module



# Function to connect to MySQL database
def connect_mysql():
    try:
        # Retrieve MySQL connection parameters from the config module
        params = dbconfig('MYSQL_CONFIG')

        # Establish a connection to the MySQL database
        connection = pymysql.connect(**params)

        # Print a message indicating a successful connection
        # Uncomment the line below if you want to enable this print statement
        # print("MySQL Windows connected")

        return connection
    except MySQLOperationalError as e:
        # Handle MySQL connection errors and print an error message
        print(f"MySQL Connection Error: {e}")
        return None


# Function to connect to MariaDB database
def connect_mariadb():
    try:
        # Retrieve MariaDB connection parameters from the config module
        params = dbconfig("MARIADB_CONFIG")

        # Establish a connection to the MariaDB database
        connection = pymysql.connect(**params)

        # Print a message indicating a successful connection
        # Uncomment the line below if you want to enable this print statement
        # print("MariaDB connected")

        return connection
    except MySQLOperationalError as e:
        # Handle MariaDB connection errors and print an error message
        print(f"MariaDB Connection Error: {e}")
        return None


# Function to connect to PostgreSQL database
def connect_postgresql():
    try:
        # Retrieve PostgreSQL connection parameters from the config module
        params = dbconfig("POSTGRESQL_CONFIG")

        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**params)

        # Print a message indicating a successful connection
        # Uncomment the line below if you want to enable this print statement
        # print("PostgreSQL connected")

        return connection
    except PostgreSQLOperationalError as e:
        # Handle PostgreSQL connection errors and print an error message
        print(f"PostgreSQL Connection Error: {e}")
        return None
