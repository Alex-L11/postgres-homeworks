-- SQL-команды для создания таблиц
CREATE TABLE employees(
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	title VARCHAR(255) NOT NULL,
	birth_date DATE NOT NULL,
	notes TEXT
);

CREATE TABLE customers(
	customer_id VARCHAR PRIMARY KEY,
	company_name VARCHAR(100) NOT NULL,
	contact_name VARCHAR (100) NOT NULL
);

CREATE TABLE orders(
	order_id INT PRIMARY KEY,
	customer_id VARCHAR(100) NOT NULL,
	employee_id INT NOT NULL,
	order_date DATE NOT NULL,
	ship_city VARCHAR(100) NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
