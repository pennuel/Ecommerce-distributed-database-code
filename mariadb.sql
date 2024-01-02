create database e_commerce_site3_payment_order;
use e_commerce_site3_payment_order;


CREATE TABLE orders_nairobi (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);

CREATE TABLE orders_mombasa (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);


INSERT INTO orders_nairobi (order_id, customer_id, product_id, quantity, order_date) VALUES
(1001, 1, 101, 2, '2023-01-01'),
(1002, 2, 201, 3, '2023-01-02'),
(1003, 5, 102, 1, '2023-01-03'),
(1004, 6, 202, 2, '2023-01-04'),
(1005, 7, 101, 1, '2023-01-05');

INSERT INTO orders_mombasa (order_id, customer_id, product_id, quantity, order_date) VALUES
(1006, 345433, 201, 4, '2023-01-06'),
(1007, 345434, 102, 2, '2023-01-07'),
(1008, 345438, 202, 3, '2023-01-08'),
(1009, 345439, 101, 1, '2023-01-09'),
(1010, 3454310, 201, 2, '2023-01-10');


CREATE TABLE payments_credit_card (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_amount DECIMAL(10, 2),
    payment_date DATE,
    payment_method VARCHAR(50)
);

CREATE TABLE payments_paypal (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_amount DECIMAL(10, 2),
    payment_date DATE,
    payment_method VARCHAR(50)
);


INSERT INTO payments_credit_card (payment_id, order_id, payment_amount, payment_date, payment_method) VALUES
(5001, 1001, 2400, '2023-01-02', 'Credit Card'),
(5002, 1002, 225, '2023-01-03', 'Credit Card'),
(5003, 1003, 150, '2023-01-04', 'Credit Card'),
(5004, 1004, 300, '2023-01-05', 'Credit Card'),
(5005, 1005, 200, '2023-01-06', 'Credit Card');

INSERT INTO payments_paypal (payment_id, order_id, payment_amount, payment_date, payment_method) VALUES
(6001, 2001, 180, '2023-01-07', 'PayPal'),
(6002, 2002, 120, '2023-01-08', 'PayPal'),
(6003, 2003, 250, '2023-01-09', 'PayPal'),
(6004, 2004, 90, '2023-01-10', 'PayPal'),
(6005, 2005, 150, '2023-01-11', 'PayPal');