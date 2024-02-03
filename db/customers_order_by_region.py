import psycopg2
import pymysql

from db.dbconnect.connect import connect_mariadb, connect_postgresql, connect_mysql
from db.product_test import product_details

def create_customer_report():
    """
    This function connects to the databases and queries them to create the customer order summary report
    :return: prints the report in the command line
    """
    # Connect to MySQL to retrieve customer data
    mysql_connection = connect_mysql()

    # Define the regions for which the report is generated

    if mysql_connection:
        mysql_cursor = mysql_connection.cursor()
        try:
            regions = ['nairobi', 'mombasa']
            for region in regions:
                print(f"customers from {region}")
                sql = "SELECT customer_id, customer_name FROM customers_{}".format(region)
                mysql_cursor.execute(sql)
                customers = mysql_cursor.fetchall()
                # Create a report by fetching order details for each customer
                for customer_id, customer_name in customers:
                    print(f"\nCustomer Report for {customer_name} (Customer ID: {customer_id}):")
                    #connect to post to retrieve products from caterogy tables
                    post_connection = connect_postgresql()
                    product_categories = ['electronics','clothing']
                    if post_connection:
                        post_cursor = post_connection.cursor()
                        try:
                            for product_category in product_categories:
                                sql = "SELECT * FROM products_{}".format(product_category)
                                post_cursor.execute(sql)
                                products = post_cursor.fetchall()

                                print(f"  {product_category}")
                                for product in products:
                                    # count+=1
                                    # print(count)
                                    # print(product)
                                    product_id,product_name,category,_ = product
                                    # print("{} {} {}".format(product_id,product_name,category))

                                    # Connect to MariaDB to retrieve order details
                                    mariadb_connection = connect_mariadb()
                                    if mariadb_connection:
                                        mariadb_cursor = mariadb_connection.cursor()
                                        try:
                                            # sql = "SELECT o.order_id, o.product_id, o.quantity FROM orders_nairobi JOIN payments p ON o.order_id = p.order_id WHERE o.customer_id = {}".format(customer_id)
                                            sql = ("SELECT  o.product_id,count(o.order_id), "
                                                   "sum(o.quantity) FROM orders_nairobi o  "
                                                   "WHERE o.customer_id = {} AND o.product_id = {}").format(customer_id, product_id)
                                            mariadb_cursor.execute(sql)
                                            orders = mariadb_cursor.fetchall()
                                            order = orders[0]
                                            # print(orders)
                                            # print(order)

                                            order_product_id,total_orders, quantity = order

                                            # print (f"product_id:{product_id},total_orders:{total_orders}, quantity:{quantity}" )
                                            # # for order in orders:
                                            # #     # connect to postgreSQL to retrieve the product details
                                            # #     # product_detail = product_details(f"{order[1]}")
                                            # #     product_detail = 0

                                            print(f"    {product_details(product_id,product_category)} total order: {total_orders}, Quantity: {quantity}")
                                        except pymysql.Error as e:
                                            print(f"mariadb Error: {e}")

                                        finally:
                                            mariadb_cursor.close()
                                            mariadb_connection.close()
                                # print(f'finished {product_category} category')

                        except psycopg2.Error as e:
                            print(f"postgres Error: {e}")

                        finally:
                            post_cursor.close()
                            post_connection.close()

        except pymysql.Error as e:
            print(f"MySQL Error: {e}")
        finally:
            mysql_cursor.close()
            mysql_connection.close()
