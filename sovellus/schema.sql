CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE, 
    password TEXT, 
    admin INTEGER
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT,
    openinghours TEXT,
    address TEXT,
    info TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    restaurant_id INTEGER REFERENCES restaurants,
    rating INTEGER,
    comment TEXT
);