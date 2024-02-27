-- Table: category

-- DROP TABLE IF EXISTS category;

CREATE TABLE IF NOT EXISTS category
(
    category_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    category_name character varying(50) NOT NULL,
    active boolean NOT NULL,
    parent_category_id integer,
    CONSTRAINT pk__category__category_id PRIMARY KEY (category_id),
    CONSTRAINT fk__category__category_id FOREIGN KEY (parent_category_id)
        REFERENCES category (category_id)
)


-- Index: ux_category_name

-- DROP INDEX IF EXISTS idx__category__category_name;

CREATE UNIQUE INDEX IF NOT EXISTS idx__category__category_name
    ON category 
	
-- Table: customer

-- DROP TABLE IF EXISTS customer;

CREATE TABLE IF NOT EXISTS customer
(
    customer_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    last_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    CONSTRAINT pk__customer__customer_id PRIMARY KEY (customer_id)
)

-- Table: employee

-- DROP TABLE IF EXISTS employee;

CREATE TABLE IF NOT EXISTS employee
(
    employee_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    last_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    phone character varying(100) NOT NULL,
    "position" character varying(50) NOT NULL,
    CONSTRAINT pk__employee__employee_id PRIMARY KEY (employee_id),
    CONSTRAINT idx__employee__email UNIQUE (email)
)

-- Table: menu_item

-- DROP TABLE IF EXISTS menu_item;

CREATE TABLE IF NOT EXISTS menu_item
(
    menu_item_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    menu_item_name character varying(50) NOT NULL,
    category_id integer NOT NULL,
    price double precision NOT NULL,
    CONSTRAINT pk__menu_item__menu_item_id PRIMARY KEY (menu_item_id),
    CONSTRAINT fk__menu_item__category_id FOREIGN KEY (category_id)
        REFERENCES category (category_id)
)


-- Table: order

-- DROP TABLE IF EXISTS "order";

CREATE TABLE IF NOT EXISTS "order"
(
    order_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    menu_item_id integer NOT NULL,
    customer_id integer NOT NULL,
    quantity integer NOT NULL,
    order_date timestamp without time zone NOT NULL,
    employee_id integer,
    CONSTRAINT pk__order__order_id PRIMARY KEY (order_id),
    CONSTRAINT fk__order__customer_id FOREIGN KEY (customer_id)
        REFERENCES customer (customer_id),
    CONSTRAINT fk__order__employee_id FOREIGN KEY (employee_id)
        REFERENCES employee (employee_id),
    CONSTRAINT fk__order__menu_item_id FOREIGN KEY (menu_item_id)
        REFERENCES menu_item (menu_item_id) 
)
