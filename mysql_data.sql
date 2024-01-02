CREATE DATABASE e_commerce_site1;
USE e_commerce_site1;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    region VARCHAR(50)
);

INSERT INTO customers (customer_id,
                       customer_name,
                       region) VALUES
(1, 'John Smith', 'USA'),
(2, 'Alice Johnson', 'USA'),
(3, 'Hans Müller', 'Europe'),
(4, 'Sophie Dupont', 'Europe');
