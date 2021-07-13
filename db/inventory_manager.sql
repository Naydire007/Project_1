DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    company_name VARCHAR (255),
    description TEXT
);

CREATE TABLE inventory(
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(255),
    description VARCHAR (255),
    stock_quantity INT,
    buying_cost INT,
    selling_cost INT,
    manufacturers_id INT REFERENCES manufacturers(id)
);