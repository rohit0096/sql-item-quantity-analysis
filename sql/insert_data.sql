-- Insert data into Customer table
INSERT INTO Customer (customer_id, age) VALUES
(1, 34),
(2, 28),
(3, 45);
GO

-- Insert data into Items table
INSERT INTO Items (item_id, item_name) VALUES
(101, 'Laptop'),
(102, 'Mobile Phone'),
(103, 'Tablet');
GO

-- Insert data into Sales table
INSERT INTO Sales (sales_id, customer_id) VALUES
(1001, 1),
(1002, 2),
(1003, 3);
GO

-- Insert data into Orders table
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES
(5001, 1001, 101, 2),  -- Customer 1 bought 2 Laptops
(5002, 1001, 103, 1),  -- Customer 1 bought 1 Tablet
(5003, 1002, 102, 3),  -- Customer 2 bought 3 Mobile Phones
(5004, 1003, 101, 1);  -- Customer 3 bought 1 Laptop
GO
