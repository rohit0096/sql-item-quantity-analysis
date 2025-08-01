
-- Customer Table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    age INT
);

-- Sales Table
CREATE TABLE Sales (
    sales_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Items Table
CREATE TABLE Items (
    item_id INT PRIMARY KEY,
    item_name NVARCHAR(100)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    sales_id INT,
    item_id INT,
    quantity INT,
    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);
