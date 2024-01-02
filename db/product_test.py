# Import necessary library
import psycopg2

# Import custom function to connect to PostgreSQL
from db.dbconnect.connect import connect_postgresql

def product_details(product_id, category):
    # Connect to PostgreSQL to retrieve product details
    postgres_connection = connect_postgresql()

    # Check if the connection to PostgreSQL is successful
    if postgres_connection:
        try:
            # Use a context manager to automatically close the cursor when done
            with postgres_connection.cursor() as postgres_cursor:
                # SQL query to retrieve product details based on product ID and category
                sql = "SELECT product_name, category, price FROM products_{} WHERE product_id = {}".format(category, product_id)
                postgres_cursor.execute(sql)
                product = postgres_cursor.fetchone()

                # Check if the product details are retrieved successfully
                if product:
                    product_name, category, price = product
                    details = "Product ID: {}, Name: {}, Category: {}, Price: {}".format(product_id, product_name, category, price)
                    return details

        except psycopg2.Error as e:
            # Handle PostgreSQL errors
            print(f"PostgreSQL Error: {e}")

        finally:
            # Close the PostgreSQL connection
            postgres_connection.close()

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Test the product_details function with sample data
    print(product_details(101, 'electronics'))
