# Import necessary libraries
import psycopg2
import pymysql

# Import database connection functions and product details function from custom modules
from db.dbconnect.connect import connect_mariadb, connect_postgresql
from db.product_test import product_details


def create_sales_by_payment_per_region_report():
    """
    connects to the databases(MySQL, PostgreSQL, and MariaDB) and qeries them to get the report
    :return: prints the report on the command line
    """
    # Print the title of the report
    print("Sales By Payment Per Region")

    # Define the regions for which the report is generated
    regions = ['nairobi','mombasa']

    # Loop through each region
    for region in regions:
        print(f"\nSales By Payment for {region}")
        # Connect to PostgreSQL to retrieve products from category tables
        post_connection = connect_postgresql()
        product_categories = ['electronics', 'clothing']

        # Check if the connection to PostgreSQL is successful
        if post_connection:
            post_cursor = post_connection.cursor()

            try:
                # Loop through each product category
                for product_category in product_categories:
                    # SQL query to retrieve all products for the current category
                    sql = "SELECT * FROM products_{}".format(product_category)
                    post_cursor.execute(sql)
                    products = post_cursor.fetchall()


                    print(f"\n{product_category}")
                    # Loop through each product
                    for product in products:
                        # Variable initialization
                        total_payment_paypal = 0.00
                        total_payment_credit = 0.00
                        credit_order = 0
                        paypal_order = 0
                        total_credit_quantity = 0
                        total_paypal_quantity = 0

                        # Unpack product details
                        product_id, product_name, category, _ = product


                        # Print product header
                        print(f"\n\tProduct: {product_name}")

                        # Connect to MariaDB to retrieve order details
                        mariadb_connection = connect_mariadb()

                        # Check if the connection to MariaDB is successful
                        if mariadb_connection:
                            mariadb_cursor = mariadb_connection.cursor()

                            try:
                                # SQL query to get orders that are connected to the current product ID and region
                                sql_orders = (
                                    "SELECT o.order_id, o.quantity FROM orders_{} o WHERE o.product_id = {}").format(
                                    region, product_id)
                                mariadb_cursor.execute(sql_orders)
                                orders_id = mariadb_cursor.fetchall()

                                # Loop through the generated order list to calculate the total amount per credit system
                                # and the total quantity
                                for order_id, credit_quantity in orders_id:
                                    # SQL query to get payment amount from credit card payments
                                    sql_payments_credit = (
                                        "SELECT p.payment_amount FROM payments_credit_card p WHERE p.order_id= {}").format(
                                        order_id)
                                    mariadb_cursor.execute(sql_payments_credit)
                                    payment_credit = mariadb_cursor.fetchall()

                                    # Check if payment_credit is not empty
                                    if payment_credit:
                                        payment_credit_tuple = payment_credit[0]
                                        pay = payment_credit_tuple[0]
                                        total_payment_credit += float(pay)
                                        credit_order += 1
                                        total_credit_quantity += credit_quantity

                                # Print the report for credit card payments
                                print("\tcredit card payments")
                                print(
                                    f"\t   {product_details(product_id, product_category)} total order: {credit_order}, Quantity: {total_credit_quantity}, payment: Credit, Amount: {total_payment_credit}")

                                # Loop through the order list again to calculate the total amount per Paypal system
                                # and the total quantity

                                for order_id, paypal_quantity in orders_id:
                                    # SQL query to get payment amount from Paypal payments
                                    sql_payments_paypal = (
                                        "SELECT p.payment_amount FROM payments_paypal p WHERE p.order_id= {}").format(
                                        order_id)
                                    mariadb_cursor.execute(sql_payments_paypal)
                                    payment_paypal = mariadb_cursor.fetchone()

                                    # Check if payment_paypal is not empty and calculate the total payment and quantity
                                    if payment_paypal:
                                        payment_paypal_tuple = payment_paypal[0]
                                        pay = payment_paypal_tuple[0]
                                        total_payment_paypal += float(pay)
                                        paypal_order += 1
                                        total_paypal_quantity += paypal_quantity

                                # Print the report for Paypal payments
                                print("\tpaypal payments")
                                print(
                                    f"\t   {product_details(product_id, product_category)} total order: {paypal_order}, Quantity: {total_paypal_quantity}, payment: Paypal, Amount: {total_payment_paypal}")

                            except pymysql.Error as e:
                                print(f"Mariadb Error: {e}")

                            finally:
                                mariadb_cursor.close()
                                mariadb_connection.close()

                    # Print a message indicating the completion of the current product category
                    # print(f'Finished {product_category} category\n')

            except psycopg2.Error as e:
                print(f"PostgreSQL Error: {e}")

            finally:
                post_cursor.close()
                post_connection.close()


