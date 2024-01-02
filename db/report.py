import psycopg2
import pymysql

from db.connect import connect_mysql, connect_postgresql, connect_mariadb
from db.product_test import product_details


def create_customer_report():
    # Connect to MySQL to retrieve customer data
    mysql_connection = connect_mysql()
    if mysql_connection:
        mysql_cursor = mysql_connection.cursor()
        try:
            mysql_cursor.execute("SELECT customer_id, customer_name FROM customers_nar")
            customers = mysql_cursor.fetchall()
            print(customers)


            # Connect to MariaDB to retrieve order details
            mariadb_connection = connect_mariadb()
            if mariadb_connection:
                mariadb_cursor = mariadb_connection.cursor()
                try:
                    # Create a report by fetching order details for each customer
                    for customer_id, customer_name in customers:
                        sql = "SELECT o.order_id, o.product_id, o.quantity,p.payment_amount, o.order_date FROM orders o JOIN payments p ON o.order_id = p.order_id WHERE o.customer_id = {}".format(customer_id)
                        mariadb_cursor.execute(sql)
                        orders = mariadb_cursor.fetchall()

                        print(f"Customer Report for {customer_name} (Customer ID: {customer_id}):")

                        for order in orders:
                            # connect to postgreSQL to retrieve the product details
                            product_detail = product_details(f"{order[1]}")
                            print(f"Order ID: {order[0]}, {product_detail}, Quantity: {order[2]}, Date: {order[3]}")
                        print("\n")

                except pymysql.Error as e:
                    print(f"mariadb Error: {e}")
                finally:
                    mariadb_cursor.close()
                    mariadb_connection.close()

        except pymysql.Error as e:
            print(f"MySQL Error: {e}")
        finally:
            mysql_cursor.close()
            mysql_connection.close()


if __name__ == "__main__":
    create_customer_report()
