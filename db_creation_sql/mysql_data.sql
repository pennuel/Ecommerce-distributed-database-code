create database e_commerce_site1_customers;
use e_commerce_site1_customers;

-- Horizontally fragmented customers tables
CREATE TABLE customers_nairobi (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    region VARCHAR(50)
);

CREATE TABLE customers_mombasa (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    region VARCHAR(50)
);

-- Sample data for horizontally fragmented customers tables
INSERT INTO customers_nairobi (customer_id, customer_name, region) VALUES
(1, 'John Smith', 'Nairobi'),
(2, 'Alice Johnson', 'Nairobi'),
(5, 'Nancy Wangari', 'Nairobi'),
(6, 'Peter Kimani', 'Nairobi'),
(7, 'Isabel Mwende', 'Nairobi');

INSERT INTO customers_mombasa (customer_id, customer_name, region) VALUES
(345433, 'Hans Müller', 'Mombasa'),
(345434, 'Sophie Dupont', 'Mombasa'),
(345438, 'Joseph Auma', 'Mombasa'),
(345439, 'Alice Githua', 'Mombasa'),
(3454310, 'David Waweru', 'Mombasa');
