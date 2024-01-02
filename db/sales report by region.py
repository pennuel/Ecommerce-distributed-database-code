import psycopg2
import pymysql

from db.connect import connect_mariadb, connect_postgresql, connect_mysql
from db.product_test import product_details




def create_sales_by_payment_per_region_report():
    print("sales By payment per region")
    regions = ['nairobi']
    for region in regions:
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

                    count = 0
                    for product in products:
                        #Variable initialization
                        total_payment_paypal = 0.00
                        total_payment_credit = 0.00
                        credit_order = 0
                        paypal_order = 0
                        total_credit_quantity=0
                        total_paypal_quantity=0
                        product_id,product_name,category,_ = product

                        print(f"Product{product_name}")
                        # Connect to MariaDB to retrieve order details
                        mariadb_connection = connect_mariadb()
                        if mariadb_connection:
                            mariadb_cursor = mariadb_connection.cursor()
                            try:

                                #perfrom
                                sql = ("SELECT  o.product_id,count(o.order_id), "
                                       "sum(o.quantity) FROM orders_{} o  "
                                       "WHERE o.product_id = {}").format(region,product_id)
                                mariadb_cursor.execute(sql)
                                orders = mariadb_cursor.fetchall()


                                sql_orders = ("SELECT o.order_id, o.quantity FROM orders_{} o WHERE o.product_id = {}").format(region,product_id)
                                mariadb_cursor.execute(sql_orders)
                                orders_id = mariadb_cursor.fetchall()



                                for order_id in orders_id:
                                    id,credit_quantity = order_id
                                    sql_payments_credit = ("SELECT p.payment_amount FROM payments_credit_card p WHERE p.order_id= {}").format(id)
                                    mariadb_cursor.execute(sql_payments_credit)
                                    payment_credit = mariadb_cursor.fetchall()
                                    # print('payment_credit')
                                    # print(payment_credit[0])
                                    if payment_credit is None:
                                        pass
                                    else:
                                        # print(payment_credit)
                                        payment_credit_tuple = payment_credit[0]
                                        pay = payment_credit_tuple[0]

                                        total_payment_credit+=float(pay)
                                        # print(total_payment_credit)
                                        credit_order+=1
                                        total_credit_quantity+=credit_quantity
                                print(f" {product_details(product_id, product_category)} total order: {credit_order}, Quantity: {total_credit_quantity}, payment: Credit, Amount: {total_payment_credit}")

                                for order_id in orders_id:
                                    id, paypal_quantity = order_id
                                    sql_payments_paypal = ("SELECT p.payment_amount FROM payments_paypal p WHERE p.order_id= {}").format(id)
                                    mariadb_cursor.execute(sql_payments_paypal)
                                    payment_paypal = mariadb_cursor.fetchone()
                                    # print('payment_paypal')
                                    if payment_paypal is None:
                                        pass
                                    else:
                                        # print(payment_paypal[0])
                                        payment_paypal_tuple = payment_paypal[0]
                                        pay = payment_paypal_tuple[0]
                                        # print(pay)
                                        total_payment_paypal += float(pay)
                                        # print(total_payment_paypal)
                                        paypal_order+=1
                                        total_paypal_quantity+=paypal_quantity
                                # print (f"product_id:{product_id},total_orders:{total_orders}, quantity:{quantity}" )
                                # # for order in orders:
                                # #     # connect to postgreSQL to retrieve the product details
                                # #     # product_detail = product_details(f"{order[1]}")
                                # #     product_detail = 0
                                print(f" {product_details(product_id,product_category)} total order: {paypal_order}, Quantity: {total_paypal_quantity}, payment: Paypal, Amount: {total_payment_paypal}")
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


create_sales_by_payment_per_region_report()

# # Combine and process the data
# postgresql_data = fetch_postgresql_data()
# mariadb_data = fetch_mariadb_data()
#
# # Print the report
# print("Customer Orders Summary by Region:")
# print("Region\t\tTotal Orders")
#
# for region, total_orders in postgresql_data + mariadb_data:
#     print(f"{region}\t\t{total_orders}")
