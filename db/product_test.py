import psycopg2

from db.connect import connect_postgresql

def product_details(product_id,category):
    postgres_connection = connect_postgresql()

    if postgres_connection:
        try:
            with postgres_connection.cursor() as postgres_cursor:
                sql = "SELECT product_name, category, price FROM products_{} WHERE product_id = {}".format(category,product_id)
                postgres_cursor.execute(sql)
                product = postgres_cursor.fetchone()

                if product:
                    product_name, category, price = product
                    details ="Product ID: {}, Name: {}, Category: {}, Price: {}".format(product_id, product_name, category, price)
                    return details

        except psycopg2.Error as e:
            print(f"PostgreSQL Error: {e}")
        finally:
            postgres_connection.close()



if __name__ == "__main__":
    print(product_details(101,'electronics'))