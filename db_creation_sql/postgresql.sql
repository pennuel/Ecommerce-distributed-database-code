-- horizontally fragmented products tables
CREATE TABLE products_electronics (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE products_clothing (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);


INSERT INTO products_electronics (product_id, product_name, category, price) VALUES
(101, 'Laptop', 'Electronics', 1200),
(102, 'Smartphone', 'Electronics', 800);

INSERT INTO products_clothing (product_id, product_name, category, price) VALUES
(201, 'T-Shirt', 'Clothing', 250),
(202, 'Jeans', 'Clothings', 500)