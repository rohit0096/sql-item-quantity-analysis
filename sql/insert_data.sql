-- Insert data into Customer table
INSERT INTO Customer (customer_id, age) VALUES
(1, 21),
(2, 23),
(3, 35);
GO

-- Insert data into Items table
INSERT INTO Items (item_id, item_name) VALUES
(1, 'x'),
(2, 'y'),
(3, 'z');
GO

-- Insert data into Sales table
INSERT INTO Sales (sales_id, customer_id) VALUES
(1, 1),
(2, 2),
(3, 2),
(4, 2),
(5, 3);
GO

-- Insert data into Orders table
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (1, 1, 1, 10); -- Customer 1 buys 10 x
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (2, 2, 1,  1); -- Customer 2 buys 1 x
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (3, 3, 2,  1); -- Customer 2 buys 1 y
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (4, 4, 3,  1); -- Customer 2 buys 1 z
INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (5, 5, 3,  2); -- Customer 3 buys 2 z
