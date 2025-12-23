CREATE TABLE categories(
	category_id SERIAL PRIMARY KEY,
	category_name VARCHAR(50),
	description TEXT,
	picture TEXT
);

CREATE TABLE suppliers(
	supplier_id SERIAL PRIMARY KEY,
	company_name VARCHAR(40),
	contact_name VARCHAR(30),
	contact_title VARCHAR(30),
	address VARCHAR(60),
	city VARCHAR(15),
	region VARCHAR(15),
	postal_code VARCHAR(10),
	country VARCHAR(15),
	phone VARCHAR(24), 
	fax VARCHAR(24),
	homepage TEXT
);

CREATE TABLE products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(50),
	supplier_id INT REFERENCES suppliers(supplier_id), 
	category_id INT REFERENCES categories(category_id),
	quantity_per_unit VARCHAR(20),
	unit_price REAL,
	units_in_stock SMALLINT,
	units_on_order SMALLINT,
	reorder_level SMALLINT,
	discontinued INT
);

CREATE TABLE orders(
	order_id SERIAL PRIMARY KEY,
	order_date DATE,
	required_date DATE,
	shipped_date DATE,
	ship_via SMALLINT,
	freight REAL,
	ship_name VARCHAR(40),
	ship_address VARCHAR(60),
	ship_city VARCHAR(15),
	ship_region VARCHAR(15),
	ship_postal_code VARCHAR(10),
	ship_country VARCHAR(15)
);

CREATE TABLE order_details(
	order_id INT REFERENCES orders(order_id),
	product_id INT REFERENCES products(product_id), 
	unit_price REAL,
	quantity SMALLINT,
	discount REAL
	PRIMARY KEY (order_id, product_id)
);

INSERT INTO categories(category_name, description, picture)
VALUES  ('Beverages', 'Soft drinks, coffees, teas, beers, and ales', '[binary data]'),
		('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings', '[binary data]'),
		('Confections', 'Desserts, candies, and sweet breads', '[binary data]'),
		('Dairy Products', 'Cheeses', '[binary data]'),
		('Grains/Cereals', 'Breads, crackers, pasta, and cereal', '[binary data]');

INSERT INTO suppliers(company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax, homepage)
VALUES  ('trefwdqwrgt', 'trbewrty', 'iuygfhj', 'uytrcgyuh', 'uyttfyguhjk', 'iougyftgfyguh', 'iuytyrcfgvjh', 'uiyttrfg', 'jkhjgfgy', 'iouytfugyiu', 'kuiytfdtryyiguuvgyi'),
		('trefwdqwrgt', 'trbewrty', 'iuygfhj', 'uytrcgyuh', 'uyttfyguhjk', 'iougyftgfyguh', 'iuytyrcfgvjh', 'uiyttrfg', 'jkhjgfgy', 'iouytfugyiu', 'kuiytfdtryyiguuvgyi'),
		('trefwdqwrgt', 'trbewrty', 'iuygfhj', 'uytrcgyuh', 'uyttfyguhjk', 'iougyftgfyguh', 'iuytyrcfgvjh', 'uiyttrfg', 'jkhjgfgy', 'iouytfugyiu', 'kuiytfdtryyiguuvgyi'),
		('trefwdqwrgt', 'trbewrty', 'iuygfhj', 'uytrcgyuh', 'uyttfyguhjk', 'iougyftgfyguh', 'iuytyrcfgvjh', 'uiyttrfg', 'jkhjgfgy', 'iouytfugyiu', 'kuiytfdtryyiguuvgyi'),
		('trefwdqwrgt', 'trbewrty', 'iuygfhj', 'uytrcgyuh', 'uyttfyguhjk', 'iougyftgfyguh', 'iuytyrcfgvjh', 'uiyttrfg', 'jkhjgfgy', 'iouytfugyiu', 'kuiytfdtryyiguuvgyi');

INSERT INTO products(
	product_name,
	supplier_id, 
	category_id,
	quantity_per_unit,
	unit_price,
	units_in_stock,
	units_on_order,
	reorder_level,
	discontinued
)
VALUES  ('nhtbgrte', 1, 2, '324', 34.179, 43, 22, 92, 49),
		('nhtbgrte', 1, 2, '324', 34.179, 43, 22, 92, 49),
		('nhtbgrte', 1, 2, '324', 34.179, 43, 22, 92, 49),
		('nhtbgrte', 1, 2, '324', 34.179, 43, 22, 92, 49),
		('nhtbgrte', 1, 2, '324', 34.179, 43, 22, 92, 49);

INSERT INTO orders(
	order_date,
	required_date,
	shipped_date,
	ship_via,
	freight,
	ship_name,
	ship_address,
	ship_city,
	ship_region,
	ship_postal_code,
	ship_country
)
VALUES  ('1999-01-08', '2000-12-11', '2000-10-02', 628, 76.888, 'jujhduw', 'iwehdikqjwd', 'kuwedb', 'iuehfi', 'uhdiw', 'ikwehfiu'),
		('1999-01-08', '2000-12-11', '2000-10-02', 628, 76.888, 'jujhduw', 'iwehdikqjwd', 'kuwedb', 'iuehfi', 'uhdiw', 'ikwehfiu'),
		('1999-01-08', '2000-12-11', '2000-10-02', 628, 76.888, 'jujhduw', 'iwehdikqjwd', 'kuwedb', 'iuehfi', 'uhdiw', 'ikwehfiu'),
		('1999-01-08', '2000-12-11', '2000-10-02', 628, 76.888, 'jujhduw', 'iwehdikqjwd', 'kuwedb', 'iuehfi', 'uhdiw', 'ikwehfiu'),
		('1999-01-08', '2000-12-11', '2000-10-02', 628, 76.888, 'jujhduw', 'iwehdikqjwd', 'kuwedb', 'iuehfi', 'uhdiw', 'ikwehfiu');

INSERT INTO order_details(
	order_id,
	product_id, 
	unit_price,
	quantity,
	discount
)
VALUES  (1, 4, 3, 46.937, 33, 28.388),
		(4, 2, 3, 46.937, 33, 28.388),
		(5, 1, 3, 46.937, 33, 28.388),
		(2, 1, 3, 46.937, 33, 28.388),
		(5, 3, 3, 46.937, 33, 28.388);


ALTER TABLE suppliers
ADD COLUMN muallif VARCHAR(50);

ALTER TABLE suppliers
RENAME COLUMN muallif TO author;

DELETE FROM products
WHERE product_id = 3;

UPDATE products
SET product_name = 'Konbu',
	supplier_id = 1, 
	category_id = 2,
	quantity_per_unit = '2 kg box',
	unit_price = 6,
	units_in_stock = 24,
	units_on_order = 0,
	reorder_level = 5,
	discontinued = 0
WHERE product_id = 4;
